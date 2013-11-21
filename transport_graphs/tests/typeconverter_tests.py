from nose.tools import raises
from utils.typeconverters import UnicodeToFloatConverter
from utils.typeconverters import UnicodeToIntConverter

class TestUnicodeToFloatConverter(object):
    """ Tests the functionality of UnicodeToFloatConverter"""

    def test_pass_on_valid_input_a(self):
        unicode_string = u"1.65"

        converter = UnicodeToFloatConverter()
        output = converter.convert(unicode_string)

        assert type(output) is float
        assert output == 1.65

    def test_pass_on_valid_input_b(self):
        unicode_string = u"1000"

        converter = UnicodeToFloatConverter()
        output = converter.convert(unicode_string)

        assert type(output) is float
        assert output == 1000.0

    @raises(ValueError)
    def test_fail_on_conversion_impossible(self):
        unicode_string = u"I'm a unicode string"

        converter = UnicodeToFloatConverter()
        output = converter.convert(unicode_string)

        assert False

    @raises(ValueError)
    def test_fail_on_input_not_unicode(self):
        input_value = None

        converter = UnicodeToFloatConverter()
        output = converter.convert(input_value)

        assert False

class TestUnicodeToIntConverter(object):
    """ Tests the functionality of UnicodeToFloatConverter"""

    def test_pass_on_valid_input_a(self):
        unicode_string = u"1"

        converter = UnicodeToIntConverter()
        output = converter.convert(unicode_string)

        assert type(output) is int
        assert output == 1

    def test_pass_on_valid_input_b(self):
        unicode_string = u"-21000"

        converter = UnicodeToIntConverter()
        output = converter.convert(unicode_string)

        assert type(output) is int
        assert output == -21000

    @raises(ValueError)
    def test_fail_on_conversion_impossible(self):
        unicode_string = u"I'm a unicode string"

        converter = UnicodeToIntConverter()
        output = converter.convert(unicode_string)

        assert False

    @raises(ValueError)
    def test_fail_on_input_not_unicode(self):
        input_value = None

        converter = UnicodeToIntConverter()
        output = converter.convert(input_value)

        assert False
