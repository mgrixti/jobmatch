__author__ = 'Matthew Grixti'

from src.Model.AbstractModel import AbstractModel
from src.Model.SkillCollection import SkillCollection


class JobPost(AbstractModel):

    title = None
    description = None
    skills = None


    def get_postID(self):
        return self.id

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def getSkills(self):
        # if None get skills from DB
        if self.skills == None:
            self.skills = SkillCollection()
            self.skills.fetchAllForUser(self.id)

        return self.skills

    def populateFields(self, data):
        self.id = data.job_id
        self.first_name = data.job_title.decode("utf-8")
        self.last_name = data.job_description.decode("utf-8")