from nose.tools import raises
import os
from utils.decorators import CheckPathIsValid
import gtfs
from gtfsprovider import GtfsProviderCsv

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

class TestCsvGtfsProvider(object):
    """ Tests the loading of GTFS csvs """

    DATA_DIRECTORY = os.path.join(os.path.abspath(os.curdir), "tests/test_data")

    def test_load_agency(self):
        """ Tests the loading of the agency.txt file
            from test_data """
        provider = GtfsProviderCsv(self.DATA_DIRECTORY)
        data = provider.load_agency()
        # data is not empty
        assert data

        first = data[0]
        # data dict contains the correct keys
        assert set(first.keys()) == set(gtfs.AGENCY_KEYS)

    def test_load_calendar_dates(self):
        """ Tests the loading of the calendar_dates.txt file
            from test_data """
        provider = GtfsProviderCsv(self.DATA_DIRECTORY)
        data = provider.load_calendar_dates()
        #data is not empty
        assert data

        first = data[0]
        # data dict contains the correct keys
        assert set(first.keys()) == set(gtfs.CALENDAR_DATES_KEYS)

    def test_load_calendar(self):
        """ Tests the loading of the calendar.txt file
            from test_data """
        provider = GtfsProviderCsv(self.DATA_DIRECTORY)
        data = provider.load_calendar()
        #data is not empty
        assert data

        first = data[0]
        # data dict contains the correct keys
        assert set(first.keys()) == set(gtfs.CALENDAR_KEYS)

    def test_load_shapes(self):
        """ Tests the loading of the shapes.txt file
            from test_data """
        provider = GtfsProviderCsv(self.DATA_DIRECTORY)
        data = provider.load_shapes()
        #data is not empty
        assert data

        first = data[0]
        # data dict contains the correct keys
        assert set(first.keys()) == set(gtfs.SHAPES_KEYS)

    def test_load_stops(self):
        """ Tests the loading of the stops.txt file
            from test_data """
        provider = GtfsProviderCsv(self.DATA_DIRECTORY)
        data = provider.load_stops()
        #data is not empty
        assert data

        first = data[0]
        # data dict contains the correct keys
        assert set(first.keys()) == set(gtfs.STOPS_KEYS)

    def test_load_routes(self):
        """ Tests the loading of the routes.txt file
            from test_data """
        provider = GtfsProviderCsv(self.DATA_DIRECTORY)
        data = provider.load_routes()
        #data is not empty
        assert data

        first = data[0]
        # data dict contains the correct keys
        assert set(first.keys()) == set(gtfs.ROUTES_KEYS)

    def test_load_stop_times(self):
        """ Tests the loading of the stop_times.txt file
            from test_data """
        provider = GtfsProviderCsv(self.DATA_DIRECTORY)
        data = provider.load_stop_times()
        #data is not empty
        assert data

        first = data[0]
        # data dict contains the correct keys
        assert set(first.keys()) == set(gtfs.STOP_TIMES_KEYS)

    def test_load_trips(self):
        """ Tests the loading of the trips.txt file
            from test_data """
        provider = GtfsProviderCsv(self.DATA_DIRECTORY)
        data = provider.load_trips()
        #data not empty
        assert data

        first = data[0]
        # data dict contains the correct keys
        assert set(first.keys()) == set(gtfs.TRIPS_KEYS)



