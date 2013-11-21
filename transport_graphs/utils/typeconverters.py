from abc import ABCMeta, abstractmethod
from exceptions import NotImplementedError

class UnicodeToTypeConverter(object):
    """ Base class for performing type conversion """
    __metaclass__ = ABCMeta

    @abstractmethod
    def convert(self, value):
        pass