from flask import Flask, request
from flask_restful import abort, Api, Resource, reqparse
from sendi import fix_engine
from os import listdir
import json

app = Flask(__name__)

app.config.from_pyfile('config.py')

api = Api(app)


def abort_if_no_csv_files_to_process():
    from config import CSV_IN_DIR
    if len(listdir(CSV_IN_DIR)) == 0:
        return {'FileName': None}

# returns vtmf object from parsing a csv file or if vtmf object supplied, returns fix equivalent
# if a csv file is parsed, it's deleted afterwards and the next file in the list is processed


class ConvProt(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        # get required vtmf's based on strategy name that we get from db route
        # validations
        self.reqparse.add_argument('ORDERID', type=int, required=True, help='ORDERID needed', location='json')
        self.reqparse.add_argument('SYMBOL', type=str, required=True, help='SYMBOL needed', location='json')
        self.reqparse.add_argument('ORDQTY', type=int, required=True, help='ORDQTY needed', location='json')
        self.reqparse.add_argument('ROUTE', type=str, required=True, help='ROUTE needed', location='json')
        self.reqparse.add_argument('PRICE', type=float, required=True, help='PRICE needed', location='json')
        super(ConvProt, self).__init__()

    def get(self):
        abort_if_no_csv_files_to_process()
        return json.dumps(fix_engine.get_vtmf())
    def post(self):
        vtmf = json.loads(request.data)
        return json.dumps(fix_engine.put_vtmf(vtmf))


# returns orders that have been proccessed using db and if fix object supplied, sends a new fix order message
# new order message updates the database
class OrdProc(Resource):
    def get(self):
        return fix_engine.get_orders()
    def post(self):
        fix = json.loads(request.data)
        return json.dumps(fix_engine.send_fix(fix))


api.add_resource(ConvProt, '/process', '/process/<order_id>', endpoint='process')
api.add_resource(OrdProc, '/orders', '/orders/<fix_id>', endpoint='orders')



from convi import views, models


__author__ = '86286K'