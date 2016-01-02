__author__ = 'Matthew Grixti'

from abc import ABCMeta, abstractmethod, abstractproperty


class AbstractCollection(object):
    __metaclass__ = ABCMeta


    def __init__(self):
         self._collection = []

    @property
    def collection(self):
        return self._collection

    @collection.setter
    def collection(self, value):
        self._collection = value

    # Add item to end of collection
    def addToCollection(self, collectionItem):
        self.collection.append(collectionItem)
    # remove the item passed in from collectionItem)

    def removeFromCollection(self, collectionItem):
        self.collection.remove(collectionItem)
    # find an item by its ID in a collectionItem)

    def findByID(self, id):

        for collectionItem in self.collection:
            if(collectionItem.get_id() == id):
                return collectionItem

        return None
    # is the collection empty?rn None

    def isEmpty(self):

        if(self.collection.__len__() == 0):
            return True

        return False