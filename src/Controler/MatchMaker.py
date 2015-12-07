from src.Model.JobPost import JobPost
from src.Model.AHP import AHP


class MatchMaker:

    def GenerateJobMatches(self, job_list):

        # For each skill a user has, see if a job has any of those skills. Each skill match = 1
        for user_skill in user_skills:

            for job in job_list:

                job_rank = 0

                for job_skill in job.getSkills():

                    if job_skill.get_skill_id() == user_skill.get_skill_id():
                        job_rank+= 1


    def rankJob(self, user, job):

        # Compare user top_skills to job skills. If job has skill add that skills weight to users rank
        return None

