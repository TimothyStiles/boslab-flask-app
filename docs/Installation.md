# PREPARE OPERATING SYSTEM
## Off of a fresh ubuntu 16.04
1. Update OS

```
$ sudo apt update
$ sudo apt upgrade
```
2. Make sure you're using Python 3

```
$ python --version # Check python version
python 2.7.12
$ echo "alias python=python3" >> ~/.bashrc # set 'python' alias to refer to python3
$ source ~/.bashrc # restart .bashrc to enable new additions
$ python --version # Check python version
```

3. Install Pycharm Community

```
$ sudo add-apt-repository ppa:mystic-mirage/pycharm
$ sudo apt update
$ sudo apt install pycharm-community
$ echo "alias charm=pycharm-community" >> ~/.bashrc
$ source ~/.bashrc # restart .bashrc to enable new additions
```

4. Install git, virtualenvwrapper, python-dev, pip

```
$ sudo apt install git virtualenvwrapper python-dev pip python3-dev python3-pip
$ sudo -H pip install --upgrade pip
$ sudo -H pip install virtualenvwrapper

```

5. Configure git

```
$ git config --global user.name “francisglee” # set github username
$ git config --global user.email “francis.g.lee@gmail.com” # set github user email
$ git config --global push.default simple
$ git config --global credential.helper cache # set default password keeper
$ git remote origin https://www.github.com/boslab/boslab-flask-app.git # set git remote
$ git remote -v # check git remote
```

2. Create app directory:

```
$ mkdir Projects
$ cd Projects
$ mkdir boslab-flask-app
$ cd boslab-flask-app
```

----------------------------------------------------------
# GETTING DATABASE UP AND RUNNING

1. Install Postgres

```
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install postgresql postgresql-contrib libpq-dev
```

2. Create database

```
$ sudo -i -u postgres psql
postgres$ ALTER USER postgres WITH PASSWORD 'password'; # give master-user, postgres, a password
postgres$ CREATE USER ifrancium WITH PASSWORD 'password'; # create admin user
postgres$ CREATE DATABASE boslab OWNER ifrancium ENCODING 'utf-8'; # create
database
```

-------------------------------------------------------------
# SET UP VIRTUAL ENVIRONMENT

1. Initialize git and virtual environment

```
$ git init
$ mkvirtualenv --python=/usr/bin/python3 boslab-flask-app
# Activate env: workon boslab-flask-app
```

2. Install python packages

```
$ pip install Flask psycopg2 Flask-SQLAlchemy Flask-Migrate Flask-Script requests
$ pip freeze > requirements.txt
```

-------------------------------------------------------------
# CREATE FILE STRUCTURE

1. Create File Structure

```
$ touch run.py setup.py .gitignore README.md
$ mkdir instance app docs tests api
$ cd app
$ touch __init__.py config.py app.py views.py models.py forms.py utils.py manage.py scrape.py
$ mkdir static templates
$ cd templates
$ touch index.html
$ cd ~/foods-app-database/app/static
$ mkdir css js
$ cd css
$ touch style.css bootstrap.css
$ cd ~/foods-app-database/app/static/js
$ touch style.js bootstrap.js
```

2.

-------------------------------
# RUN APP

1. initialize database

```
$ python manage.py db init # creates migrate folder with database schema
$ python manage.py db migrate # dumps instance of database
$ python manage.py db upgrade #

```
2. Run Server

```
$ python manage.py runserver # starts up the server
```
-------------------------------------------------
# IMPORT AND EXPORT POSTGRESQL DATABASE

1. Dump PostgreSQL
```
$ pg_dump -U USERNAME DBNAME > dbexport.pgsql
```

2. Upload from .pgsql file
```
$ psql -U USERNAME DBNAME < dbexport.pgsql
```

3. Upload from CSV file
