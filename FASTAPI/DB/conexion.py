import os 
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

dbName = 'usuarios.sqlite'
basedir = os.path.abspath(os.path.dirname(__file__))
dbUrl = f"sqlite:///{os.path.join(basedir, dbName)}"

engine = create_engine(dbUrl, echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()
