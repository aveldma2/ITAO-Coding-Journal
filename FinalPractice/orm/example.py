from sqlalchemy.orm import sessionmaker
session = sessionmaker()

from sqlalchemy import create_engine

engine = create_engine('sqlite:///family.sqlite')
session.configure(bind=engine)

from model.base import *
from model.family import Family
from model.person import Person

Base.metadata.create_all(engine)

ses = session()

f = Family()

f.name = input('What is family name')

ses.add(f)
ses.commit()

f.name