__author__ = 'mgrixti'


from sqlalchemy import Column, Integer, String, VARCHAR
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

    def GetAll(self):
        db = DbConnection()
        session = db.connect()

        # SELECT * FROM user
        results = session.query(UserDA)

        return results
