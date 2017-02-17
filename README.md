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
6.  Python

#####Installation
1.  Clone the project: git clone https://github.com/pcote/twitterapp.git
2.  Go to the twitter application page to register a new app [here](https://apps.twitter.com/).  When done take note of the following pieces of information...
    * consumer key
    * consumer secret
    * access token key
    * access token secret
3.  Open up the file called Vagrantfile.  Make the following edits.
    * Fill in the values for consumer key and secret as well as access token key and secret.
    * Fill in the fields for certcity, certstate, and certcountry.  These fields are going to be for an SSL certificate that gets generated for you for this app.
4.  Open up a file called /etc/hosts in the editor of your choice. (note: admin rights required to edit this)
    * Add this line at the bottom: 192.168.33.10   twitterapp.com
    * Save the file.
5.  At the command line, go back to the main project folder where the Vagrantfile is.
6.  Type the following: vagrant up
7.  Get up and grab a cup of coffee.  This will take a few minutes.
8.  After setup process complete, open up a browser and go to your app [here](https://twitterapp.com).
9.  Congratulation, you are now all set up.

### Using Twitterapp

(todo)