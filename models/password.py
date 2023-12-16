from config.database import Base
from sqlalchemy import Column, Integer, String

class Password(Base):
    __tablename__ = "passwords"
    id_password = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer) # Foreign Key
    password = Column(String)