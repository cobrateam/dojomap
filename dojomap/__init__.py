from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'really secret, no?'

import dojomap.views
