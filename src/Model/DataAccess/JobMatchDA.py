from sqlalchemy import Column, Integer, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from src.Model.DataAccess.DbConnection import DbConnection


Base = declarative_base()

class JobMatchDA(Base):
    __tablename__ = 'job_match'

    match_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    job_id = Column(Integer)
    score = Column(DECIMAL(12,10))

    def __init__(self, user_id=0, job_id=0, score=0):
        JobMatchDA.db = DbConnection()
        JobMatchDA.session = JobMatchDA.db.connect()

        if user_id != 0:
            self.user_id = user_id
            self.job_id = job_id
            self.score = score

    def GetAll(self):
        results = JobMatchDA.session.query(JobMatchDA).all()
        return results

    def GetAllForUser(self, id):
        results = JobMatchDA.session.query(JobMatchDA).filter(JobMatchDA.user_id == id).all()

        return results

    def GetAllForJob(self, id):
        results = JobMatchDA.session.query(JobMatchDA).filter(JobMatchDA.job_id == id).all()

        return results

    def insertMatch(self, user_id, job_id, score):
        new_match = JobMatchDA(user_id, job_id, score)
        JobMatchDA.session.add(new_match)
        JobMatchDA.session.commit()

    def GetMatch(self, user_id, job_id):
        results = JobMatchDA.session.query(JobMatchDA).filter(JobMatchDA.job_id == job_id, JobMatchDA.user_id == user_id)
        return results.all()

    def updateScore(self, user_id, job_id, score):
        result = self.session.query(JobMatchDA).filter(JobMatchDA.job_id == job_id, JobMatchDA.user_id == user_id).one()
        result.score = score
        self.session.add(result)
        self.session.commit()