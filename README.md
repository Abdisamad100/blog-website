# Title
Blog-website

# Description
Blog-Website is a personal blogging website where you can create and share your opinions and other users can read and comment on them. It also has random quotes that inspire the users. 

# Features
As a user of the web application you will be able to:

See all blogs
Create an account
Log in
Create a blog
Comment on a blog
See comments posted on each individual blog
Edit your profile i.e will be able to add a short bio about yourself and a profile picture
# Development
Getting started
Prerequisites
python3.6
virtual environment
pip
Cloning
In your terminal:

  $ git clone https://github.com/abdisamad100/blog-website.git
  $ cd blog-website
Running the Application
Install virtual environment using $ python3.6 -m venv --without-pip virtual

Activate virtual environment using $ source virtual/bin/activate

Download pip in our environment using $ curl https://bootstrap.pypa.io/get-pip.py | python
Create a start.sh file in the root of the folder and add the following code:

  export MAIL_USERNAME=<your-email-address>
  export MAIL_PASSWORD=<your-email-password>
  export SECRET_KEY=<your-secret-key>
Edit the configuration instance in manage.py by commenting on production instance and uncommenting development instance

To run the application, in your terminal:

  $ chmod a+x start.sh
  $ ./start.sh
Testing the Application
To run the tests for the class file:

  $ python3.6 manage.py server

# Technologies Used
Python3.6
Flask
HTML
Bootstrap


# Known Bugs
The blog doesn't meet all the user's stories/needs.


# Author 
Abdisamad Mohamed

# License
MIT License

Copyright (c) 2020 Abdisamad Mohamed










