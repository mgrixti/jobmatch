__author__ = 'Matthew Grixti'

from src.Controler.MatchMaker import MatchMaker
from src.Model.JobMatchCollection import JobMatchCollection

print("\n****Match Demo****\n")
print('1) Match All users against jobs.\n'
      '2) Match single user against all job.\n'
      '3) Match single job against all users.')
demoNum = input('Enter demo to run (1-3):')

matcher = MatchMaker()
jobmatches = JobMatchCollection()
if demoNum == '1':
    matcher.matchAll()
    jobmatches.fetchAll()
    for match in jobmatches.collection:
        print('User', match.user_id, 'matched to job:',match.job_id)
elif demoNum == '2':
    id = input('Enter userID:')
    matcher.matchSingleUserToJobs(id)

    jobmatches.fetchAllForUser(id)
    for match in jobmatches.collection:
        print('User', match.user_id, 'matched to job:',match.job_id)

elif demoNum == '3':
    id = input('Enter jobID:')
    matcher.matchSingleJobToUsers(id)

    jobmatches.fetchAllForJob(id)
    for match in jobmatches.collection:
        print('Job', match.job_id, 'matched to user ID:',match.user_id)
else:
    print('Invalid Input')