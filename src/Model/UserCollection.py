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
            print(row)
            user = User()
            user.populateFields(row)
            self.addToCollection(user)

# userCollection = UserCollection()
# userCollection.fetchAll()
# user = userCollection.findByID(1)
# print(user.get_id())
#
# for user1 in userCollection.getCollection():
#     print(user1)
#     print(user1.id, user1.first_name, user1.last_name)