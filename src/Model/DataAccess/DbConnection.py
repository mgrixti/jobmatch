__author__ = 'Matthew Grixti'

from sqlalchemy import *
from sqlalchemy.orm import *

class DbConnection():

    # Establish connection to Database
    def connect(self):
        #Create db engine. Pass in connection string.
        engine = create_engine('mysql+mysqlconnector://jobmatch:Pennyworth2@mysql.mattgrixti.com/jobmatch', echo=False)
        Session = sessionmaker(bind=engine)
        return Session()
