# JOBSJOBSJOBS: A Custom CMS

**JOBSJOBSJOBS** is a job listings website that has a simple, custom Content Management System (CMS), built using Python and Django for the back-end, and HTML, CSS, and JavaScript for the front-end.

<font color="blue"><center>[WIP: gif of CMS section]</center></font>

This project was built to support this **[online class]()**, which walks you through building this CMS from scratch.

## Introduction

The following instructions will allow you to copy the project and run it on your local machine for development and testing purposes. See **Deployment** section for notes on how to deploy the project on a live server.

## Table of Contents
* [Requirements](#requirements)
* [Installation](#installation)
* [Testing Locally](#testing-locally)
* [Deployment](#deployment)
* [Project Structure](#project-structure)
* [Frequently Asked Questions](#faqs)

## <a name="requirements"></a>Requirements

Before you can get this project to run on your local machine, you need to have the following installed on your system:

* Python **2.7**
* Django **1.11**

### **[Python]()**
Mac OS X comes with Python 2.7 out of the box, but it's best to double check anyway. Type the following on the command line to find out what version of Python your system has installed (if any):

```bash
$ python -V
```
If Python is installed, it will print its current version. If you don't get a response from the command, you should download and install Python [here](https://www.python.org/downloads/).

_Note: This build has not been tested on Python 3.x._


### **[Django]()**
Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Type the following on the command line to see if you have Django installed:

```bash
$ python -m django --version
```
If Django is installed, you should see the version of your installation. If it isn’t, you’ll get an error saying `No module named django`.

<font color="blue"><center>[WIP: Details about how to install Django if you don't already have it]</center></font>

_Note: The versions of Python and Django that you are using are important. For more info about version support, go to [Django's FAQ page](https://docs.djangoproject.com/en/1.11/faq/install/#faq-python-version-support)._

## <a name="installation"></a>Installation

Now that you have all the prerequisites installed, you're ready to clone this project and get the development environment running on your local machine.

### Initial Download

You can download the zip directly from Github or through the command line.

If downloading through the command line, navigate to the directory where you would like to copy this repository. This can be anywhere in your local file system, like your home directory. For example:

```bash
$ cd ~/
```

Afterwards, enter the following to clone this repository into a new directory in this location.

```bash
$ git clone git@github.com:michellecruz/jobs-cms.git
```

### Starting Your Development Environment

Now that you have the project stored locally, navigate to the directory of the repo (where **manage.py** is in the [Project Structure](#project-structure)).

```bash
$ cd jobs-cms
```

Type the following command to run your local server.

```bash
$ python manage.py runserver
```
Go to [http://localhost:8000](http://localhost:8000) and you should be able to see the website.

_Note: Since this was created to teach the viewer how to create a CMS, the filters throughout this job listing website **do not work** and are only there for style purposes._

## <a name="testing-locally"></a>Testing CMS Locally

Now that your website it up and running locally, you can access your admin panel to make changes to the website. Go to [http://localhost:8000/admin](http://localhost:8000/admin) and use the following login credentials:

username: <font color="red">```admin```</font>
password: <font color="red">```password```</font>

<font color="blue"><center>[WIP: add more testing explanations]</center></font>

## <a name="deployment"></a>Deployment

<font color="blue"><center>[WIP: add additional notes about how to deploy this on a live system]</center></font>

## Built With

* [Django]() - The web framework used.

## Authors

* **Michelle Cruz** <[michelle@thisalso.com](mailto:michelle@thisalso.com)>

## Acknowledgments

* Thanks to [Tyler Moody]() for help on creating the initial designs.
* Thanks to ...

# <a name="project-structure"></a>Project Structure
```
.
├── README.md
├── manage.py
├── db.sqlite3
├── 📁 joblisting (contains project settings and urls)
│      ├── __init__.py
│      ├── settings.py
│      ├── urls.py
│      └── wsgi.py
└── 📁 jobs (contains jobs app)
       ├── __init__.py
       ├── admin.py
       ├── apps.py
       ├── models.py
       ├── urls.py
       ├── views.py
       ├── 📁 migrations
       ├── 📁 static
       │      ├── 📁 css
       │      ├── 📁 images
       │      └── 📁 js
       └── 📁 templates
              ├── details.html
              ├── index.html
              ├── 📁 _includes
              ├── 📁 admin
              └── 📁 registration
                     ├── logged_out.html
                     └── login.html
```

# <a name="faqs"></a>Frequently Asked Questions

**What’s the difference between a project and an app on Django?**
*An app is a Web application that does something – e.g., a Weblog system, a database of public records or a simple poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.*
