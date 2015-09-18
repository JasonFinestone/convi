import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database/convi.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'database/db_repository')

SECRET_KEY = '24KJSF98325KJLSDF972saf29832LFjasfineZKFJL78f7ds98FSDKLF'

LOG_DIR = os.path.join(basedir, 'log')
LOG_FILE = os.path.join(LOG_DIR, 'convi.log')

CSV_IN_DIR = os.path.join(basedir, 'input')
CSV_OUT_DIR = os.path.join(basedir, 'output')

__author__ = '86286K'

