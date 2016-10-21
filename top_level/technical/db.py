from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

Engine = create_engine('sqlite:///sqlalchemy.db')
Base.metadata.bind = Engine
DBSession = sessionmaker(bind=Engine)
Session = DBSession()
