__author__ = 'Matthew Grixti'

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from src.DataAccess.DbConnection import DbConnection
from src.DataAccess.JobDA import JobDA
from src.DataAccess.SkillDA import SkillDA


Base = declarative_base()

class JobSkillDA(Base):
    __tablename__ = 'job_skill'

    job_skill_id = Column(Integer, primary_key=True)
    job_id = Column(Integer, ForeignKey(JobDA.job_id))
    skill_id = Column(Integer, ForeignKey(SkillDA.skill_id))

    job = relationship(JobDA)
    skills = relationship(SkillDA)


    def __init__(self):
        JobSkillDA.db = DbConnection()
        JobSkillDA.session = JobSkillDA.db.connect()

    def GetAll(self):

        # SELECT * FROM job_skill
        results = JobSkillDA.session.query(JobSkillDA)
        return results

    def GetByID(self, id):

        results = JobSkillDA.session.query(JobSkillDA).filter(JobSkillDA.job_skill_id == id).one()
        return results

    def GetAllSkillsForJob(self, job_id):

        results = JobSkillDA.session.query(JobSkillDA).join(JobDA).join(SkillDA).\
                  filter(JobSkillDA.job_id == job_id).all()

        return results


#list = JobSkillDA()
#skills = list.GetByID(2)
#for skill in skills:
  # print(skill.job.job_id, skill.job.job_title.decode(), skill.skills.skill_name.decode())
#print (skills)