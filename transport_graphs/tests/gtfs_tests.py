from nose.tools import raises
import os
from utils.decorators import CheckPathIsValid

import gtfs

from gtfsprovider import GtfsProviderCsv
from gtfsprovider import GtfsProviderSingleRowMock

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


def write_to_file(filename, data):
    """ Useful for writing datastructures to file as text """
    with open(filename, 'w') as the_file:
        the_file.write(str(data))


class TestGtfsRoute(object):
    """ Tests basic functionality of gtfs.Route objects """

    def test_construction(self):
        provider = GtfsProviderSingleRowMock()
        routes = provider.load_routes()
        assert len(routes) == 1

        first_route = routes[0]
        route = gtfs.Route(first_route)

        assert route.is_valid()
        assert route.unique_id() == first_route[u"route_id"]
        assert route.get_route_id() == route.unique_id()
        assert route.get_route_short_name() == first_route[u"route_short_name"]
        assert route.get_route_long_name() == first_route[u"route_long_name"]
        assert route.get_route_type() == first_route[u"route_type"]
        assert route == route

class TestGtfsTripElement(object):
    """ Tests basic functionality of gtfs.TripElement objects """

    def test_construction(self):
        provider = GtfsProviderSingleRowMock()
        trip_elements = provider.load_trips()
        assert len(trip_elements) == 1

        first_element = trip_elements[0]
        trip_element = gtfs.TripElement(first_element)

        assert trip_element.is_valid()

        expected_unique_id = (
                first_element[u"route_id"],
                first_element[u"service_id"],
                first_element[u"trip_id"]
            )

        assert trip_element.unique_id() == expected_unique_id
        assert trip_element.get_route_id() == first_element[u"route_id"]
        assert trip_element.get_service_id() == first_element[u"service_id"]
        assert trip_element.get_trip_id() == first_element[u"trip_id"]
        assert trip_element.get_shape_id() == first_element[u"shape_id"]
        assert trip_element.get_trip_headsign() == first_element[u"trip_headsign"]
        assert trip_element.get_direction_id() == first_element[u"direction_id"]





