from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from convi.database import Base

class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    original_orderId = Column(Integer)
    original_message = Column(String(1024))
    original_response = Column(String(1024))
    original_datetime = Column(DateTime)
    new_orderId = Column(Integer)
    new_message = Column(String(1024))
    new_response = Column(String(1024))
    new_datetime = Column(DateTime)

    def __repr__(self):
        return '<Order %r>' % (self.original_orderId)


class Fix(Base):
    __tablename__ = 'fix'
    id = Column(Integer, primary_key=True)
    fix_tag = Column(Integer, index=True, unique=True)
    fix_name = Column(String(64), index=True, unique=True)
    fix_type = Column(String(16))
    fix_notes = Column(String(1024))
    vtmf_id = Column(Integer, ForeignKey('vtmf.id'))

    def __repr__(self):
        return '<Fix %r>' % (self.fix_name)


class Vtmf(Base):
    __tablename__ = 'vtmf'
    id = Column(Integer, primary_key=True)
    vtmf_tag = Column(Integer, index=True, unique=True)
    vtmf_name = Column(String(64), index=True, unique=True)
    vtmf_type = Column(String(16))
    vtmf_notes = Column(String(1024))
    fix_id = Column(Integer, ForeignKey('fix.id'))

    def __repr__(self):
        return '<Vtmf %r>' % (self.vtmf_name)


class Strategy(Base):
    __tablename__ = 'strategy'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), index=True)
    route = Column(String(64), index=True, unique=True)
    required = Column(String(1024))
    optional = Column(String(1024))

class Map(Base):
    __tablename__ = 'map'
    id = Column(Integer, primary_key=True)
    fix_tag = Column(Integer, index=True, unique=True)
    fix_name = Column(String(64), index=True, unique=True)
    fix_type = Column(String(16))
    vtmf_tag = Column(Integer, index=True, unique=True)
    vtmf_name = Column(String(64), index=True, unique=True)
    vtmf_type = Column(String(16))
    notes = Column(String(1024))

    def __repr__(self):
        return '<Map %r>' % (self.fix_name)

__author__ = '86286K'