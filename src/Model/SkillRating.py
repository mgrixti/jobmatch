__author__ = 'Matthew Grixti'

from src.Model.AbstractModel import AbstractModel


class SkillRating(AbstractModel):

    skill_id_one = None
    skill_id_two = None
    rating = None
    user_id = None

     # Returns the id of the skill.
    def get_skill_id(self):
        return self.id

    # Returns the id of the skill.
    def get_skill_id_one(self):
        return self.skill_id_one

      # Returns the id of the skill.
    def get_skill_id_two(self):
        return self.skill_id_two

    def populateFields(self, data):

        self.id = data.skill_rating_id
        self.skill_id_one = data.skill_id_one
        self.skill_id_two = data.skill_id_two
        self.rating = data.rating
        self.user_id = data.user_id