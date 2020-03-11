# djangoofc

How To Install Django and Set Up a Development Environment on Ubuntu 16.04

Step 1 — Install Python and pip
or
Install Python3 and pip3
To install Python we must first update the local APT repository. In your terminal window, we’ll input the command that follows. Note that the -y flag answers “yes” to prompts during the upgrade process. Remove the flag if you’d like the upgrade to stop for each prompt.

sudo apt-get update && sudo apt-get -y upgrade
When prompted to configure grub-pc, you can press ENTER to accept the default, or configure as desired.

It is recommended by the Django Software Foundation to use Python 3, so once everything is updated, we can install Python 3 by using the following command:

sudo apt-get install python3
To verify the successful installation of Python 3, run a version check with the python3 command:

python3 -V
The resulting output will look similar to this:

Output
python 3.5.2
Now that we have Python 3 installed, we will also need pip in order to install packages from PyPi, Python’s package repository.

sudo apt-get install -y python3-pip
To verify that pip was successfully installed, run the following command:

pip3 -V
You should see output similar to this:

Output
pip 8.1.1 from /usr/lib/python3/dist-packages (python 3.5)
Now that we have pip installed, we have the ability to quickly install other necessary packages for a Python environment.

-------------------------------------------
-------------------------------------------

+++++++++++++++++++++++++++++++
 Step 2 — Install virtualenv +
+++++++++++++++++++++++++++++++
virtualenv is a virtual environment where you can install software and Python packages in a contained development space, which isolates the installed software and packages from the rest of your machine’s global environment. This convenient isolation prevents conflicting packages or software from interacting with each other.

To install virtualenv, we will use the pip3 command, as shown below:

pip3 install virtualenv
Once it is installed, run a version check to verify that the installation has completed successfully:

virtualenv --version
We should see the following output, or something similar:

Output
15.1.0
You have successfully installed virtualenv.

At this point, we can isolate our Django web application and its associated software dependencies from other Python packages or projects on our system.

---------------------------------------------
---------------------------------------------
Step 3 — Install Django

There are three ways to install Django. We will be using the pip method of installation for this tutorial, but let’s address all of the available options for your reference.

Option 1: Install Django within a virtualenv.
This is ideal for when you need your version of Django to be isolated from the global environment of your server.
Option 2: Install Django from Source.
If you want the latest software or want something newer than what your Ubuntu APT repository offers, you can install directly from source. Note that opting for this installation method requires constant attention and maintenance if you want your version of the software to be up to date.
Option 3: Install Django Globally with pip.
The option we are going with is pip 3 as we will be installing Django globally.

mkdir django-apps
cd django-apps 

While inside the django-apps directory, create your virtual environment. Let’s call it env.

virtualenv env
Now, activate the virtual environment with the following command:

source env/bin/activate 
      (or)
. env/bin/activate

You’ll know it’s activated once the prefix is changed to (env), which will look similar to the following depending on what directory you are in:

(env) sureshk: $ 

Within the environment, install the Django package using pip. Installing Django allows us to create and run Django applications. To learn more about Django, read our tutorial series on Django Development.

(env) sureshk: $ pip install django
Once installed, verify your Django installation by running a version check:

(env) sureshk: $ django-admin --version
This, or something similar, will be the resulting output:

Output
2.0.1
With Django installed on your server, we can move on to creating a test project to make sure everything is working correctly.

Starting the Project

(env) sureshk: $ django-admin startproject djangoprojects


#Let’s look at what startproject created:

djangoprojects/
    manage.py
    djangoprojects/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
These files are:

The outer djangoprojects/ root directory is a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.
manage.py: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.


django-admin is Django’s command-line utility for administrative tasks. This document outlines all it can do.

In addition, manage.py is automatically created in each Django project. It does the same thing as django-admin but also sets the DJANGO_SETTINGS_MODULE environment variable so that it points to your project’s settings.py file.

A Django settings file contains all the configuration of your Django installation. This document explains how settings work and which settings are available.

A settings file is just a Python module with module-level variables.

Here are a couple of example settings:

ALLOWED_HOSTS = ['www.example.com']
DEBUG = False
DEFAULT_FROM_EMAIL = 'webmaster@example.com'

A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Within a module, the module’s name (as a string) is available as the value of the global variable __name__.

The inner djangoprojects/ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. djangoprojects.urls).
djangoprojects/__init__.py: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.
djangoprojects/settings.py: Settings/configuration for this Django project. Django settings will tell you all about how settings work.
djangoprojects/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.
djangoprojects/asgi.py: An entry-point for ASGI-compatible web servers to serve your project. See How to deploy with ASGI for more details.
djangoprojects/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details.




Jinja
Jinja2 is a full-featured template engine for Python. It has full unicode support, an optional integrated sandboxed execution environment, widely used and BSD licensed.

It's a Template Engine system, and its syntax is based on jinja. 

example:
{% extends "layout.html" %}
{% block body %}
  <ul>
  {% for user in users %}
    <li><a href="{{ user.url }}">{{ user.username }}</a></li>
  {% endfor %}
  </ul>
{% endblock %}