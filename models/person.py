from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from models.family import Family
Base = declarative_base()


class Person(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)

    family_id = Column(Integer, ForeignKey('families.id'))
    family = relationship(Family, backref=backref('members', uselist=True, cascade='delete,all'))