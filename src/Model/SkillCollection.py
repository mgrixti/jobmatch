__author__ = 'Matthew Grixti'

from src.Model.AbstractCollection import AbstractCollection
from src.Model.DataAccess.SkillDA import SkillDA
from src.Model.DataAccess.JobSkillDA import JobSkillDA
from src.Model.DataAccess.UserSkillDA import UserSkillDA
from src.Model.Skill import Skill

class SkillCollection(AbstractCollection):

    skillDA = SkillDA()
    userSkillDA = UserSkillDA()
    jobSkillDA = JobSkillDA()

    def fetchAll(self):
        data = self.skillDA.GetAll()
        self.populateSkills(data)

    def fetchByID(self, id):
        data = self.skillDA.GetByID(id)
        self.populateSkills(data)

    def fetchAllForUser(self, id):
        data = self.userSkillDA.GetAllForUser(id)
        self.populateSkills(data)

    def fetchAllForJob(self, id):
        data = self.jobSkillDA.GetAllSkillsForJob(id)
        self.populateSkills(data)

    def populateSkills(self, data):

        for row in data:
            skill = Skill()
            skill.populateFields(row)
            self.addToCollection(skill)