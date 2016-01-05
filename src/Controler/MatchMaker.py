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

            self.matchToUser(user, jobs)

    # Run the job list against a single user
    def matchToUser(self, user, jobList):
        topSkills = user.getTopSkills()
        ratingCollection = user.getSkillRatings()

        ratings = []

        for rating in ratingCollection.collection:
            ratings.append(rating.get_rating())


        weights = None

        # If there are 10 ratings
        if ratings.__len__() == 10:
            ahp = AHP()
            weights = ahp.generateWeightsFromRatings(ratings)

        else:
            print("Invalid number of ratings for: ", user.first_name, user.last_name, ", has ", ratings.__len__())


    # Returns True or False if job has skill with the same ID
    def hasJobSkill(self, job, skill_id):

        skills = job.getSkills()
        hasSkill = skills.contains(skill_id)

        return hasSkill


matcher = MatchMaker()
matcher.MatchAll()
