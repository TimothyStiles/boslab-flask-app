from flask import Flask

app = Flask(__name__)

from views import *


# run chron job
# download data from site
# create model instance
# upload data to database

if __name__ == '__main__':
    app.run()

