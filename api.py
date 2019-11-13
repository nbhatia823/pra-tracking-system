from flask import request, json, Response, Blueprint
from db import Db
from playhouse.shortcuts import model_to_dict

# i need to respond to POST and PUT and DELETE requests with success messages or error codes. 
# i need to send the proper response number.
# i need to respond to GET requests with a json body; 

pra_api = Blueprint('pra_api', __name__)

@pra_api.route('/api/pra', methods=['GET', 'POST'])
def post_or_get_pras():

    if request.method == 'GET':
        # read filters from query parameter and store as dictionary; 
        # each entry is field_name: filter_value i.e. LEA="Los Angeles Police Department"
        filters = request.args.to_dict()
        
        # "limit" is passed as normal query parameter. if present remove it from filters
        # so filters can be exclusively filters for "WHERE" query
        # if not present, then default limit will be used
        if "limit" in filters:
            limit = filters["limit"]
            del filters["limit"]
            pra_dicts = Db.get_pras(filters=filters, limit=limit)    
        else:
            pra_dicts = Db.get_pras(filters)
        
        # package pras as json
        pra_json = json.dumps(pra_dicts)
        return Response(pra_json,  
                        mimetype='application/json', 
                        status=200)
    
    elif request.method == 'POST':
        print("attempting to post new request")
        pra_field_mappings = get_pra_info_from_current_request()
        new_pra_id = Db.create_pra(pra_field_mappings)
        if new_pra_id != -1:
            return Response(status=201)
        else:
            return Response(status=400)

@pra_api.route('/api/pra/<id>', methods=['PUT', 'GET', 'DELETE'])
def get_or_update_or_delete_pra(id): # 'id' is string-type
    ``
    if request.method == 'PUT':
        pra_field_mappings = get_pra_info_from_current_request()
        rows_updated = Db.update_pra(id, pra_field_mappings)
        if rows_updated == 1:
            return Response(status=204)
        else:
            return Response(status=400)
    
    elif request.method == 'GET':
        pra_dict = Db.get_pra(id)
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

