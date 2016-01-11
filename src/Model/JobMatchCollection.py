__author__ = 'Matthew Grixti'

from src.Model.AbstractCollection import AbstractCollection
from src.Model.DataAccess.JobMatchDA import JobMatchDA
from src.Model.JobMatch import JobMatch


class JobMatchCollection(AbstractCollection):

    jobMatchDA = JobMatchDA()

    def fetchAll(self):
        data = self.jobMatchDA.GetAll()
        self.populateJobMatch(data)

    def fetchByID(self, id):
        data = self.jobMatchDA.GetByID(id)
        self.populateJobMatch(data)

    def fetchAllForUser(self, id):
        data = self.jobMatchDA.GetAllForUser(id)
        self.populateJobMatch(data)

    def fetchAllForJob(self, id):
        data = self.jobMatchDA.GetAllForJob(id)
        self.populateJobMatch(data)

    def addMatch(self, user_id, job_id, score):
        match = JobMatch()
        match.user_id = user_id
        match.job_id = job_id
        match.score = score
        self.collection.append(match)
        self.jobMatchDA.insertMatch(user_id, job_id, score)

        return match

    def updateScore(self, jobMatch, score):
        jobMatch.updateScore(score)
        self.jobMatchDA.updateScore(jobMatch.user_id, jobMatch.job_id, score)

    def populateJobMatch(self, data):

        for row in data:
            job = JobMatch()
            job.populateFields(row)
            self.addToCollection(job)
