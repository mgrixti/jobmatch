__author__ = 'Matthew'

class JobPost:

    postID = None
    title = None
    description = None
    skills = []

    # Constructor
    def __init__(self, job_id, job_title, description, skills):
        JobPost.postID = job_id
        JobPost.Title = job_title
        JobPost.description = description
        JobPost.skills = skills

    def get_postID(self):
        return JobPost.postID

    def get_title(self):
        return JobPost.title

    def get_description(self):
        return JobPost.description

    def get_skills(self):
        return JobPost.skills