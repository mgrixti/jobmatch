__author__ = 'Matthew Grixti'


class AbstractCollection:

    collection = []

    def addToCollection(self, collectionItem):
        self.collection.append(collectionItem)

    def removeFromCollection(self, collectionItem):
        self.collection.remove(collectionItem)

    def findByID(self, id):

        for collectionItem in self.collection:
            if(collectionItem.get_id() == id):
                return collectionItem

        return None

    def getCollection(self):
        return self.collection

    def setCollection(self, newCollection):
        self.collection = newCollection

    def isEmpty(self):

        if(self.collection.__len__() == 0):
            return True

        return False