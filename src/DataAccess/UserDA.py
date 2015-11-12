__author__ = 'Matthew Grixti'

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from src.DataAccess.DbConnection import DbConnection


Base = declarative_base()


#UserDA is a mapped class used to access the UserDA table
class UserDA(Base):

    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    def __repr__(self):
        return "{User(first_name='%s', last_name='%s')}" % (self.first_name.decode("utf-8"), self.last_name.decode("utf-8"))

    def __init__(self):
        UserDA.db = DbConnection()
        UserDA.session = UserDA.db.connect()

    def GetAll(self):

        # SELECT * FROM user
        results = UserDA.session.query(UserDA)
        return results


    def GetByID(self, id):

        # SELECT * FROM user WHERE id =
        results = UserDA.session.query(UserDA).filter(UserDA.user_id == id).one()
        return results
