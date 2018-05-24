# JOBSJOBSJOBS: A Custom CMS

**JOBSJOBSJOBS** is a job listings website that has a simple, custom Content Management System (CMS), built using Python and Django for the back-end, and HTML, CSS, and JavaScript for the front-end.

This project was built to support this **[online class]()**, which goes through building the CMS from scratch.

## Introduction

The following instructions will allow you to copy the project and run it on your local machine for development and testing purposes. See **Deployment** section for notes on how to deploy the project on a live server.

## Table of Contents
* [Requirements](#requirements)
* [Installation](#installation)
* [Testing Locally](#testing-locally)
* [Deployment](#deployment)
* [Project Structure](#project-structure)

## <a name="requirements"></a>Requirements

To get this project to run on your local machine, you will need to have the following installed on your system:

* Python **2.7**
* Django **1.11**

###**[Python]()**
Mac OS X comes with Python 2.7 out of the box, but it's best to double check anyway. Type the following on the command line to find out what version of Python your system has installed (if any):

```bash
$ python -V
```
If Python is installed, it will print its current version. If you don't get a response from the command, you should download and install Python [here](https://www.python.org/downloads/).

*Note: This build has not been tested on Python 3.x.*


###**[Django]()**
Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Type the following on the command line to see if you have Django installed:

```bash
$ python -m django --version
```
If Django is installed, you should see the version of your installation. If it isn’t, you’ll get an error saying `No module named django`.

*Note: The versions of Python and Django that you are using are important. For more info about version support, go to [Django's FAQ page](https://docs.djangoproject.com/en/1.11/faq/install/#faq-python-version-support).*

## <a name="installation"></a>Installation

A step by step series of examples that tell you how to get a development environment running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

## <a name="testing-locally"></a>Testing Locally

Explain how to run tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```
etc...

## <a name="deployment"></a>Deployment

Add additional notes about how to deploy this on a live system...

## Built With

* [Django]() - The web framework used.

## Authors

* **Michelle Cruz** <[michelle@thisalso.com](mailto:michelle@thisalso.com)>

## Acknowledgments

* Thanks to [Tyler Moody]() for help on creating the initial designs.
* Thanks to ...

# <a name="project-structure"></a>Project Structure
```
README.md
📁 joblisting
	├── manage.py
	├── db.sqlite3
	├── 📁 joblisting
	│		 ├── __init__.py
	│		 ├── settings.py
	│		 ├── urls.py
	│		 └── wsgi.py
	└── 📁 jobs
	 		 ├── __init__.py
			 ├── admin.py
			 ├── apps.py
			 ├── models.py
			 ├── urls.py
			 ├── views.py
			 ├── 📁 migrations
			 ├── 📁 static
			 │	 	  ├── 📁 css
			 │		  ├── 📁 images
			 │		  └── 📁 js
			 └── 📁 templates
			 		  ├── details.html
			 		  ├── index.html
			 		  ├── 📁 _includes
			 		  ├── 📁 admin
			 		  └── 📁 registration
			        	  	   ├── logged_out.html
		        	  		   └── login.html
```
