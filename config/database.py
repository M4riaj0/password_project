import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sql_file_name = "../database.sqlite"
base_dir = os.path.dirname(os.path.abspath(__file__))
database_url = "sqlite:///" + os.path.join(base_dir, sql_file_name)

engine = create_engine(database_url, echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()