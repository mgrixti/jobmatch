__author__ = 'Matthew'

class User:

    userID = None
    first_name = None
    last_name = None
    skills = []

    # Constructor
    # Assigns instant variables their user specific values
    def __init__(self, user_id, first_name, last_name,skills):
        User.userID = user_id
        User.first_name = first_name
        User.last_name = last_name
        User.skills = skills

    # Returns userID of user
    def get_userid(self):
        return User.userID

    # Returns first name of user
    def get_first_name(self):
        return User.first_name

    # Returns last name of user
    def get_last_name(self):
        return User.last_name

    # Returns array of users skills
    def get_skills(self):
        return User.skills

    # Adds new skill to end of list
    # TODO Check for if skill is in the list
    def add_skill(self, skill):
        User.skills.append(skill)
