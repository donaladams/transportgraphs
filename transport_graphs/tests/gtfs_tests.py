from nose.tools import *
import os

from utils.decorators import CheckPathIsValid
import gtfs

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
        """ Test with the path to the current directoy invalidated
            by lopping off some chars and adding random ones """
        path = os.path.abspath(os.curdir)
        path = path[:-3] + "asdfasjdkjhg"
        output = function_to_decorate(path)
        assert False


class TestGTFSLoadCsv(object):
    """ Tests the loading of GTFS csvs """

    DATA_DIRECTORY = os.path.join(os.path.abspath(os.curdir), "tests/test_data")

    def test_load_agency(self):
        data = gtfs.load_agency(self.DATA_DIRECTORY)
        assert data

        first = data[0]
        assert set(first.keys()) == set(gtfs.AGENCY_KEYS)


    def test_load_calendar_dates(self):
        data = gtfs.load_calendar_dates(self.DATA_DIRECTORY)
        assert data
        first = data[0]
        assert set(first.keys()) == set(gtfs.CALENDAR_DATES_KEYS)

    def test_load_calendar(self):
        data = gtfs.load_calendar(self.DATA_DIRECTORY)
        assert data

        first = data[0]
        assert set(first.keys()) == set(gtfs.CALENDAR_KEYS)

    def test_load_shapes(self):
        data = gtfs.load_shapes(self.DATA_DIRECTORY)
        assert data

        first = data[0]
        assert set(first.keys()) == set(gtfs.SHAPES_KEYS)

    def test_load_stops(self):
        data = gtfs.load_stops(self.DATA_DIRECTORY)
        assert data

        first = data[0]
        assert set(first.keys()) == set(gtfs.STOPS_KEYS)

    def test_load_routes(self):
        data = gtfs.load_routes(self.DATA_DIRECTORY)
        assert data

        first = data[0]
        assert set(first.keys()) == set(gtfs.ROUTES_KEYS)

    def test_load_stop_times(self):
        data = gtfs.load_stop_times(self.DATA_DIRECTORY)
        assert data

        first = data[0]
        assert set(first.keys()) == set(gtfs.STOP_TIMES_KEYS)

    def test_load_trips(self):
        data = gtfs.load_trips(self.DATA_DIRECTORY)
        assert data

        first = data[0]
        assert set(first.keys()) == set(gtfs.TRIPS_KEYS)



