__author__ = 'Matthew'

class Skill:

    skill_id = None;
    skill_name = None

    # Constructor
    def __init__(self, skill_id, skill_name):
        Skill.skill_id = skill_id
        Skill.skill_name = skill_name

    # Returns the id of the skill.
    def get_skill_id(self):
        return Skill.skill_id

    # Returns the name of the skill.
    def get_skill_name(self):
        return Skill.skill_name
