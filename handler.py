import os, sys

app_dir = os.path.dirname(os.path.abspath(__file__))
libs_dir = os.path.join(app_dir, 'libs')
sys.path.insert(0, libs_dir)

from google.appengine.ext.webapp.util import run_wsgi_app
from dojomap import app

run_wsgi_app(app)
