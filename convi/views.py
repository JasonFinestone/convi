__author__ = 'jason'

from convi import app

@app.route('/')
def index():
    return 'Hello World!'
