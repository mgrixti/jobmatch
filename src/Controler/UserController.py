from src.Model.User import User
from src.DataAccess.UserDA import UserDA
from src.DataAccess.UserSkillDA import UserSkillDA

class UserController():


    def BuildSingleUser(self, id):
        userDA = UserDA()
        userSkillDA = UserSkillDA()

        userData = userDA.GetByID(id)
        userSkills = userSkillDA.GetAllForUser(id)
        user = UserController.BuildUserObject(self,userData, userSkills)

        return user

    def BuildUserObject(self, userData, userSkills):

        user_id = userData.user_id
        first_name = userData.first_name.decode()
        last_name = userData.last_name.decode()
        skills = []

        for skill in userSkills:
            skills.append(skill.skill_id)

        return User(user_id, first_name, last_name, skills)