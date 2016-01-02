__author__ = 'Matthew Grixti'

from src.Model.AbstractCollection import AbstractCollection
from src.Model.DataAccess.UserSkillRatingDA import UserSkillRatingDA
from src.Model.DataAccess.JobSkillDA import JobSkillDA
from src.Model.DataAccess.UserSkillDA import UserSkillDA
from src.Model.DataAccess.UserTopSkillDA import UserTopSkillDA

from src.Model.Skill import Skill


class SkillRatingCollection(AbstractCollection):


    userSkillRatingDA = UserSkillRatingDA()
    userSkillDA = UserSkillDA()
    userTopSkillDA = UserTopSkillDA()
    jobSkillDA = JobSkillDA()

    def fetchAll(self):
        data = self.userSkillRatingDA.GetAll()
        self.populateSkillRatings(data)

    def fetchByID(self, id):
        data = self.userSkillRatingDA.getByID(id)
        self.populateSkillRatings(data)

    def fetchAllForUser(self, id):
        data = self.userSkillRatingDA.getAllForUser(id)
        self.populateSkillRatings(data)

    def populateSkillRatings(self, data):

        for row in data:
            skillRating = Skill()
            skillRating.populateFields(row)
            self.addToCollection(skillRating)