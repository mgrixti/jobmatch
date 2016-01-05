__author__ = 'Matthew Grixti'

from sqlalchemy import Column, Integer, ForeignKey, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from src.Model.DataAccess.DbConnection import DbConnection
from src.Model.DataAccess.UserDA import UserDA
from src.Model.DataAccess.SkillDA import SkillDA

Base = declarative_base()


class UserSkillRatingDA(Base):
    __tablename__ = 'skill_rating'

    skill_rating_id = Column(Integer, primary_key=True)
    skill_id_one = Column(Integer)
    skill_id_two = Column(Integer)
    rating = Column(DECIMAL(10,10))
    user_id = Column(Integer)

    def __init__(self):
        self.db = DbConnection()
        self.session = self.db.connect()

    def getAll(self):
        results = self.session.query(UserSkillRatingDA)
        return results

    def getAllForUser(self, id):
        results = self.session.query(UserSkillRatingDA).filter(UserSkillRatingDA.user_id == id)
        return results

    def getByID(self, id):
        results = self.session.query(UserSkillRatingDA).filter(UserSkillRatingDA.skill_rating_id == id).one()
        return results