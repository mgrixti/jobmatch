__author__ = 'Matthew'

class User:

    userID = None;
    skills = [];

    # Constructor
    def __init__(self, user_id, skills):
        User.userID = user_id;
        User.skills = skills;

    def get_userid(self):
        return User.userID;

    def get_skills(self):
        return User.skills;