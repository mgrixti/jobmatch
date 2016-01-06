__author__ = 'Matthew Grixti'

from src.Model.AbstractModel import AbstractModel



class Skill(AbstractModel):


    skill_name = None
    isTop = None

    # Returns the name of the skill.
    def get_skill_name(self):
        return self.skill_name

    def populateFields(self, data, isTop=False):

        self.id = data.skill_id

        if isTop:
            self.isTop = data.is_top_skill
        else:
            self.skill_name = data.skill_name.decode("utf-8")