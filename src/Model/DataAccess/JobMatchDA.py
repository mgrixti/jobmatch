from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from src.Model.DataAccess.DbConnection import DbConnection


Base = declarative_base()

class JobMatchDA(Base):
    __tablename__ = 'job_match'

    match_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    job_id = Column(Integer)

    def __init__(self, user_id=0, job_id=0):
        JobMatchDA.db = DbConnection()
        JobMatchDA.session = JobMatchDA.db.connect()

        if user_id != 0:
            self.user_id = user_id
            self.job_id = job_id

    def GetAll(self):
        results = JobMatchDA.session.query(JobMatchDA)
        return results

    def GetAllForUser(self, id):
        results = JobMatchDA.session.query(JobMatchDA).filter(JobMatchDA.user_id == id)

        return results

    def GetAllForJob(self, id):
        results = JobMatchDA.session.query(JobMatchDA).filter(JobMatchDA.job_id == id)

        return results

    def insertMatch(self, user_id, job_id):
        new_match = JobMatchDA(user_id, job_id)
        JobMatchDA.session.add(new_match)
        results = JobMatchDA.session.commit()

da = JobMatchDA()
da.insertMatch(5,7)