from config import Config
from peewee import PostgresqlDatabase, Model, TextField, CharField, BooleanField, DateField



db = PostgresqlDatabase(
    Config.DATABASE,
    user=Config.USERNAME,
    password=Config.PASSWORD,
    host=Config.HOST,
    port=Config.PORT,
)

# peewee models
class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = db

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


