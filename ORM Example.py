from sqlalchemy.orm import sessionmaker
session = sessionmaker()

from sqlalchemy import create_engine

engine = create_engine('sqlite:////family.sqlite')
session.configure(bind=engine)

from models.family import Family
from models.person import Person

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

Base.metadata.create_all(engine)

ses = session()

f = Family()
f.name = input('What is your family name')

if f.name != '':

    mem_count = int(input('how many'))

    for i in range(mem_count):
        n = input('name:')
        member = Person(first_name=n, family = f)

    ses.add(f)
    ses.commit()

families = ses.query(Family).all()
for f in families:
    print(family)
    for m in f.members:
      print(m)