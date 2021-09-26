from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Family(Base):
    __tablename__ = "families"
    id = Column(Integer, primary_key=True)
