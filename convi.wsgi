import os,sys

PROJECT_DIR = '/apps/www/raiseFogBugz'

activate_this = os.path.join(PROJECT_DIR, 'bin', 'activate_this.py')
#activate_this = '/apps/www/raiseFogBugz/flask/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
sys.path.append(PROJECT_DIR)

from raiseFogBugz import app as application

#def application(environ, start_response):
#  start_response('200 OK', [('Content-Type', 'text/plain')])
#  yield 'Hello World\n'
~
