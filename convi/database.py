from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database/convi.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'database/db_repository')

# remove echo=True when going to production (used to see db queries during dev)
#engine = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True, echo=True)
engine = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True)
db_session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import convi.models
    Base.metadata.create_all(bind=engine)



__author__ = '86286K'
