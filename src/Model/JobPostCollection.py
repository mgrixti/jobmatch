__author__ = 'Matthew Grixti'

from src.Model.AbstractCollection import AbstractCollection
from src.Model.DataAccess.JobSkillDA import JobSkillDA
from src.Model.DataAccess.JobDA import JobDA
from src.Model.Skill import Skill


class JobPostCollection(AbstractCollection):

    jobDA = JobDA()
    jobSkillDA = JobSkillDA()


    def fetchAll(self):
        data = self.jobDA.GetAll()
        self.populateSkills(data)

    def fetchByID(self, id):
        data = self.jobDA.GetByID(id)
        self.populateSkills(data)

    def fetchAllForJob(self, id):
        data = self.jobSkillDA.GetAllSkillsForJob(id)
        self.populateSkills(data)

    def populateSkills(self, data):

        for row in data:
            skill = Skill()
            skill.populateFields(row)
            self.addToCollection(skill)