# UdacityBlogProject: Getting Started

This project was created for Udacity Nanodegree Full Stack Web Developer.

I choose to run at Heroku once that I had problem with Google Cloud billing system in Brazil.

# Rubric information

What framework is used? -> App was build using Django and Heroku.
Blog is deployed and viewable to the public. -> https://udacityblogproject.herokuapp.com/blog/

The signup, login, and logout workflow is intuitive to a human user. -> The best UX and UI that I can make without a designer.
Editing and viewing workflow is intuitive to a human user. -> Navigation tree is working, except date filter.
Pages render correctly. -> All the pages checked online. Have to secure allow scripts to be loaded because off Foundation framework.

User accounts are appropriately handled. -> Yes.
Account information is properly retained. -> Yes.
Usernames are unique. -> Yes.
Passwords are secure and appropriately used. -> Yes.

User permissions are appropriate for logged out users. -> Yes. Not allowed to create blog posts.
User permissions are appropriate for logged in users. -> Yes. Logged in users can create, edit, or delete blog posts they themselves have created. Users should only be able to like posts once and should not be able to like their own post.
Comment permissions are enforced. -> Yes.

Code should be readable per the Google Python Style Guide. -> Yes.
Code is well structured. -> Yes.
Code is well commented. -> Yes.

Are steps for running the project provided in a README file? -> Yes. ;-)

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone git@github.com:vrbarros/UdacityBlogProject.git
$ cd UdacityBlogProject

$ pip install -r requirements.txt

$ python manage.py migrate
$ python manage.py collectstatic

$ python manage.py runserver 8000
```

Your app should now be running on [localhost:8000](http://localhost:8000/).
