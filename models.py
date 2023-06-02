from database import Base
import uuid
from sqlalchemy import Integer, String, ForeignKey, Column, BINARY

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True, nullable=False, )
    password = Column(String, index=True, nullable=False)