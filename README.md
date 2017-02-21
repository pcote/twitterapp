#TwitterApp

###Description
A basic demonstration of a web application that looks up timelines of Twitter users and displays their tweets.

###How To Install

#####Pre-Requisites
TwitterApp is a Vagrant based project.  As such, here are the prerequisites required to get started.
1.  Vagrant
2.  VirtualBox 5
3.  64-bit Ubuntu Linux desktop O.S.
4.  Ansible
5.  Git
6.  Python 2.7

#####Installation
1.  Clone the project: <b>git clone https://github.com/pcote/twitterapp.git</b>
2.  Go to the twitter application page to register a new app [here](https://apps.twitter.com/).  When done take note of the following pieces of information...
    * consumer key
    * consumer secret
    * access token key
    * access token secret
3.  At the command line run <b>python setup.py</b>.  Follow the instructions for entering the Twitter API credentials and SSL certificate info.
4.  Open up a file called /etc/hosts in the editor of your choice. (note: admin rights required to edit this)
    * Add this line at the bottom: <b>192.168.33.10   twitterapp.com</b>
    * Save the file.
5.  At the command line, go back to the main project folder where the Vagrantfile is.
6.  Type: <b>vagrant up</b>
7.  Get up and grab a cup of coffee.  This will take a few minutes.
8.  After setup process complete, open up a browser and go to your app [here](https://twitterapp.com).
9.  Congratulation, you are now all set up.

### Using Twitterapp

Twitterapp lets you lookup people by their twitter handles and see their latest tweets.


#####Looking up a Twitter User's Tweets
1.  Go to https://twitterapp.com.  Alternatively, you can just click [here](https://twitterapp.com).
2.  If you see a message saying "Your connection is not private", don't worry.  You get this because this project uses a self-signed SSL certificate out-of-the-box.
    * Tell your browser it is safe to proceed.  For example, in Chrome, you would do so by clicking "Advanced" and then "Proceed to twitterapp.com (unsafe)"
    * When you arrive at the main page, you will see something like "Not Secure" and/or a crossed out "https" in the location bar.  In this case, this is fine.
    
3.  Type in the name of a twitter user by their handle.  Do not attach @ signs or hash symbols (#) to their handle.  For example....
    * Good: chicken_b
    * Bad: Phil Cote
    * Also Bad: @chicken_b, #chicken_b

4.  Select the maximum number of tweets for this user.
5.  Click the "Get Tweets" button.

#####Other Features
* __Drag around tweets:__ Click any tweet with your mouse and drag it up to whereever you want it in the tweet list.
* __Look up multiple users:__ Type in multiple twitter handles separated by commas.  Choosing "max tweets" will set the max on a __per user__ basis.
    * Example: chicken_b, blendernation
    