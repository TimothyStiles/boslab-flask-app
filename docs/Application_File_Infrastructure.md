```
foods-app-database File Structure
├── requirements.txt
├── run.py
├── setup.py
├── instance
     ├── __init__.py
     └── config.py
├── app
     ├── __init__.py
     ├── config.py
     ├── app.py
     ├── views.py
     ├── models.py
     ├── forms.py
     ├── static
           ├── css
                ├── style.css
                └── bootstrap.css
           └── js
                ├── style.js
                └── bootstrap.js
     ├── templates
           └── index.html
     ├── utils.py
     ├── scrape.py
     └── manage.py
├── docs
     ├── jupyter-notebooks
     ├── installation.md
     ├── develop.md
     └── api.md
├── .gitignore
├── tests
├── api
├── DOCKERFILE
└── README.md
```

| Items                        | Description                                              |
| :--------------------------- | :------------------------------------------------------- |
| requirements.txt             | This file lists all of the Python packages that your app depends on. You may have separate files for production and dev dep. |
| run.py                       | This is the file that is invoked to start up a development server. It gets a copy of the app from your package and runs it. This won't be used in production, but it will see a lot of mileage in development. |
| setup.py                     | like __init__.py for the larger application (functions as .env or .envrc) |
| instance/config.py           | This file contains configuration variables that shouldn't be in version control. This includes things like API keys and database URIs containing passwords. This also contains variables that are specific to this particular instance of your application. For example, you might have DEBUG = False in config.py, but set DEBUG = True in instance/config.py on your local machine for development. Since this file will be read in after config.py, it will override it and set DEBUG = True. (also can function like .env or .envrc) |
| app                          | This is the package that contains you application |
| app/__init__.py              | This file initializes your application and brings together all of the various components. |
| app/config.py                | This file contains most of the configuration variables that your app needs. |
| app/app.py                   | This file contains apps and routes; this gets split up into a bunch of different files as your application scales |
| app/views.py                 | This is where the routes are defined. It may be split into a package of its own (yourapp/views/) with related views grouped together into modules.  Also can be referred to as controller.py |
| app/models.py                | This is where you define the models of your application. This may be split into several modules in the same way as views.py.  For us, this will describe our data. |
| app/forms.py                 | This is for security (WTForms, CSRF, SecureForms, reCAPTCHA) |
| app/static                   | This directory contains the public CSS, JavaScript, images and other files that you want to make public via your app. It is accessible from yourapp.com/static/ by default. |
| app/static/css/bootstrap.css | Description |
| app/static/css/style.css     | Description |
| app/static/js/bootstrap.js   | Description |
| app/static/js/style.js       | Description |
| app/templates                | This is where you'll put the Jinja2 templates for your app. |
| app/templates/index.html     | This is your homepage. |
| app/utils.py                 | This file contains generic python class wrappers. |
| app/scrape.py                | This file contains webscraping functions. |
| app/manage.py                | This file contains scripts that run database initiations, migrations, and upgrades. |
| docs                         | This folder contains documentation on installation and development
| docs/Installation.md         | This file describes how to set up a machineto run foods-app-database.
| docs/Application_File_Infrastructure.md | This file describes the file organization. |
| docs/Develop.md              | Description |
| .gitignore                   | Description |
| tests                        | Description |
| api                          | Description |
| DOCKERFILE                   | Description |
| README.md                    | This file contains the summary of this application
