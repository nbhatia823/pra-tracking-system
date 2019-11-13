from flask import Flask, render_template, request, redirect, flash, Blueprint
from flask_wtf.csrf import CSRFProtect

from classes.frontend_models import PRACreationForm, PRATable
from classes.pra import Pra
from db import Db
from api import pra_api

app = Flask(__name__)
app.register_blueprint(pra_api)
print(app.secret_key)
app.secret_key = 'the random string'
print(app.secret_key)

csrf = CSRFProtect(app)
app.config['WTF_CSRF_ENABLED'] = False


@app.route("/")
def home():
    pras = Pra.select()
    table = PRATable(pras)
    print("_____ TABLE _______")

    print(table)
    print("_____ TABLE _______")
    return render_template('index.html', table=table)


@app.route('/create', methods=['GET', 'POST'])
def create():
    form = PRACreationForm()

    if request.method == 'POST':
        print("reached1")
        if form.validate() == False:
            print("reached2")

            flash('Please correct missing fields.')
            return render_template('create.html', form=form)
        else:
            print("date form pra is\n")
            print(request.form['dateOfRequest'])
            print("if sherrifs dept set to\n")
            print(request.form)
            pra = Pra(
                comments=request.form['comments'],
                county=request.form['county'],
                currentstatus=request.form['currentstatus'],
                dateoflastcontact=request.form['dateoflastcontact'],
                dateofrequest=request.form['dateofrequest'],
                enddaterequested=request.form['enddaterequested'],
                initialcontactmethod=request.form['initialcontactmethod'],
                initialcontactinfo=request.form['initialcontactinfo'],
                initialcontactperson=request.form['initalcontactperson'],
                issheriffsdept=True if 'ifSheriffsDept' in request.form else False,
                lea=request.form['lea'],
                leadmember=request.form['leadmember'],
                linktoprarequest=request.form['linktoprarequest'],
                startdaterequested=request.form['startdaterequested'],
            )
            pra.save()
            return redirect('/')

    elif request.method == 'GET':
        return render_template("create.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
