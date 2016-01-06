__author__ = 'Matthew Grixti'

from src.Model.AbstractCollection import AbstractCollection
from src.Model.DataAccess.SkillDA import SkillDA
from src.Model.DataAccess.JobSkillDA import JobSkillDA
from src.Model.DataAccess.UserSkillDA import UserSkillDA
from src.Model.Skill import Skill

# All fetch methods are for database retrieval
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

    def fetchTopForUser(self, id):
        data = self.userSkillDA.GetTopForUser(id)
        self.populateSkills(data, True)

    def fetchAllForJob(self, id):
        data = self.jobSkillDA.GetAllSkillsForJob(id)
        self.populateSkills(data)

    def populateSkills(self, data, isTop=False):

        # if data != None:

            for row in data:
                skill = Skill()

                if isTop:
                    skill.populateFields(row, True)
                else:
                    skill.populateFields(row)

                self.addToCollection(skill)
        # else:
        #     print("Error: No skills to Populate")
