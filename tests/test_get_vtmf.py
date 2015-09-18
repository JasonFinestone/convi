from convi.config import CSV_IN_DIR, CSV_OUT_DIR
from convi.database import db_session
from convi.models import Strategy, Order, Fix, Vtmf
from os import listdir, rename, path
import csv

#basedir = path.abspath(path.dirname(__file__))
#CSV_IN_DIR = path.join(basedir, '../convi/input')
#CSV_OUT_DIR = path.join(basedir, '../convi/output')
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(basedir, '../convi/database/convi.db')

#engine = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True)
#db_session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

#Base = declarative_base()
#Base.query = db_session.query_property()


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
    # fix_map = {'ORDERID': 100, 'SYMBOL': 55, 'ORDQTY': 756}
    # for order in vtmf:
    order_message = vtmf
    #order_response = vtmf.get('RESPONSE')
    # get route
    print order_message
    #print order_message['ROUTE']
    #order_route = order_message['ROUTE']

    ### convert to fix tags
    # create a fix map {VTMF_NAME:FIX_TAG}
    fix_map = db_session.query(Fix).options(joinedload('vtmf')).all()

    return fix_map


    strategy = models.Strategy.query.filter_by(route=order_route).first()
    required = strategy.required
    optional = strategy.optional
    required_portion = {}
    optional_portion = {}
    # dict(required[i:i+2] for i in range(0, len(required),2))
    for req in required:
        required_portion[req] = order_message[req]
    for opt in optional:
        optional_portion[opt] = order_message[opt]

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


answer = get_vtmf()
if answer:
    print 'Sent:', answer['NEW_ORDER']
    print 'Received:', answer['RESPONSE']

    answer_message = answer['NEW_ORDER']
    print answer_message
    second_answer = put_vtmf(answer_message)

    print second_answer





__author__ = '86286K'
