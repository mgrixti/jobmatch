__author__ = 'Matthew Grixti'

from src.Model.AbstractModel import AbstractModel
from src.Model.SkillCollection import SkillCollection


class User(AbstractModel):

    first_name = None
    last_name = None
    skills = None # Lazy loaded
    topSkillRatings = None # Lazy loaded

    # Returns first name of user
    def get_first_name(self):
        return self.first_name

    # Returns last name of user
    def get_last_name(self):
        return self.last_name

    # Returns array of users skills
    def get_skills(self):
        return self.skills

    # Getter for user's skill
    def getSkills(self):
        # if None get skills from DB
        if self.skills == None:
            self.skills = SkillCollection()
            self.skills.fetchAllForUser(self.id)

        return self.skills

    def populateFields(self, data):
        self.id = data.user_id
        self.first_name = data.first_name.decode("utf-8")
        self.last_name = data.last_name.decode("utf-8")

    # Adds new skill to end of list
    # TODO Check for if skill is in the list
    def add_skill(self, skill):
        User.skills.append(skill)

