__author__ = 'Matthew Grixti'

from src.Model.AbstractCollection import AbstractCollection
from src.Model.DataAccess.JobMatchDA import JobMatchDA
from src.Model.JobPost import JobPost


class JobMatchCollection(AbstractCollection):

    jobMatchDA = JobMatchDA()

    def fetchAll(self):
        data = self.jobMatchDA.GetAll()
        self.populateJobs(data)

    def fetchByID(self, id):
        data = self.jobMatchDA.GetByID(id)
        self.populateJobs(data)

    def fetchAllForUser(self, id):
        data = self.jobMatchDA.GetAllForUser(id)
        self.populateJobs(data)

    def addMatch(self, user_id, job):
        self.collection.append(job)
        self.jobMatchDA.insertMatch(user_id, job.id)

    def populateJobs(self, data):

        for row in data:
            job = JobPost()
            job.populateFields(row)
            self.addToCollection(job)
