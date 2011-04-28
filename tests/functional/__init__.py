from dojomap import app

def setup():
    app.config['TESTING'] = True
    app.config['CSRF_ENABLED'] = False
