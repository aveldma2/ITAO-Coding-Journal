from model.base import *
from model.family import Family

class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)

    family_id = Column(Integer, ForeignKey('families.id'))
    family = relationship(Family, backref=backref('members', uselist=True, cascade='delete,all'))