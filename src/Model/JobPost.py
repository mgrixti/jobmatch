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
            self.skills.fetchAllForJob(self.id)

        return self.skills

    def populateFields(self, data):
        self.id = data.job_id
        self.title = data.job_title.decode("utf-8")
        self.description = data.job_description.decode("utf-8")