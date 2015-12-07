__author__ = 'Matthew Grixti'

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from src.Model.DataAccess.DbConnection import DbConnection

Base = declarative_base()


#UserDA is a mapped class used to access the UserDA table
class JobDA(Base):

    __tablename__ = 'job_post'

    job_id = Column(Integer, primary_key=True)
    job_title = Column(String)
    job_description = Column(String)

    def __repr__(self):
        return "{Job(job_title=='%s', job_description='%s')}" % (self.job_title.decode("utf-8"), self.job_description.decode("utf-8"))

    def __init__(self):
        JobDA.db = DbConnection()
        JobDA.session = JobDA.db.connect()

    def GetAll(self):

        # SELECT * FROM job_post
        results = JobDA.session.query(JobDA)
        return results


    def GetByID(self, id):

        # SELECT * FROM Job_postWHERE id =
        results = JobDA.session.query(JobDA).filter(JobDA.job_id == id).one()
        return results
