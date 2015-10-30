__author__ = 'Matthew'

class JobPost:

    postID = None
    description = None
    skills = []

    # Constructor
    def __init__(self, user_id, description, skills):
        JobPost.postID = user_id
        JobPost.description = description
        JobPost.skills = skills

    def get_postid(self):
        return JobPost.postID

    def get_description(self):
        return JobPost.description

    def get_skills(self):
        return JobPost.skills