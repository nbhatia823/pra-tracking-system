from classes.pra import Pra


class Definitions:
    STATUSES = [
        ('Data requested - no response', 'Data requested - no response'),
        ('Data requested - in process', 'Data requested - in process'),
        ('Data received - incomplete', 'Data received - incomplete'),
        ('Data received - no errors', 'Data received - no errors'),
        ('Data ready for analysis', 'Data ready for analysis'),
    ]

    CONTACT_METHODS = [
        ('phone', 'Phone'),
        ('email', 'Email'),
        ('fax', 'Fax'),
        ('portal', 'Portal'),
    ]

    DEFAULT_NUM_ROW_ENTRIES = 20

    DEFAULT_PRA_FIELDS = [
        Pra.id,
        Pra.county,
        Pra.lea,
        Pra.leadmember,
        Pra.startdaterequested,
        Pra.enddaterequested,
        Pra.dateofrequest,
        Pra.currentstatus
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
    ]
