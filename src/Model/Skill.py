__author__ = 'Matthew'

from src.Model.AbstractModel import AbstractModel

class Skill(AbstractModel):

    skill_name = None

    # Returns the id of the skill.
    def get_skill_id(self):
        return self.id

    # Returns the name of the skill.
    def get_skill_name(self):
        return self.skill_name

    def populateFields(self, data):
        self.id = data.skill_id
        self.first_name = data.first_name.decode("utf-8")
        self.last_name = data.last_name.decode("utf-8")