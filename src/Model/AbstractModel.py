__author__ = 'Matthew Grixti'

from abc import ABCMeta, abstractmethod

class AbstractModel(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self._id = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, newID):
        self._id = newID

    @abstractmethod
    def populateFields(self, data):
        pass