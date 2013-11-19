Pure FTP Accounting Project
====================

This is a lightweight application to manage FTP user accounts.

It was developed and tested primarily with pure-ftpd but other servers that
support MySQL backend may work.

Requirements 
------------

 * Django 1.5
 * filebrowser
 * grappelli
 * south

Installation
------------

* Install requirements:

```sh
$ pip install -r requirements.txt
```

* Setup project

```sh
$ vim settings.py
$ python manage.py syncdb
$ python manage.py migrate
$ python manage.py createsuperuser

```
* Launch server:

```sh
$ python manage.py runserver
```

Usage 
-----

Set the following in settings.py:

 - **COMPLEX_MODE**: When set to False, there is only one user model that
corresponds to FTP users and django users at the same time. When set to True
there are two different models, FTPStaff and FCPClient. This setup is geared
towards a more enterprise setup where you can have FTPStaff who can
create/edit/delete other FTPClients but have no permissions over the other
staff accounts. Defaults to False

 - **FTP_CHROOT**: The FTP root directory. defaults to /home/ftp (note: the user
running this service should have write access to the ftp directory).

 - **USER_EXPIRY_DAYS**: By default, in complex mode, Client users are set to expire
after a set amount of days. Set this to 0 to disable this functionality.
