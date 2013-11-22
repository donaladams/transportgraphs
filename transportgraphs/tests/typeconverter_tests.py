import pytz
import datetime
from nose.tools import raises
from utils.typeconverters import UnicodeToFloat
from utils.typeconverters import UnicodeToInt
from utils.typeconverters import UnicodeCheck
from utils.typeconverters import UnicodeToTimeZone
from utils.typeconverters import UnicodeToDatetime
from utils.typeconverters import UnicodeToTime

class TestUnicodeToFloat(object):
    """ Tests the functionality of UnicodeToFloat """

    def test_pass_on_valid_input_a(self):
        unicode_string = u"1.65"

        converter = UnicodeToFloat()
        output = converter.convert(unicode_string)

        assert type(output) is float
        assert output == 1.65

    def test_pass_on_valid_input_b(self):
        unicode_string = u"1000"

        converter = UnicodeToFloat()
        output = converter.convert(unicode_string)

        assert type(output) is float
        assert output == 1000.0

    @raises(ValueError)
    def test_fail_on_conversion_impossible(self):
        unicode_string = u"I'm a unicode string"

        converter = UnicodeToFloat()
        output = converter.convert(unicode_string)
        #should not reach here
        assert False

    @raises(ValueError)
    def test_fail_on_input_not_unicode(self):
        input_value = None

        converter = UnicodeToFloat()
        output = converter.convert(input_value)
        #should not reach here
        assert False


class TestUnicodeToInt(object):
    """ Tests the functionality of UnicodeToInt """

    def test_pass_on_valid_input_a(self):
        unicode_string = u"1"

        converter = UnicodeToInt()
        output = converter.convert(unicode_string)

        assert type(output) is int
        assert output == 1

    def test_pass_on_valid_input_b(self):
        unicode_string = u"-21000"

        converter = UnicodeToInt()
        output = converter.convert(unicode_string)

        assert type(output) is int
        assert output == -21000

    @raises(ValueError)
    def test_fail_on_conversion_impossible(self):
        unicode_string = u"I'm a unicode string"

        converter = UnicodeToInt()
        output = converter.convert(unicode_string)
        #should not reach here
        assert False

    @raises(ValueError)
    def test_fail_on_input_not_unicode(self):
        input_value = None

        converter = UnicodeToInt()
        output = converter.convert(input_value)
        #should not reach here
        assert False


class TestUnicodeCheck(object):
    """ Tests the UnicodeCheck converter class """

    @raises(ValueError)
    def test_non_unicode_input(self):
        python_string = "I'm a python string"
        converter = UnicodeCheck()
        output = converter.convert(python_string)
        #should not reach here
        assert False

    def test_unicode_input(self):
        unicode_string = u"I'm a unicodestring"

        converter = UnicodeCheck()
        output = converter.convert(unicode_string)

        assert type(output) is unicode
        assert output == unicode_string


class TestUnicodeToTimeZone(object):
    """ Tests the UnicodeToTimeZone class """

    def test_valid_input(self):
        """ This should correctly produce a class
            derived from datetime.tzinfo """
        unicode_string = u"Europe/Dublin"

        converter = UnicodeToTimeZone()
        output = converter.convert(unicode_string)

        assert issubclass(type(output), datetime.tzinfo)
        assert output.zone == unicode_string

    @raises(ValueError)
    def test_invalid_input(self):
        """ This should cause the converter to throw
            a ValueError"""
        unicode_string = u"I'm definitely not a time zone name"

        converter = UnicodeToTimeZone()
        output = converter.convert(unicode_string)


class TestUnicodeToDatetime(object):
    """ Test conversion of unicode to datetime """

    def test_correct_gtfs_date_format_input(self):
        unicode_string = u"20130520"
        converter = UnicodeToDatetime("%Y%m%d")
        output = converter.convert(unicode_string)

        assert type(output) == datetime.datetime
        assert output.year == 2013
        assert output.month == 5
        assert output.day == 20
        assert output.hour == 0
        assert output.minute == 0
        assert output.second == 0

    @raises(ValueError)
    def test_bad_gtfs_format_input(self):
        """ Should through a ValueError as date incorrect"""
        unicode_string = u"adcd201212"
        converter = UnicodeToDatetime("%Y%m%d")
        output = converter.convert(unicode_string)
        #should not reach here
        assert False


class TestUnicodeToTime(object):
    """ Test conversion of unicode to datetime.time """

    def test_correct_gtfs_time_format_input(self):
        unicode_string = u"10:05:10"
        converter = UnicodeToTime("%H:%M:%S")
        output = converter.convert(unicode_string)

        assert type(output) == datetime.time
        assert output.hour == 10
        assert output.minute == 5
        assert output.second == 10


    @raises(ValueError)
    def test_bad_gtfs_format_input(self):
        """ Should through a ValueError as time incorrect"""
        unicode_string = u"1:65:0a"
        converter = UnicodeToTime("%Y%m%d")
        output = converter.convert("%H:%M:%S")
        #should not reach here
        assert False




