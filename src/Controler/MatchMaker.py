from src.Model.AHP import AHP
from src.Model.UserCollection import UserCollection
from src.Model.JobCollection import JobCollection
from src.Model.JobMatchCollection import JobMatchCollection
from src.Model.DataAccess.JobMatchDA import JobMatchDA
import math



class MatchMaker:

    # Runs all users against all jobs
    def matchAll(self):

        # Gets all jobs
        jobCollection = JobCollection()
        jobCollection.fetchAll()
        jobs = jobCollection.collection

        # Gets all users
        userCollection = UserCollection()
        userCollection.fetchAll()
        users = userCollection.collection

        # Runs each user against the list of jobs.
        for user in users:

            self.matchToUser(user, jobs)

    def matchSingleUserToJobs(self, userID):

        jobCollection = JobCollection()
        jobCollection.fetchAll()
        jobs = jobCollection.collection


        userCollection = UserCollection()
        userCollection.fetchByID(userID)
        userCol = userCollection.collection

        if userCol.__len__() > 0:
            user = userCol.pop(0)
            self.matchToUser(user, jobs)
        else:
            print("No user with the ID", userID)

    def matchSingleJobToUsers(self,jobID):

        jobCollection = JobCollection()
        jobCollection.fetchByID(jobID)
        jobs = jobCollection.collection

        userCollection = UserCollection()
        userCollection.fetchAll()
        users = userCollection.collection

        for user in users:

            self.matchToUser(user, jobs)

    # Run the job list against a single user
    def matchToUser(self, user, jobList):

        print("\nLooking for matches for", user.first_name, user.last_name)

        topSkills = user.getTopSkills().collection
        ratingCollection = user.getSkillRatings().collection

        ratings = []

        # Extract the raw rating from SkillRating Object
        for rating in ratingCollection:
            ratings.append(rating.get_rating())

        # If there are 10 ratings
        if ratings.__len__() == self.requiredRatings(topSkills.__len__()):
            # Generate weights for users top skills
            ahp = AHP(topSkills.__len__())
            weights = ahp.generateWeightsFromRatings(ratings)

            # Pull weights and associate them with their skill in a dict
            skillWeightings = {}
            for i in range(weights.__len__()):
                skillWeightings[topSkills[i].id] = weights[i]


            matches = JobMatchCollection() # Matches found
            for job in jobList: # Run each job

                score = 0
                for skill in skillWeightings.keys():
                    if self.hasJobSkill(job, skill):
                        score+= skillWeightings[skill]

                print("\t\tJob",job.id, "has score of: ", score)

                # Get match from databases
                matchExist = self.matchExist(user.id, job.id)

                if score > 0 and matchExist == None: # Score is > 0 and match is not already in DB
                    print("\t\t\tMatch does not exist. Adding...")
                    matches.addMatch(user.id, job.id, score)

                elif matchExist != None and round(score,10) != matchExist.score:
                    print("\t\t\tMatch exists but score don't match. Updating Score....")
                    matchExist.updateScore(user.id, job.id, score)

            print("\t****",user.first_name, user.last_name, "has been matched with", matches.collection.__len__(), "new jobs.")
        else:
            print("\tNo skills or an invalid number of ratings. ", user.first_name, user.last_name, " has ", ratings.__len__(), 'but needs', self.requiredRatings(topSkills.__len__()), "ratings and is unable to finds matches")


    # Returns True or False if job has skill with the same ID
    def hasJobSkill(self, job, skill_id):
        skills = job.getSkills()
        hasSkill = skills.contains(skill_id)

        return hasSkill

    # Calculates the number of ratings required for AHP based on the number of skills chosen
    def requiredRatings(self, numSkills):
        ratings = (math.pow(numSkills, 2) - numSkills)/2
        return ratings

    def matchExist(self, user_id, job_id):
        da = JobMatchDA()
        match = da.GetMatch(user_id, job_id)

        if match.__len__() > 0:
            return  match[0]
        else:
            return None