__author__ = 'Matthew Grixti'

from src.Model.AbstractModel import AbstractModel
from src.Model.DataAccess.JobMatchDA import JobMatchDA

class JobMatch(AbstractModel):

    user_id = None
    job_id = None
    score = None


    def getUserID(self):
        return self.user_id

    def getJobID(self):
        return self.job_id

    def updateScore(self, score):
        da = JobMatchDA()
        self.score = score

    def populateFields(self, data):
        self.id = data.match_id
        self.user_id = data.user_id
        self.job_id = data.job_id
        self.score = data.score