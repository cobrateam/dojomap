from dojomap.models import Dojo
from flaskext import wtf
from wtforms.ext.appengine.db import model_form

DojoForm = model_form(Dojo, base_class=wtf.Form, exclude=('latitude', 'longitude'))
