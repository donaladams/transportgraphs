import os
from nose.tools import raises
import gtfs.models as models
from gtfs.gtfsprovider import GtfsProviderCsv
from gtfs.gtfsprovider import GtfsProviderSingleRowMock
from utils.decorators import CheckPathIsValid
from gtfs.modelbuilder import GtfsModelBuilder
from gtfs.schema import GtfsCsvSchema

class TestCsvGtfsProvider(object):
    """ Tests the loading of GTFS csvs """

    DATA_DIRECTORY = os.path.join(os.path.abspath(os.curdir), "tests/test_data")

    def test_load_agency(self):
        """ Tests the loading of the agency.txt file
            from test_data """
        schema = GtfsCsvSchema()
        provider = GtfsProviderCsv(self.DATA_DIRECTORY, schema)
        data = provider.load_agency()
        # data is not empty
        assert data
        first = data[0]
        # data dict contains the correct keys
        assert set(first.keys()) == set(models.AGENCY_KEYS)

    def test_load_calendar_dates(self):
        """ Tests the loading of the calendar_dates.txt file
            from test_data """

        schema = GtfsCsvSchema()
        provider = GtfsProviderCsv(self.DATA_DIRECTORY, schema)
        data = provider.load_calendar_dates()
        #data is not empty
        assert data

        first = data[0]
        # data dict contains the correct keys
        assert set(first.keys()) == set(models.CALENDAR_DATES_KEYS)

    def test_load_calendar(self):
        """ Tests the loading of the calendar.txt file
            from test_data """

        schema = GtfsCsvSchema()
        provider = GtfsProviderCsv(self.DATA_DIRECTORY, schema)
        data = provider.load_calendar()
        #data is not empty
        assert data

        first = data[0]
        # data dict contains the correct keys
        assert set(first.keys()) == set(models.CALENDAR_KEYS)

    def test_load_shapes(self):
        """ Tests the loading of the shapes.txt file
            from test_data """
        schema = GtfsCsvSchema()
        provider = GtfsProviderCsv(self.DATA_DIRECTORY, schema)
        data = provider.load_shapes()
        #data is not empty
        assert data

        first = data[0]
        # data dict contains the correct keys
        assert set(first.keys()) == set(models.SHAPES_KEYS)

    def test_load_stops(self):
        """ Tests the loading of the stops.txt file
            from test_data """

        schema = GtfsCsvSchema()
        provider = GtfsProviderCsv(self.DATA_DIRECTORY, schema)
        data = provider.load_stops()
        #data is not empty
        assert data

        first = data[0]
        # data dict contains the correct keys
        assert set(first.keys()) == set(models.STOPS_KEYS)

    def test_load_routes(self):
        """ Tests the loading of the routes.txt file
            from test_data """

        schema = GtfsCsvSchema()
        provider = GtfsProviderCsv(self.DATA_DIRECTORY, schema)
        data = provider.load_routes()
        #data is not empty
        assert data

        first = data[0]
        # data dict contains the correct keys
        assert set(first.keys()) == set(models.ROUTES_KEYS)

    def test_load_stop_times(self):
        """ Tests the loading of the stop_times.txt file
            from test_data """

        schema = GtfsCsvSchema()
        provider = GtfsProviderCsv(self.DATA_DIRECTORY, schema)
        data = provider.load_stop_times()
        #data is not empty
        assert data

        first = data[0]
        # data dict contains the correct keys
        assert set(first.keys()) == set(models.STOP_TIMES_KEYS)

    def test_load_trips(self):
        """ Tests the loading of the trips.txt file
            from test_data """

        schema = GtfsCsvSchema()
        provider = GtfsProviderCsv(self.DATA_DIRECTORY, schema)
        data = provider.load_trips()
        #data not empty
        assert data

        first = data[0]
        # data dict contains the correct keys
        assert set(first.keys()) == set(models.TRIPS_KEYS)


def write_to_file(filename, data):
    """ Useful for writing datastructures to file as text """
    with open(filename, 'w') as the_file:
        the_file.write(str(data))


class TestGtfsRoute(object):
    """ Tests basic functionality of models.Route objects """

    def test_construction(self):
        schema = GtfsCsvSchema()
        provider = GtfsProviderSingleRowMock(schema)
        routes = provider.load_routes()
        assert len(routes) == 1

        first_route = routes[0]
        route = models.Route(first_route)

        assert route.is_valid()
        assert route.unique_id() == first_route[u"route_id"]
        assert route.get_route_id() == route.unique_id()
        assert route.get_route_short_name() == first_route[u"route_short_name"]
        assert route.get_route_long_name() == first_route[u"route_long_name"]
        assert route.get_route_type() == first_route[u"route_type"]
        assert route == route


