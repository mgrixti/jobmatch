__author__ = 'Matthew Grixti'

from sqlalchemy import Column, Integer, ForeignKey
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

        results = UserSkillDA.session.query(UserSkillDA).join(UserDA).join(SkillDA).\
                  filter(UserSkillDA.user_id == user_id).all()

        return results


#list = UserSkillDA()
#skills = list.GetAllForUser(3)
#for skill in skills:
 #   print(skill.user.id, skill.user.first_name.decode(), skill.skills.skill_name.decode())