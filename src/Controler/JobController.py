from src.Model.User import User
from src.DataAccess.JobDA import JobDA
from src.DataAccess.JobSkillDA import JobSkillDA

class JobPostController():


    def BuildSingleJob(self, id):
        jobDA = JobDA()
        jobSkillDA = JobSkillDA()

        jobData = jobDA.GetByID(id)
        jobSkills = jobSkillDA.GetAllSkillsForJob(id)
        job = JobPostController.BuildJobObject(self, jobData, jobSkills)

        return job

    def BuildJobObject(self, jobData, jobSkills):

        job_id = jobData.user_id
        job_title = jobData.job_title.decode()
        job_description = jobData.job_desription.decode()
        skills = []

        for skill in jobSkills:
            skills.append(skill.skill_id)

        return User(job_id, job_title, job_description, skills)