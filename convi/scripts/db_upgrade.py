__author__ = '86286K'
#!flask/bin/python
from migrate.versioning import api
from convi.config import SQLALCHEMY_DATABASE_URI
from convi.config import SQLALCHEMY_MIGRATE_REPO
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print('Current database version: ' + str(v))