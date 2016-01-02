from src.Model.JobPost import JobPost
from src.Model.AHP import AHP
from src.Model.UserCollection import UserCollection
from src.Model.JobCollection import JobCollection


class MatchMaker:

    def MatchAll(self):

        jobCollection = JobCollection()
        jobCollection.fetchAll()
        jobs = jobCollection.collection

        userCollection = UserCollection()
        userCollection.fetchAll()
        users = userCollection.collection


        for user in users:
            ratings = user.getSkillRatings()



    # def GenerateJobMatches(self, job_list):
    #
    #     # For each skill a user has, see if a job has any of those skills. Each skill match = 1
    #     for user_skill in user_skills:
    #
    #         for job in job_list:
    #
    #             job_rank = 0
    #
    #             for job_skill in job.getSkills():
    #
    #                 if job_skill.get_skill_id() == user_skill.get_skill_id():
    #                     job_rank+= 1
    #
    #
    # def rankJob(self, user, job):
    #
    #     # Compare user top_skills to job skills. If job has skill add that skills weight to users rank
    #     return None


matcher = MatchMaker()
matcher.MatchAll()
