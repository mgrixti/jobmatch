__author__ = 'Matthew Grixti'

from abc import ABCMeta, abstractmethod

class AbstractModel(object):
    __metaclass__ = ABCMeta

    id = None

    def get_id(self):
        return self.id

    @abstractmethod
    def populateFields(self, data):
        pass