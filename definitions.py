from classes.pra import Pra


class Definitions:
    STATUSES = [
        ("Requested", "Requested"),
        ("Requested - No Response", "Requested - No Response"),
        ("Received - Incomplete", "Received - Incomplete"),
        ("Contesting", "Contesting"),
        ("Processing", "Processing"),
        ("Analyzing")
    ]

    CONTACT_METHODS = [
        ('phone', 'Phone'),
        ('email', 'Email'),
        ('fax', 'Fax'),
        ('portal', 'Portal'),
    ]

    DEFAULT_PRA_FIELDS = [
        Pra.id,
        Pra.county,
        Pra.lea,
        Pra.leadmember,
        Pra.startdaterequested,
        Pra.enddaterequested,
        Pra.dateofrequest,
        Pra.currentstatus,
        Pra.active,
        Pra.datelastupdated
    ]

    ALL_PRA_FIELDS = [
        Pra.comments,
        Pra.county,
        Pra.currentcontact,
        Pra.currentstatus,
        Pra.dataactionable,
        Pra.dataanalyzed,
        Pra.datacleaned,
        Pra.datageocoded,
        Pra.dataqualitychecked,
        Pra.datatype,
        Pra.dateoflastcontact,
        Pra.dateofrequest,
        Pra.datereceived,
        Pra.enddaterequested,
        Pra.enddatereturned,
        Pra.id,
        Pra.initialcontact,
        Pra.issheriffsdept,
        Pra.lea,
        Pra.leadmember,
        Pra.linktoprarequest,
        Pra.startdaterequested,
        Pra.startdatereturned,
        Pra.updates,
        Pra.variables,
        Pra.variableschecked,
        Pra.variablescomplete,
        Pra.active,
        Pra.datelastupdated

    ]

    STATUS_PRA_FIELDS = [
        Pra.county,
        Pra.currentstatus,
        Pra.dataactionable,
        Pra.dataanalyzed,
        Pra.datacleaned,
        Pra.datageocoded,
        Pra.dataqualitychecked,
        Pra.datatype,
        Pra.dateofrequest,
        Pra.datereceived,
        Pra.enddatereturned,
        Pra.issheriffsdept,
        Pra.lea,
        Pra.startdatereturned,
        Pra.variableschecked,
        Pra.variablescomplete,
        Pra.active,
        Pra.datelastupdated
    ]
