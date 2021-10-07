from model.base import *

class Family(Base):
    __tablename__="families"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"The {self.name} Family"