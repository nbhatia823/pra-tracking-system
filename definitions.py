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

    MAX_ROW_ENTRIES = 20

    DEFAULT_DESIRED_PRA_FIELDS = [
        Pra.id,
        Pra.county,
        Pra.lea,
        Pra.leadmember,
        Pra.startdaterequested,
        Pra.enddaterequested,
        Pra.dateofrequest,
        Pra.currentstatus
    ]