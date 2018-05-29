# JOBSJOBSJOBS: A Custom CMS

**JOBSJOBSJOBS** is a job listing website that has a simple, custom Content Management System (CMS), built using Python and Django for the back-end, and HTML, CSS, and JavaScript for the front-end.

<p align="center">
  <kbd><img src="../assets/cms.gif?raw=true" width="400"></kbd>
</p>

This project was built to support this **[online class]()**, which walks you through building a custom CMS from scratch.


## Table of Contents
1. [Introduction](#intro)
* [Requirements](#requirements)
* [Installation](#installation)
* [Testing CMS Locally](#testing-locally)
* [Deployment](#deployment)
* [Project Structure](#project-structure)
* [Frequently Asked Questions](#faqs)


## <a name="intro"></a>Introduction

The next few sections will teach you how to copy this project and run it on your local machine for development and testing purposes. See the [Deployment](#deployment) section for notes on how to deploy the project on a live server.

## <a name="requirements"></a>Requirements

Before you can get this project to run on your local machine, you need to have the following installed on your system:

* Python **2.7**
* Django **1.11**

### **[Python](https://www.python.org)**
Mac OS X comes with Python 2.7 out of the box, but it's best to double check anyway. Type the following on the command line to find out what version of Python your system has installed (if any):

```bash
$ python -V
```
If Python is installed, it will print its current version. If you don't get a response from the command, you should download and install Python 2.7 [here](https://www.python.org/downloads/).

_Note: This build has not been tested on Python 3.x._


### **[Django](https://docs.djangoproject.com/en/1.11/)**
Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Type the following on the command line to see if you have Django installed:

```bash
$ python -m django --version
```
If Django is installed, you should see the version of your installation. If it isn’t, you’ll get an error saying `No module named django`. In that case, download and install Django 1.11 [here](https://www.djangoproject.com/download/1.11.13/tarball).

_Note: The versions of Python and Django that you are using are important. Django **1.11** is the last version to support Python **2.7**. For more info about version support, go to [Django's FAQ page](https://docs.djangoproject.com/en/1.11/faq/install/#faq-python-version-support)._

## <a name="installation"></a>Installation

Now that you have all the prerequisites installed, you're ready to clone this project and get the development environment running on your local machine.

### Initial Download

You can download the zip directly from Github or through the command line.

If you're downloading through the command line, navigate to the directory where you would like to copy this repository. This can be anywhere in your local file system, like your home directory. For example:

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

> username: ```admin```<br>
> password: ```password```

Once logged in, you'll have access to the Admin Dashboard, where you can add/edit/delete jobs and manage your authorized admins.

_Note: Because this is a demo, there are no confirmation states for **Deleting** or **Publishing**. But when you create your own CMS, it's recommended that you add these details to prevent accidental deletion of data._

## <a name="deployment"></a>Deployment

* [Python Anywhere](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/)

**[WIP: add additional notes about how to deploy this on a live system]**

## Built With

* [Django](https://www.djangoproject.com) - The web framework used.

## Authors

* **Michelle Cruz** <[michelle@thisalso.com](mailto:michelle@thisalso.com)>

## Acknowledgments

* Thanks to [Tyler Moody]() for help with creating the initial designs.
* Thanks to [siegelgale.com](http://www.siegelgale.com/brand-naming-8-great-fake-company-names) for the list of fictional company names.

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
>An app is a Web application that does something – e.g., a Weblog system, a database of public records or a simple poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

**Where is the data from the CMS stored?**
>In the [Project Structure](#project-structure), you'll notice the file **db.sqlite3**. This is where your data is stored. By default, Django's configuration uses SQLite, a lightweight database that is included in Python, so you won’t need to install anything else to support your database.

**Can I use the SQLite database for production?**
>In this case, yes. You can technically use SQLite for development and production, but for much heavier transaction loads there may be better options such as PostgreSQL or MySQL. Go [here](https://docs.djangoproject.com/en/1.11/ref/databases/) to learn more about using other databases.