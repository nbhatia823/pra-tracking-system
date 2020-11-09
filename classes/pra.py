from peewee import TextField, CharField, BooleanField, DateField, TimestampField
from peewee_setup import BaseModel, db_helper
from playhouse.postgres_ext import ArrayField, JSONField


class Pra(BaseModel):
    active = BooleanField(null=True)
    comments = TextField(null=True)
    county = CharField(null=True)
    # three keys: "name", "method", "info" with corresonding values
    currentcontact = JSONField(null=True)
    currentstatus = CharField(null=True)
    dataactionable = BooleanField(null=True)
    dataanalyzed = BooleanField(null=True)
    datacleaned = BooleanField(null=True)
    datageocoded = BooleanField(null=True)
    datatype = CharField(null=True)
    dataqualitychecked = BooleanField(null=True)
    dateoflastcontact = CharField(null=True)
    dateofrequest = CharField(null=True)
    datereceived = CharField(null=True)
    enddaterequested = CharField(null=True)
    enddatereturned = CharField(null=True)
    # three keys: "name", "method", "info" with corresonding values
    initialcontact = JSONField(null=True)
    issheriffsdept = BooleanField(null=True)
    lastupdated = CharField(null=True)
    lea = CharField(null=True)
    leadmember = CharField(null=True)
    linktoprarequest = CharField(null=True)
    startdaterequested = CharField(null=True)
    startdatereturned = CharField(null=True)
    # each entry is stored with key as timestamp and value as the note
    updates = JSONField(null=True)
    # each entry is stored with variable name as key, and then two subkeys:
    variables = JSONField(null=True)
    # the subkeys are requested (bool as value) and received (bool as value)
    variableschecked = BooleanField(null=True)
    variablescomplete = BooleanField(null=True)
