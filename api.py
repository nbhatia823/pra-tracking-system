from flask import request, json, Response, Blueprint
from db import Db
from playhouse.shortcuts import model_to_dict
from definitions import Definitions
from config import Config
from flask_bcrypt import check_password_hash, generate_password_hash


pra_api = Blueprint('pra_api', __name__)


@pra_api.route('/api/login', methods=['POST'])
def login():
    login_info = request.json
    username = login_info["username"].lower()
    password = login_info["password"]

    try:

        if username == Config.ADMIN_USERNAME and check_password_hash(Config.ADMIN_PASSWORD, password):
            # Login as admin
            return Response(json.dumps({"access": "admin"}),
                            mimetype='application/json',
                            status=200)
        elif username == Config.GUEST_USERNAME and check_password_hash(Config.GUEST_PASSWORD, password):
            # Login as guest
            return Response(json.dumps({"access": "guest"}),
                            mimetype='application/json',
                            status=200)
        else:
            return Response(status=400)
    except:
        return Response(status=400)


@pra_api.route('/api/pra', methods=['GET', 'POST'])
def post_or_get_pras():

    if request.method == 'GET':
        # read filters from query parameter and store as dictionary;
        # each entry is field_name: filter_value i.e. LEA="Los Angeles Police Department"
        query_params = request.args.to_dict()

        # "limit" is passed as normal query parameter. if present remove it and store in limit
        # so filters can be exclusively filters for "WHERE" query
        # if not present, then default limit will be used
        if "limit" in query_params:
            limit = query_params["limit"]
            del query_params["limit"]
        else:
            limit = Definitions.DEFAULT_NUM_ROW_ENTRIES

        # "fields" passed as array of fields, perform same as above
        if "fields" in query_params:
            fields_requested = query_params["fields"]
            del query_params["fields"]
            if fields_requested == "all":
                fields = Definitions.ALL_PRA_FIELDS
            elif fields_requested == "status":
                fields = Definitions.STATUS_PRA_FIELDS
            else:
                fields = Definitions.DEFAULT_PRA_FIELDS
        else:
            fields = Definitions.DEFAULT_PRA_FIELDS

        # remaining parameters make up the filters
        filters = query_params

        pra_dicts = Db.get_pras(
            fields=fields, filters=filters, limit=limit)

        # package pras as json
        pra_json = json.dumps(pra_dicts)
        return Response(pra_json,
                        mimetype='application/json',
                        status=200)

    elif request.method == 'POST':
        pra_field_mappings = get_pra_info_from_current_request()
        new_pra_id = Db.create_pra(pra_field_mappings)
        if new_pra_id != -1:
            return Response(status=201)
        else:
            return Response(status=400)


@pra_api.route('/api/pra/<id>', methods=['PUT', 'GET', 'DELETE'])
def get_or_update_or_delete_pra(id):  # 'id' is string-type

    if request.method == 'PUT':
        pra_field_mappings = get_pra_info_from_current_request()
        rows_updated = Db.update_pra(id, pra_field_mappings)

        if rows_updated == 1:
            return Response(status=204)
        else:
            return Response(status=400)

    elif request.method == 'GET':
        query_params = request.args.to_dict()
        if "fields" in query_params:
            fields_requested = query_params["fields"]
            if fields_requested == "all":
                fields = Definitions.ALL_PRA_FIELDS
            elif fields_requested == "status":
                fields = Definitions.STATUS_PRA_FIELDS
            else:
                fields = Definitions.DEFAULT_PRA_FIELDS
        else:
            fields = Definitions.DEFAULT_PRA_FIELDS
        pra_dict = Db.get_pra(id, fields=fields)
        # if the pra with given id exists, send it back as json;
        if pra_dict:
            pra_json = json.dumps(pra_dict)
            return Response(pra_json,
                            mimetype='application/json',
                            status=200)
        # else if not found, return 404 code saying not found
        else:
            return Response(status=404)

    elif request.method == 'DELETE':
        rows_deleted = Db.delete_pra(id)
        if rows_deleted == 1:
            return Response(status=204)
        else:
            return Response(status=400)

# reads field_mappings from body of request and returns as a dictionary of field_name:
# field_value; must be a json-type header in request


def get_pra_info_from_current_request():
    field_mappings = request.json
    return field_mappings
