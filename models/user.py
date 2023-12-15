from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class User(Base):
    __tablename__ = "users"
    id_user = Column(Integer, primary_key=True, index=True)
    username = Column(String(50))
    password = Column(String(50))