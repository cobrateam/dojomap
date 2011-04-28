from google.appengine.ext import db

class Dojo(db.Model):
    name = db.StringProperty(required=True)
    description = db.TextProperty(required=True)
    address = db.TextProperty(required=True)

    latitude = db.FloatProperty()
    longitude = db.FloatProperty()
