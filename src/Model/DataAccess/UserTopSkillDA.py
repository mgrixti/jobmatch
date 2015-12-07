__author__ = 'Matthew Grixti'

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from src.Model.DataAccess.DbConnection import DbConnection
from src.Model.DataAccess.UserDA import UserDA
from src.Model.DataAccess.SkillDA import SkillDA

Base = declarative_base()


class UserTopSkillDA(Base):
    __tablename__ = 'user_skill'

    top_skill_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(UserDA.user_id))
    skill_id = Column(Integer, ForeignKey(SkillDA.skill_id))

    def __init__(self):
        self.db = DbConnection()
        self.session = self.db.connect()

    def getAllForUser(self, id):
        results = self.session.query(UserTopSkillDA).filter(UserTopSkillDA.user_id == id).one()
        return results

    def getByID(self, id):
        results = self.session.query(UserTopSkillDA).filter(UserTopSkillDA.top_skill_id == id).one()
        return results