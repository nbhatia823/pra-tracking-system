from flask import Flask, render_template, request, redirect, flash
from flask_wtf.csrf import CSRFProtect

from models import *
from frontend_models import *
from definitions import *

app = Flask(__name__)
app.secret_key = 'the random string'
csrf = CSRFProtect(app)

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
                currentstatus=request.form['currentStatus'],
                dateoflastcontact=request.form['dateOfLastContact'],
                dateofrequest=request.form['dateOfRequest'],
                enddaterequested=request.form['endDateRequested'],
                initialcontactmethod=request.form['initialContactMethod'],
                initialcontactinfo=request.form['initialContactInfo'],
                initialcontactperson=request.form['initialContactPerson'],
                issheriffsdept=True if 'ifSheriffsDept' in request.form else False,
                lea=request.form['lea'],
                leadmember=request.form['leadMember'],
                linktoprarequest=request.form['linkToPRARequest'],
                startdaterequested=request.form['startDateRequested'],
            )
            pra.save()
            return redirect('/')
        print("reached3")

    elif request.method == 'GET':
        return render_template("create.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