class TestGtfsTripElement(object):
    """ Tests basic functionality of models.TripElement objects """

    def test_construction(self):
        schema = GtfsCsvSchema()
        provider = GtfsProviderSingleRowMock(schema)
        trip_elements = provider.load_trips()
        assert len(trip_elements) == 1

        first_element = trip_elements[0]
        trip_element = models.TripElement(first_element)

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
    """ Tests basic functionality of models.Stop objects """

    def test_construction(self):
        schema = GtfsCsvSchema()
        provider = GtfsProviderSingleRowMock(schema)
        stops_elements = provider.load_stops()
        assert len(stops_elements) == 1

        first_element = stops_elements[0]
        stop = models.Stop(first_element)

        assert stop.is_valid()

        expected_unique_id = first_element[u"stop_id"]
        assert stop.unique_id() == expected_unique_id
        assert stop.get_stop_id() == expected_unique_id
        assert stop.get_stop_name() == first_element[u"stop_name"]
        assert stop.get_stop_lat() == first_element[u"stop_lat"]
        assert stop.get_stop_lon() == first_element[u"stop_lon"]


class TestGtfsStopTime(object):
    """ Tests basic functionality of models.StopTime objects """

    def test_construction(self):
        schema = GtfsCsvSchema()
        provider = GtfsProviderSingleRowMock(schema)
        stop_times = provider.load_stop_times()
        assert len(stop_times) == 1

        first_element = stop_times[0]
        stop_time = models.StopTime(first_element)

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


class TestGtfsAgency(object):
    """ Tests the basic functionality of gtfs.models.Agency """
    def test_construction(self):
        schema = GtfsCsvSchema()
        provider = GtfsProviderSingleRowMock(schema)
        agencies = provider.load_agency()

        assert len(agencies) == 1

        first_element = agencies[0]
        agency = models.Agency(first_element)

        assert agency.is_valid()

        expected_unique_id = first_element[u"agency_name"]
        assert agency.unique_id() == expected_unique_id
        assert agency.get_agency_name() == expected_unique_id
        assert agency.get_agency_url() == first_element[u"agency_url"]

        expected_timezone = first_element[u"agency_timezone"]
        assert(agency.get_agency_timezone() == expected_timezone)


class TestGtfsCalendarElement(object):
    """ Tests basic functionality of models.CalendarElement objects """

    def test_construction(self):
        schema = GtfsCsvSchema()
        provider = GtfsProviderSingleRowMock(schema)
        calendar_elements = provider.load_calendar()
        assert len(calendar_elements) == 1

        first_element = calendar_elements[0]
        calendar = models.CalendarElement(first_element)

        assert calendar.is_valid()

        expected_unique_id = first_element[u"service_id"]

        assert calendar.unique_id() == expected_unique_id
        assert calendar.get_service_id() == expected_unique_id
        assert calendar.get_monday() == first_element[u"monday"]
        assert calendar.get_tuesday() == first_element[u"tuesday"]
        assert calendar.get_wednesday() == first_element[u"wednesday"]
        assert calendar.get_thursday() == first_element[u"thursday"]
        assert calendar.get_friday() == first_element[u"friday"]
        assert calendar.get_saturday() == first_element[u"saturday"]
        assert calendar.get_sunday() == first_element[u"sunday"]

        expected_week = (
            calendar.get_monday(),
            calendar.get_tuesday(),
            calendar.get_wednesday(),
            calendar.get_thursday(),
            calendar.get_friday(),
            calendar.get_saturday(),
            calendar.get_sunday(),
            )
        assert calendar.get_week() == expected_week

        expected_start_date = first_element[u"start_date"]
        expected_end_date = first_element[u"end_date"]
        assert calendar.get_start_date() == expected_start_date
        assert calendar.get_end_date() == expected_end_date

class TestGtfsCalendarDatesElement(object):
    """ Tests basic functionality of models.CalendarDatesElement objects """

    def test_construction(self):
        schema = GtfsCsvSchema()
        provider = GtfsProviderSingleRowMock(schema)
        calendar_dates_elements = provider.load_calendar_dates()
        assert len(calendar_dates_elements) == 1

        first_element = calendar_dates_elements[0]
        calendar_date = models.CalendarDatesElement(first_element)

        assert calendar_date.is_valid()

        expected_unique_id = first_element[u"service_id"]
        assert calendar_date.unique_id() == expected_unique_id
        assert calendar_date.get_service_id() == expected_unique_id
        assert calendar_date.get_date() == first_element[u"date"]

        expected_exception_type = first_element[u"exception_type"]
        assert calendar_date.get_exception_type() == expected_exception_type

