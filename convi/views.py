from convi import app
from flask import session, make_response, send_file, request, render_template
import json

from convi.database import db_session

if app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler(LOG_FILE, maxBytes=256000, backupCount=5)
    file_handler.setLevel(logging.INFO)
    #file_handler.setLevel(logging.WARNING)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)


@app.errorhandler(500)
def internal_error(exception):
    app.logger.info('Info')
    app.logger.warn('Warn')
    app.logger.error('Error')
    app.logger.exception(exception)
    # return json.dumps(exception)
    # send_file("templates/500.html")
    return render_template('500.html'), 500


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html', title='Not Found'), 404


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
    if 'DB_SESSION' in app.config:
        app.config['DB_SESSION'].remove()


def _convert_to_JSON(result):
    """Convert result object to a JSON web request."""
    response = make_response(json.dumps(result))
    response.headers['Access-Control-Allow-Origin'] = "*"
    response.mimetype = "application/json"
    return response


@app.route("/")
def index():
    return send_file("templates/index.html")


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response



