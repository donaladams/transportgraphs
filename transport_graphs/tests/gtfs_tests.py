import os
from nose.tools import raises
import gtfs
from gtfsprovider import GtfsProviderCsv
from gtfsprovider import GtfsProviderSingleRowMock
from utils.decorators import CheckPathIsValid


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

class TestGtfsStop(object):
    """ Tests basic functionality of gtfs.Stop objects """

    def test_construction(self):
        provider = GtfsProviderSingleRowMock()
        stops_elements = provider.load_stops()
        assert len(stops_elements) == 1

        first_element = stops_elements[0]
        stop = gtfs.Stop(first_element)

        assert stop.is_valid()

        expected_unique_id = first_element[u"stop_id"]
        assert stop.unique_id() == expected_unique_id
        assert stop.get_stop_id() == expected_unique_id
        assert stop.get_stop_name() == first_element[u"stop_name"]
        assert stop.get_stop_lat() == first_element[u"stop_lat"]
        assert stop.get_stop_lon() == first_element[u"stop_lon"]

class TestGtfsStopTime(object):
    """ Tests basic functionality of gtfs.StopTime objects """

    def test_construction(self):
        provider = GtfsProviderSingleRowMock()
        stop_times = provider.load_stop_times()
        assert len(stop_times) == 1

        first_element = stop_times[0]
        stop_time = gtfs.StopTime(first_element)

        assert stop_time.is_valid()

        expected_unique_id = (
            first_element[u"trip_id"],
            first_element[u"arrival_time"],
            first_element[u"departure_time"],
            first_element[u"stop_id"],
            first_element[u"stop_sequence"]
            )

        assert stop_time.unique_id() == expected_unique_id
        assert stop_time.get_trip_id() == first_element[u"trip_id"]
        assert stop_time.get_arrival_time() == first_element[u"arrival_time"]
        assert stop_time.get_departure_time() == first_element[u"departure_time"]
        assert stop_time.get_stop_id() == first_element[u"stop_id"]
        assert stop_time.get_stop_sequence() == first_element[u"stop_sequence"]
        assert stop_time.get_pickup_type() == first_element[u"pickup_type"]
        assert stop_time.get_drop_off_type() == first_element[u"drop_off_type"]
        assert stop_time.get_shape_dist_traveled() == first_element[u"shape_dist_traveled"]


