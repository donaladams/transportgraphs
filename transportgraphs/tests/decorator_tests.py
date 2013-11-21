import os
from utils.decorators import CheckPathIsValid
from utils.decorators import check_value_is_unicode
from nose.tools import raises

@CheckPathIsValid
def function_to_decorate(path):
    """ For use in TestCheckPathIsValidDecorator unit tests"""
    return path


class TestCheckPathIsValidDecorator(object):
    """ Unit tests for decorators.CheckPathIsValid """

    def test_with_valid_path(self):
        """ Test with the path to the current directory """
        path = os.path.abspath(os.curdir)
        output = function_to_decorate(path)
        assert output == path

    @raises(ValueError)
    def test_with_invalid_path(self):
        """ Test with the path to the current directory invalidated
            by lopping off some chars and adding random ones """
        path = os.path.abspath(os.curdir)
        path = path[:-3] + "asdfasjdkjhg"
        output = function_to_decorate(path)
        assert False


class TestCheckValueIsUnicode(object):

    @raises(ValueError)
    def test_check_fails_integer(self):
        """ This should throw a ValueError as
            the input is an int """
        integer = 123
        output = self.method_requiring_validation(integer)

    @raises(ValueError)
    def test_check_fails_string(self):
        """ This should throw a ValueError as the input is a str """
        string = "The quick brown fox"
        output = self.method_requiring_validation(string)

    @raises(ValueError)
    def test_check_fails_none(self):
        """ This should throw a ValueError as the input is None """
        none = None
        output = self.method_requiring_validation(none)

    def test_check_passes(self):
        """ Unicode object given as input - this should pass. """
        unicode_string = u"Jumps over the lazy dog"
        output = self.method_requiring_validation(unicode_string)
        assert output == unicode_string


    @check_value_is_unicode
    def method_requiring_validation(self, value):
        """ Method used purely to be decorated
            for testing """
        return value