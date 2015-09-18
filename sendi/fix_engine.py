from convi.config import CSV_IN_DIR, CSV_OUT_DIR
from convi.database import db_session
from convi.models import Strategy, Order, Fix, Vtmf, Map
from os import listdir, rename, path
import csv

vtmf_list = {
             'Order1': {'ORDERID': 12345, 'SYMBOL': 'VOD.L', 'ORDQTY': 10000},
             'Order2': {'ORDERID': 152345, 'SYMBOL': 'DTEG.I', 'ORDQTY': 100400},
             'Order3': {'ORDERID': 152345, 'SYMBOL': 'DTEG.I', 'ORDQTY': 100400}
            }

vtmf_from_csv = {'ORDERID': 912345, 'SYMBOL': 'NZT.L', 'ORDQTY': 99834000}

fix_map = {'ORDERID': '100', 'SYMBOL': '55', 'ORDQTY': '756'}
vtmf_map = {'100': 'ORDERID', '55': 'SYMBOL', '756': 'ORDQTY'}

def find_csv_filenames(path_to_dir,suffix=".csv"):
    filenames = listdir(path_to_dir)
    return [filename for filename in filenames if filename.endswith(suffix)]


def get_vtmf():
    # for csv files in directory , get the vtmf headings and the values in column 1 and column2
    number_of_csv_files = len(find_csv_filenames(CSV_IN_DIR))
    print number_of_csv_files
    if number_of_csv_files > 0:
        # files = []
        for afile in listdir(CSV_IN_DIR):
            if afile.endswith('.csv'):
                # print(afile)
                # files.append(afile)
                full_path = path.join(CSV_IN_DIR, afile)
                move_path = path.join(CSV_OUT_DIR, afile)
                f = open(full_path, 'rt')
                try:
                    reader = csv.DictReader(f, restkey='NO_VTMF',restval='NO_VALUE')
                    msg_type = 'NEW_ORDER'
                    order_details = {}
                    for row in reader:
                        order_details[msg_type] = row
                        msg_type = 'RESPONSE'

                finally:
                    f.close()
                    # move file to output dir
                    rename(full_path,move_path)
                    # TODO this rename could fail so think of a way to prevent that
                    break

        return order_details


def put_vtmf(vtmf):
    """
    return fix for vtmf
    split order and response
    get route from order
    convert the entire vtm into fix equiv
    use the required and optional from strategy to identify which tags to keep.
    shorten the message, based on route, to only include those.
    pass the fix message back to frontend
    TODO: add more stuff around here, this does a good job of extracting what is needed to send via fix
          but we can return original orderid, client id, trader id, maybe some snapshot market data even.
           then pass just the required bit of fix to the quickfix application to send a new order message.
    """
    # fix_map = {'ORDERID': 100, 'SYMBOL': 55, 'ORDQTY': 756}
    # for order in vtmf:
    order_message = vtmf.get('NEW_ORDER')
    order_response = vtmf.get('RESPONSE')
    order_route = order_message['ROUTE']

    strategy = Strategy.query.filter(Strategy.route == order_route).first()
    # pop on the ExDestination/TargetSubID
    add_strategy_name = strategy.name
    order_message['TARGET_STRATEGY'] = add_strategy_name
    order_message['TIF'] = '0'
    required = strategy.required
    required_list = required.split(",")
    optional = strategy.optional
    optional_list = optional.split(",")

    required_portion = {}
    optional_portion = {}
    # dict(required[i:i+2] for i in range(0, len(required),2))
    for req in required_list:
        map_req = Map.query.filter(Map.fix_tag == req).first()
        if map_req and map_req.vtmf_name and map_req.vtmf_name in order_message:
            req_vtmf_name = map_req.vtmf_name
            if order_message[req_vtmf_name]:
                required_portion[req] = order_message[req_vtmf_name]
            else:
                required_portion[req] = "EMPTY"
        else:
            print "Missing vtmf value for required FIX TAG", req, "FIX NAME", map_req.fix_name, "VTMF NAME", map_req.vtmf_name
            required_portion[req] = "MISSING"
    for opt in optional_list:
        map_opt = Map.query.filter(Map.fix_tag == opt).first()
        if map_opt and map_opt.vtmf_name and map_opt.vtmf_name in order_message:
            opt_vtmf_name = map_opt.vtmf_name
            if order_message[opt_vtmf_name]:
                optional_portion[opt] = order_message[opt_vtmf_name]
            else:
                print "Skipping because VTMF empty", opt_vtmf_name, "FIX TAG", map_opt.fix_tag, "FIX NAME", map_opt.fix_name
        else:
            print "Missing vtmf value for optional FIX_TAG", opt, "FIX NAME", map_opt.fix_name, "VTMF NAME", map_opt.vtmf_name
            #optional_portion[opt] = " "

    full_message = required_portion.copy()
    full_message.update(optional_portion)

    return full_message

    # get those vtmf tags out of this order_message

    # then get optional vtmf's based on strategy

    # get optionals values out of the order_message

    # now convert the whole list of vtmfs and values into fix tags and values and return that
    order_number = order_message['ORDERID']
    order_symbol = order_message['SYMBOL']
    order_qty = order_message['ORDQTY']

    return {fix_map.get('ORDERID','UNKNOWN'): order_number, fix_map.get('SYMBOL','UNKNOWN'): order_symbol, fix_map.get('ORDQTY','UNKNOWN'): order_qty}

def get_orders():
    return vtmf_list

def send_fix(fix):
    # expect {100:12345,55:VOD.L,756:10000}
    # pass the given tag to the fix section and return a result plus given fix into the list of orders

    order_id = int(max(vtmf_list.keys()).lstrip('Order')) + 1
    order_id = 'Order%i' % order_id
    order_number = fix['100']
    order_symbol = fix['55']
    order_qty = fix['756']
    vtmf_list[order_id] = {vtmf_map.get('100','UNKNOWN'): order_number, vtmf_map.get('55','UNKNOWN'): order_symbol,vtmf_map.get('756','UNKNOWN'): order_qty}
    return vtmf_list[order_id]



__author__ = '86286K'
"""
from requests import put, get

vtmf_from_csv = get('http://localhost:5000/process').json()

fix_from_csv = {}
fix_sent = {}
response = {}
#
if vtmf_from_csv:
    fix_from_csv = put('http://localhost:5000/process', data={'data': vtmf_from_csv).json()

if fix_from_csv:
    fix_sent = put('http://localhost:5000/orders', data={'data': fix_from_csv).json()

if fix_sent:
    response = get('http://localhost:5000/orders').json()

"""