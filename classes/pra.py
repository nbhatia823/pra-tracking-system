from peewee import TextField, CharField, BooleanField, DateField, TimestampField
from peewee_setup import BaseModel, db_helper
from playhouse.postgres_ext import ArrayField, JSONField

class Pra(BaseModel):
    comments = TextField(null=True)
    county = CharField(null=True)
    currentcontact = JSONField(null=True)        # three keys: "name", "method", "method_info" with corresonding values    
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
    initialcontact = JSONField(null=True)       # three keys: "name", "method", "method_info" with corresonding values
    issheriffsdept = BooleanField(null=True)
    lea = CharField(null=True)
    leadmember = CharField(null=True)
    linktoprarequest = CharField(null=True)
    startdaterequested = DateField(null=True)
    startdatereturned = DateField(null=True)
    updates = JSONField(null=True)              # each entry is stored with key as timestamp and value as the note
    variables = JSONField(null=True)            # each entry is stored with variable name as key, and then two subkeys: 
                                                ### the subkeys are requested (bool as value) and received (bool as value)
    variableschecked = BooleanField(null=True)
    variablescomplete = BooleanField(null=True)


db_helper.create_tables([Pra])
