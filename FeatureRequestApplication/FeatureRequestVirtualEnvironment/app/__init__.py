# Flask  is the prototype used to create instances of web application or web applications
from flask import Flask
# from sqlalchemy package we can import Column, String, Integer, Date,asc
from sqlalchemy import Column, String, Integer, Date, Sequence
# from sqlalchemy package we can import declarativ_base
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy package we can import sessionmaker
from sqlalchemy.orm import sessionmaker
# imports all exceptetions from sqlalchemy package
from sqlalchemy.exc import *
# imports Config class from config module
from config import Config
# once we import Flask, we need to create an instance of the Flask class for our web app.
# passing __name__ is going to configure Flask.
# __name__ is a special variable that gets as value the string "__main__" when you’re executing the script.
app = Flask(__name__)
# app a flask variable gets database configurations from config.py file
app.config.from_object(Config)

try:
    # A class FeatureRequestApp will be the class to which we map 'FeatureRequestApp' table and contains requeired columns from table as variable in class.
    class FeatureRequestApp(Config.base):
        # A class using Declarative  needs a __tablename__ attribute, and one Column which is a primary key 
        __tablename__ = 'FeatureRequestApp'
        featureId=Column('id', Integer, Sequence('feature_id_seq'), primary_key=True)
        title = Column(String(100),unique=True)
        description = Column(String(1000))
        client = Column(String(10)) 
        clientPriority = Column(Integer())
        targetDate = Column(Date())
        productArea = Column(String(10))
        # __init__ is a special method in Python classes, it is the constructor method for a class
        # __init__ is called when ever an object of the class is constructed.
        def __init__(self,title, description, client, clientPriority, targetDate, productArea):
            self.title = title
            self.description = description
            self.client = client
            self.clientPriority = clientPriority
            self.targetDate = targetDate
            self.productArea = productArea

    # The declarative_base() base class contains a MetaData object where newly defined Table objects are collected.  
    # This object is to be accessed  for MetaData-specific operations.Such as, to issue CREATE statements for all tables.
    Config.base.metadata.create_all(Config.db)

    # importing routes.py, featureRequestManager, featureRequestService
    from app import routes, featureRequestManager
    from app import featureRequestService


except ArgumentError as ae:
    print('missing connection string or primary key', ae)

except UnboundExecutionError as ue:
    print('SQL was attempted without a database connection to execute it on', ue)

except IndexError as ie:
    print('missing table name', ie)

except TypeError as te:
    print('check params', te)

except TimeoutError as te:
    print('Connection TimedOut', te)

except Exception as e:
    print('Exception occured in init',e)


if __name__ == "__main__":
    app.run()




