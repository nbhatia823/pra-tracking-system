from definitions import Definitions

from flask_table import Table, Col
from flask_wtf import FlaskForm

from wtforms import StringField, BooleanField, DateField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

# flask table
class PRATable(Table):
    county = Col('County')
    lea = Col('LEA')
    issheriffsdept = Col("Is Sheriff's dept?")
    currentstatus = Col('Current status')
    dateofrequest = Col('Date of request')
    startdaterequested = Col('Start date requested')
    enddaterequested = Col('End date requested')
    startdatereturned = Col('Start date returned')
    enddatereturned = Col('End date returned')
    variableschecked = Col('Variables checked?')
    variablescomplete = Col('Variables complete?')
    dataqualitychecked = Col('Data quality checked?')
    dataactionable = Col('Data actionable?')
    datacleaned = Col('Data cleaned?')
    datageocoded = Col('Date geocoded?')
    dataanalyzed = Col('Data analyzed?')
    leadmember = Col('Current team lead')


# wtf flask form
class PRACreationForm(FlaskForm):
    county = StringField(
        'County', 
        validators=[DataRequired()])
    lea = StringField(
        'LEA', 
        validators=[DataRequired()])
    isSheriffsDept = BooleanField(
        "Is this a Sheriff's Dept?", 
        default='checked')
    dateOfLastContact = DateField(
        "Date of last contact")
    currentStatus = SelectField(
        'Current status', 
        choices=Definitions.STATUSES, 
        validators=[DataRequired()])
    comments = TextAreaField(
        'Additional comments')
    dateOfRequest = DateField(
        'Date request was made')
    startDateRequested = DateField(
        'Start date of requested data')
    endDateRequested = DateField(
        'End date of requeseted data')
    initialContactPerson = StringField(
        'Contact person', 
        validators=[DataRequired()])
    initialContactMethod = SelectField(
        'Contact method', 
        choices=Definitions.CONTACT_METHODS, 
        validators=[DataRequired()])
    initialContactInfo = StringField(
        'Contact info', 
        validators=[DataRequired()])
    leadMember = StringField(
        'Data division lead')
    linkToPRARequest = StringField(
        'Link to PRA request')


