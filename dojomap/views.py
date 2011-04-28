from dojomap import app
from flask import render_template

@app.route('/dojo/new')
def new_dojo():
    return render_template("new_dojo.html")
