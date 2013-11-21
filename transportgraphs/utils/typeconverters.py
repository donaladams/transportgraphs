from abc import ABCMeta, abstractmethod
from exceptions import NotImplementedError
from exceptions import ValueError
from utils.decorators import check_value_is_unicode

class UnicodeToTypeConverter(object):
    """ Base class for performing type conversion """
    __metaclass__ = ABCMeta

    @abstractmethod
    def convert(self, value):
        """ Perform the conversion or raise an exception. This
            should be defined in the base class. """
        raise NotImplementedError

class UnicodeToFloatConverter(UnicodeToTypeConverter):
    """ Converts form unicode to float """

    @check_value_is_unicode
    def convert(self, value):
        return float(value)

class UnicodeToIntConverter(UnicodeToTypeConverter):
    """ Converts form unicode to int """

    @check_value_is_unicode
    def convert(self, value):
        return int(value)



