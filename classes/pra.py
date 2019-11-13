from peewee import TextField, CharField, BooleanField, DateField
from peewee_setup import BaseModel, UnknownField

class Pra(BaseModel):
    comments = TextField(null=True)
    county = CharField(null=True)
    currentcontact = UnknownField(null=True)  # USER-DEFINED
    currentstatus = CharField(null=True)
    dataactionable = BooleanField(null=True)
    dataanalyzed = BooleanField(null=True)
    datacleaned = BooleanField(null=True)
    datageocoded = BooleanField(null=True)
    dataqualitychecked = BooleanField(null=True)
    dateoflastcontact = DateField(null=True)
    dateofrequest = DateField(null=True)
    enddaterequested = DateField(null=True)
    enddatereturned = DateField(null=True)
    initialcontactmethod = CharField(null=True)
    initialcontactinfo = CharField(null=True)
    initialcontactperson = CharField(null=True)
    issheriffsdept = BooleanField(null=True)
    lea = CharField(null=True)
    leadmember = CharField(null=True)
    linktoprarequest = CharField(null=True)
    startdaterequested = DateField(null=True)
    startdatereturned = DateField(null=True)
    updates = UnknownField(null=True)  # USER-DEFINED
    variables = UnknownField(null=True)  # ARRAY
    variableschecked = BooleanField(null=True)
    variablescomplete = BooleanField(null=True)


