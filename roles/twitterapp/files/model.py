from sqlalchemy import create_engine, Column, Text, Integer, VARCHAR, BLOB, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from configparser import ConfigParser
import os
import hashlib
import re
import string
import twitter


db_name = "appname"

# ENGINE SETUP
this_directory = __file__.rsplit(os.path.sep, maxsplit=1)[0]
config_file_path = "{}{}config.ini".format(this_directory, os.path.sep)
cp = ConfigParser()
cp.read(config_file_path)
config_sec = cp["dbconfig"]
user = config_sec.get("username")
pw = config_sec.get("password")
db_name = config_sec.get("database")
db_url = "mysql+pymysql://{}:{}@localhost/{}".format(user, pw, db_name)
eng = create_engine(db_url)

# TWITTER API SETUP
oauth_sec = cp["oauth"]
consumer_key = oauth_sec.get("consumer_key")
consumer_secret = oauth_sec.get("consumer_secret")
access_token_key = oauth_sec.get("access_token_key")
access_token_secret = oauth_sec.get("access_token_secret")
api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token_key,
                  access_token_secret=access_token_secret)


Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    username = Column(VARCHAR(50), primary_key=True, nullable=False)
    is_active = Column(Boolean, default=False)
    is_authenticated = Column(Boolean, default=False)
    is_anonymous = Column(Boolean, default=False)
    password = Column(Text, nullable=False)
    salt = Column(BLOB)

    def get_id(self):
        return self.username


Session = sessionmaker(bind=eng)
Base.metadata.create_all(eng)


def password_strong(pw):
    MIN_PW_LENGTH = 8
    if len(pw) < MIN_PW_LENGTH:
        return False
    if not re.search(r"\d+", pw):
        return False
    if not re.search(r"\w+", pw):
        return False
    if re.search(r"\s+", pw):
        return False
    if not set(string.punctuation).intersection(pw):
        return False
    return True


def create_user(uname, pw):
    if not password_strong(pw):
        msg = "Password requirements not met: Must be 8 characters or more with letters, numbers, punctuation, and no spaces"
        return msg

    sess = Session()
    salt_data = os.urandom(16)
    hasher = hashlib.sha256()
    hasher.update(salt_data + pw.encode())
    digest = hasher.hexdigest()
    user = User(username=uname, password=digest, salt=salt_data)

    sess.add(user)
    sess.commit()
    sess.close()
    return "created user: {}".format(uname)


def get_user(uname):
    sess = Session()
    user = sess.query(User).filter_by(username=uname).one_or_none()
    sess.close()
    return user


def is_password_valid(uname, pw, prehashed=False):
    if prehashed:
        password_arg = pw
    else:
        salt_data = get_user(uname).salt
        hasher = hashlib.sha256()
        hasher.update(salt_data + pw.encode())
        password_arg = hasher.hexdigest()

    user = get_user(uname)
    if user and user.password == password_arg:
        return True
    return False


def set_authenticate(uname, auth_status):
    sess = Session()
    user = get_user(uname)
    user.is_authenticated = auth_status
    sess.add(user)
    sess.commit()
    sess.close()


def get_tweets(screen_name, num_tweets):
    timeline = api.GetUserTimeline(screen_name=screen_name, count=num_tweets)
    timeline = [tweet.AsDict() for tweet in timeline]
    cleaned_up_list = []
    for entry in timeline:
        short_entry = dict()
        short_entry["id"] = entry["id"]
        short_entry["screen_name"] = entry["user"]["screen_name"]
        short_entry["message"] = entry["text"]
        short_entry["date"] = entry["created_at"]
        cleaned_up_list.append(short_entry)
    return cleaned_up_list