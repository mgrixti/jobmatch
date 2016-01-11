__author__ = 'Matthew Grixti'


from src.Model.AbstractCollection import AbstractCollection
from src.Model.DataAccess.UserDA import UserDA
from src.Model.User import User


class UserCollection(AbstractCollection):

    userDA = UserDA()

    def fetchAll(self):
        data = self.userDA.GetAll()
        self.populateUsers(data)

    def fetchByID(self, id):
        data = self.userDA.GetByID(id)
        self.populateUsers(data)

    def populateUsers(self, data):

        for row in data:
            user = User()
            user.populateFields(row)
            self.addToCollection(user)