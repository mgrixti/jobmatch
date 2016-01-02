__author__ = 'Matthew Grixti'

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from src.Model.DataAccess.DbConnection import DbConnection

Base = declarative_base()


#UserDA is a mapped class used to access the UserDA table
class UserDA(Base):

    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    first_name = Column(String(20))
    last_name = Column(String(20))


    def __repr__(self):
        return "{'user_id':'%s', 'first_name': '%s', 'last_name': '%s'}" % (self.user_id, self.first_name.decode("utf-8"), self.last_name.decode("utf-8"))

    def __init__(self):
        self.db = DbConnection()
        self.session = self.db.connect()

    def GetAll(self):

        # SELECT * FROM user
        results = self.session.query(UserDA)

        return results


    def GetByID(self, id):

        # SELECT * FROM user WHERE id =
        results = self.session.query(UserDA).filter(UserDA.user_id == id).one()

        return results

