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

        print("Looking for matches for", user.first_name, user.last_name)

        topSkills = user.getTopSkills().collection
        ratingCollection = user.getSkillRatings().collection

        ratings = []

        # Extract the raw rating from SkillRating Object
        for rating in ratingCollection:
            ratings.append(rating.get_rating())

        # If there are 10 ratings
        if ratings.__len__() == 10:
            # Generate weights for users top skills
            ahp = AHP()
            weights = ahp.generateWeightsFromRatings(ratings)

            # Pull weights and associate them with their skill in a dict
            skillWeightings = {}
            for i in range(weights.__len__()):
                skillWeightings[topSkills[i].id] = weights[i]



        else:
            print("Invalid number of ratings for: ", user.first_name, user.last_name, ", has ", ratings.__len__())



    # Returns True or False if job has skill with the same ID
    def hasJobSkill(self, job, skill_id):

        skills = job.getSkills()
        hasSkill = skills.contains(skill_id)

        return hasSkill

matcher = MatchMaker()
matcher.MatchAll()