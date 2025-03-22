from DB.conexion import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'tb_users'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String)
    email = Column(String)
    age = Column(Integer)
    
    