__author__ = 'Matthew Grixti'

from src.Model.AbstractCollection import AbstractCollection
from src.Model.DataAccess.JobSkillDA import JobSkillDA
from src.Model.DataAccess.JobDA import JobDA
from src.Model.JobPost import JobPost


class JobCollection(AbstractCollection):

    jobDA = JobDA()
    jobSkillDA = JobSkillDA()


    def fetchAll(self):
        data = self.jobDA.GetAll()
        self.populateJobs(data)

    def fetchByID(self, id):
        data = self.jobDA.GetByID(id)
        self.populateJobs(data)

    def fetchAllForJob(self, id):
        data = self.jobSkillDA.GetAllSkillsForJob(id)
        self.populateJobs(data)

    def populateJobs(self, data):

        for row in data:
            job = JobPost()
            job.populateFields(row)
            self.addToCollection(job)