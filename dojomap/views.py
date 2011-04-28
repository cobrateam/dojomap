from dojomap import app
from dojomap.forms import DojoForm
from dojomap.models import Dojo
from flask import render_template

@app.route('/dojo/new')
def new_dojo():
    return render_template("new_dojo.html")

@app.route('/dojo/new', methods=['POST'])
def create_dojo():
    form = DojoForm()

    if form.validate_on_submit():
        dojo = Dojo(name=form.name.data, description=form.description.data, address=form.address.data)
        dojo.put()
        return "Saved"

    return render_template("new_dojo.html", form=form)
