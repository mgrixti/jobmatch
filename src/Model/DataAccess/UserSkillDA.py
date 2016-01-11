__author__ = 'Matthew Grixti'

from sqlalchemy import Column, Integer, ForeignKey, BOOLEAN
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from src.Model.DataAccess.DbConnection import DbConnection
from src.Model.DataAccess.UserDA import UserDA
from src.Model.DataAccess.SkillDA import SkillDA

Base = declarative_base()

class UserSkillDA(Base):
    __tablename__ = 'user_skill'

    user_skill_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(UserDA.user_id))
    skill_id = Column(Integer, ForeignKey(SkillDA.skill_id))
    is_top_skill = Column(BOOLEAN)

    user = relationship(UserDA)
    skills = relationship(SkillDA)

    def __init__(self):
        UserSkillDA.db = DbConnection()
        UserSkillDA.session = UserSkillDA.db.connect()

    def GetAll(self):

        # SELECT * FROM user_skill
        results = UserSkillDA.session.query(UserSkillDA)
        return results

    def GetByID(self, id):

        results = UserSkillDA.session.query(UserSkillDA).filter(UserSkillDA.user_skill_id == id).one()
        return results

    def GetAllForUser(self, user_id):

        results = UserSkillDA.session.query(UserSkillDA.skill_id, SkillDA.skill_name).join(SkillDA).\
                  filter(UserSkillDA.user_id == user_id).all()

        return results

    def GetTopForUser(self, id):

        results = UserSkillDA.session.query(UserSkillDA).filter(UserSkillDA.user_id == id,  UserSkillDA.is_top_skill == 1).all()

        return results