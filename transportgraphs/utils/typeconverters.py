"""
typeconverters

This module contains classes used for converting between
different types
"""

from abc import ABCMeta, abstractmethod
from utils.decorators import check_value_is_unicode
from datetime import datetime, timedelta
import pytz

class UnicodeToTypeConverter(object):
    """ Base class for performing type conversion """
    __metaclass__ = ABCMeta

    @abstractmethod
    def convert(self, value):
        """ Perform the conversion or raise an exception. This
            should be defined in the base class. """
        raise NotImplementedError()


class UnicodeCheck(UnicodeToTypeConverter):
    """ Just used to check the value is indeed unicode. """

    @check_value_is_unicode
    def convert(self, value):
        return value


class UnicodeToFloat(UnicodeToTypeConverter):
    """ Converts form unicode to float """

    @check_value_is_unicode
    def convert(self, value):
        return float(value)


class UnicodeToInt(UnicodeToTypeConverter):
    """ Converts form unicode to int """

    @check_value_is_unicode
    def convert(self, value):
        return int(value)


class UnicodeToDatetime(UnicodeToTypeConverter):
    """ Converts a unicode string into datetime if
        conversion is possible. """

    def __init__(self, format='%Y%m%d'):
        self.format = format

    @check_value_is_unicode
    def convert(self, value):
        return datetime.strptime(value, self.format)

class UnicodeToTime(UnicodeToTypeConverter):
    """ Converts a unicode string into time if
        conversion is possible. """

    def __init__(self, format='%H:%M:%S'):
        self.format = format

    @check_value_is_unicode
    def convert(self, value):
        dt = datetime.strptime(value, self.format)
        return dt.time()

class UnicodeToTimeZone(UnicodeToTypeConverter):
    """ Converts a name from the tz database
        (http://en.wikipedia.org/wiki/List_of_tz_zones)
        into a pytz timezone object
        """
    @check_value_is_unicode
    def convert(self, value):
        try:
            tz = pytz.timezone(value)
            return tz
        except pytz.UnknownTimeZoneError:
            # raise Value error instead to be consistent
            raise ValueError(
                u"{0} is not a valid timezone name.".format(value)
                )


