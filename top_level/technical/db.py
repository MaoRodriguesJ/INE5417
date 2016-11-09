from top_level.technical.singleton import Singleton

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

Engine = create_engine('sqlite:///sqlalchemy.db')
Base.metadata.bind = Engine
DBSession = sessionmaker(bind=Engine)
Session = DBSession()

class DataBase:

    def create():   
        Base.metadata.create_all(Engine)
    
    def clear():
        for table in reversed(Base.metadata.sorted_tables):
            print ('Clear table: {}'.format(table))
            Session.execute(table.delete())
        Session.commit()
    
    def add(obj):
        Session.add(obj)
        Session.commit()
    
    def search_all(obj):
        return Session.query(obj.__class__).all()

    def search_one(obj, _id):
        return Session.query(obj.__class__).filter(obj.__class__._id == _id).\
               scalar()

class DB(DataBase, metaclass=Singleton):
    pass
