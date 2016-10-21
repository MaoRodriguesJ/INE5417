from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

engine = create_engine('sqlite:///sqlalchemy.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
Session = DBSession()

#Base.metadata.create_all(engine)