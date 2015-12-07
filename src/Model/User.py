__author__ = 'Matthew Grixti'

from src.Model.DataAccess.UserDA import UserDA


class User:

    id = None
    first_name = None
    last_name = None
    skills = []
    topSkillRatings = []

    # Returns id of user
    def get_id(self):
        return self.id

    # Returns first name of user
    def get_first_name(self):
        return self.first_name

    # Returns last name of user
    def get_last_name(self):
        return self.last_name

    # Returns array of users skills
    def get_skills(self):
        return self.skills

    def populateFields(self, data):
        self.id = data.user_id
        self.first_name = data.first_name.decode("utf-8")
        self.last_name = data.last_name.decode("utf-8")

    # Adds new skill to end of list
    # TODO Check for if skill is in the list
    def add_skill(self, skill):
        User.skills.append(skill)

