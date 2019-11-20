from classes.pra import Pra
from definitions import Definitions

from functools import reduce
import operator

class Db:

# ive sent all my responses as models right now. is that how i should send them? or should i send them as objects? consider a function that converts from an object to json or to a final ready to deliver state

    ### CRUD methods
    ### All methods are static because we are not creating an instantiation of Db

    # READ methods

    # Return list of pras with the desired columns; fields/columns are editable by passing in array of fields accessible by Pra.fieldname
    @staticmethod
    def get_pras(filters=None, limit=Definitions.DEFAULT_NUM_ROW_ENTRIES, fields=Definitions.DEFAULT_PRA_FIELDS):
        if filters:
            expr_filters = Db.convert_filter_dict_to_peewee_expr(filters)
            pras = Pra.select(*fields).where(expr_filters).limit(limit).dicts().execute()
        else:
            pras = Pra.select(*fields).limit(limit).dicts().execute()
        pras = [pra for pra in pras]
        return pras

    # Return a single pra with id=id and only return desired columns;
    # need to unpack array response from select query and send model only
    @staticmethod
    def get_pra(id, fields=Definitions.DEFAULT_PRA_FIELDS):
        print("attempting to print ")
        pras = Pra.select(**fields).where(Pra.id == id).limit(1).dicts().execute()
        if len(pras) == 1:
            return pras[0]
        else:
            return None

    # CREATE methods

    # Creates a pra using field_mapping which is a mapping of field_name to value as dict
    @staticmethod
    def create_pra(field_mapping):
        try:
            return Pra.insert(**field_mapping).execute()
        except:
            return -1
        

    # UPDATE methods

    # Updates a pra using field_mapping which is a mapping of field_name to value as dict
    @staticmethod
    def update_pra(id, field_mapping):
        try:
            return Pra.update(**field_mapping).where(Pra.id == id).execute()
        except:
            return -1

    # Deletes a pra using id; returns number of rows deleted
    @staticmethod
    def delete_pra(id):
        return Pra.delete().where(Pra.id == id).execute()



    ######################################



    ### Helper methods

    # converts filters given as dict to peewee logical anded expression
    @staticmethod
    def convert_filter_dict_to_peewee_expr(filters):
        expression_list = [getattr(Pra, field) == value
            for field, value in filters.items()]
        anded_expr = reduce(operator.and_, expression_list)
        return anded_expr


    @staticmethod
    def convert_array_fields_to_peewee_fields(fields):
        peewee_fields = []
        for field in fields:
            peewee_fields.append(getattr(Pra, field))