class TestGtfsShapeElement(object):
    """ Tests basic functionality of models.CalendarDatesElement objects """

    def test_construction(self):
        schema = GtfsCsvSchema()
        provider = GtfsProviderSingleRowMock(schema)
        shape_elements = provider.load_shapes()
        assert len(shape_elements) == 1

        first_element = shape_elements[0]
        shape_element = models.ShapeElement(first_element)

        assert shape_element.is_valid()

        expected_unique_id = (
            first_element[u"shape_id"],
            first_element[u"shape_pt_sequence"]
            )

        assert shape_element.unique_id() == expected_unique_id
        assert shape_element.get_shape_id() == first_element[u"shape_id"]
        assert shape_element.get_shape_pt_lat() == first_element[u"shape_pt_lat"]
        assert shape_element.get_shape_pt_lon() == first_element[u"shape_pt_lon"]

        expected_sequence = first_element[u"shape_pt_sequence"]
        assert shape_element.get_shape_pt_sequence() == expected_sequence

        expected_distance = first_element[u"shape_dist_traveled"]
        assert shape_element.get_shape_dist_traveled() == expected_distance


class TestModelBuilder(object):
    """ Tests the model builder"""
    DATA_DIRECTORY = os.path.join(os.path.abspath(os.curdir), "tests/test_data")

    def test_get_agency(self):
        """ Gets Agency models correctly """
        schema = GtfsCsvSchema()
        provider = GtfsProviderSingleRowMock(schema)
        builder = GtfsModelBuilder(provider, schema)
        agencies = builder.get_agencies()

        assert len(agencies) > 0

        model = agencies[0]
        assert type(model) == models.Agency
        return model.is_valid()

    def test_get_routes(self):
        """ Gets Route models correctly """
        schema = GtfsCsvSchema()
        provider = GtfsProviderSingleRowMock(schema)
        builder = GtfsModelBuilder(provider, schema)
        routes = builder.get_routes()

        assert len(routes)  > 0
        route = routes[0]

        assert type(route) == models.Route
        assert route.is_valid()

    def test_get_stops(self):
        """ Gets Stop models correctly """
        schema = GtfsCsvSchema()
        provider = GtfsProviderSingleRowMock(schema)
        builder = GtfsModelBuilder(provider, schema)
        stops = builder.get_stops()

        assert len(stops) > 0
        stop = stops[0]

        assert type(stop) == models.Stop
        assert stop.is_valid()

    def test_get_stop_times(self):
        """ Gets Stop Time models correctly """
        schema = GtfsCsvSchema()
        provider = GtfsProviderSingleRowMock(schema)
        builder = GtfsModelBuilder(provider, schema)
        stop_times = builder.get_stop_times()

        assert len(stop_times) > 0
        stop_time = stop_times[0]

        assert type(stop_time) == models.StopTime
        assert stop_time.is_valid()

    def test_get_trip_elements(self):
        """ Gets Trip Element models correctly """
        schema = GtfsCsvSchema()
        provider = GtfsProviderSingleRowMock(schema)
        builder = GtfsModelBuilder(provider, schema)
        trip_elements = builder.get_trip_elements()

        assert len(trip_elements) > 0
        trip_element = trip_elements[0]

        assert type(trip_element) == models.TripElement
        assert trip_element.is_valid()

    def test_get_calendar_elements(self):
        """ Gets CalendarElement models correctly """
        schema = GtfsCsvSchema()
        provider = GtfsProviderSingleRowMock(schema)
        builder = GtfsModelBuilder(provider, schema)
        calendar_elements = builder.get_calendar_elements()

        assert len(calendar_elements) > 0
        calendar_element = calendar_elements[0]

        assert type(calendar_element) == models.CalendarElement
        assert calendar_element.is_valid()


    def test_get_calendar_date_elements(self):
        """ Gets CalendarDatesElement models correctly """
        schema = GtfsCsvSchema()
        provider = GtfsProviderSingleRowMock(schema)
        builder = GtfsModelBuilder(provider, schema)
        calendar_date_elements = builder.get_calendar_dates_elements()

        assert len(calendar_date_elements) > 0
        calendar_date_element = calendar_date_elements[0]

        assert type(calendar_date_element) == models.CalendarDatesElement
        assert calendar_date_element.is_valid()

    def test_get_shape_elements(self):
        """ Gets ShapeElement models correctly """
        schema = GtfsCsvSchema()
        provider = GtfsProviderSingleRowMock(schema)
        builder = GtfsModelBuilder(provider, schema)
        shapes = builder.get_shape_elements()

        assert len(shapes) > 0
        shape_element = shapes[0]

        assert type(shape_element) == models.ShapeElement
        assert shape_element.is_valid()



