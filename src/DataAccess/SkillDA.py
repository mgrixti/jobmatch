__author__ = 'Matthew Grixti'

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from src.DataAccess.DbConnection import DbConnection


Base = declarative_base()


class SkillDA(Base):
    __tablename__ = 'skill'

    skill_id = Column(Integer, primary_key=True)
    skill_name = Column(String)

    def __init__(self):
        SkillDA.db = DbConnection()
        SkillDA.session = SkillDA.db.connect()

    def GetAll(self):

        # SELECT * FROM skill
        results = SkillDA.session.query(SkillDA)
        return results

    def GetByID(self, id):

        # SELECT * FROM skill WHERE id =
        results = SkillDA.session.query(SkillDA).filter(SkillDA.skill_id == id).one()
        return results