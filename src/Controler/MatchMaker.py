from src.Model.JobPost import JobPost


class MatchMaker:

    def GenerateJobMatches(self, user_skills, job_list):

        # For each skill a user has, see if a job has any of those skills. Each skill match = 1
        for user_skill in user_skills:

            for job in job_list:

                job_rank = 0

                for job_skill in job.getSkills():

                    if job_skill.get_skill_id() == user_skill.get_skill_id():
                        job_rank+= 1

