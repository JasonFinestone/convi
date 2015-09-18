from convi.config import CSV_IN_DIR, CSV_OUT_DIR
from convi.database import db_session
from convi.models import Strategy, Order, Fix, Vtmf, Map
from os import listdir, rename, path
import csv

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
                bfile = str(afile) + '.bkp'
                move_path = path.join(CSV_OUT_DIR, bfile)
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

                    #if len(find_csv_filenames(CSV_IN_DIR)) > 0:
                    #    break


def put_vtmf(vtmf):
    """
    return fix for vtmf
    split order and response
    get route from order
    convert the entire vtm into fix equiv
    use the required and optional from strategy to identify which tags to keep.
    shorten the message, based on route, to only include those.
    pass the fix message back to frontend
    """
    order_message = vtmf
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


answer = get_vtmf()
if answer:
    #print 'Sent:', answer['NEW_ORDER']
    #print 'Received:', answer['RESPONSE']

    answer_message = answer['NEW_ORDER']
    print answer_message
    second_answer = put_vtmf(answer_message)

    print second_answer





__author__ = '86286K'
