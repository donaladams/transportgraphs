import gtfs.mocks as mocks
from gtfs.schema import GtfsCsvSchema
from gtfs.models import GtfsNames
import pytz
import datetime as dt

class TestGtfsCsvSchema(object):

    def test_agency_schema_correct(self):
        """ Agency schema works on good data """
        data = mocks.GtfsSingleRowMock().agency()
        schema = GtfsCsvSchema()
        output = schema.apply(GtfsNames.AGENCY, data)

        assert len(output) == 1

        first_row = data[0]
        first_output = output[0]

        assert first_output[u"agency_name"] == first_row[u"agency_name"]
        assert first_output[u"agency_url"] == first_row[u"agency_url"]
        expected_tzinfo = pytz.timezone(first_row[u"agency_timezone"])
        assert first_output[u"agency_timezone"] == expected_tzinfo

    def test_calendar_dates_schema_correct(self):
        """ Calendar Dates schema works on good data """
        data = mocks.GtfsSingleRowMock().calendar_dates()
        schema = GtfsCsvSchema()
        output = schema.apply(GtfsNames.CALENDAR_DATES, data)

        assert len(output) == 1

        first_row = data[0]
        first_output = output[0]

        assert first_row[u"service_id"] == first_output[u"service_id"]
        expected_date = dt.datetime(2012, 12, 25)
        assert first_output[u"date"] == expected_date
        assert first_output[u"exception_type"] == int(first_row[u"exception_type"])

    def test_calendar_schema_correct(self):
        """ Calendar schema works on good data """
        data = mocks.GtfsSingleRowMock().calendar()
        schema = GtfsCsvSchema()
        output = schema.apply(GtfsNames.CALENDAR, data)

        assert len(output) == 1

        first_row = data[0]
        first_output = output[0]

        assert first_row[u"service_id"] == first_output[u"service_id"]
        expected_start_date = dt.datetime(2012, 11, 18)
        assert first_output[u"start_date"] == expected_start_date
        expected_end_date = dt.datetime(2012, 12, 31)
        assert first_output[u"end_date"] == expected_end_date
        assert first_output[u"monday"] == 1
        assert first_output[u"tuesday"] == 1
        assert first_output[u"wednesday"] == 1
        assert first_output[u"thursday"] == 1
        assert first_output[u"friday"] == 1
        assert first_output[u"saturday"] == 0
        assert first_output[u"sunday"] == 0

    def test_shapes_schema_correct(self):
        """ Shapes schema works on good data """
        data = mocks.GtfsSingleRowMock().shapes()
        schema = GtfsCsvSchema()
        output = schema.apply(GtfsNames.SHAPES, data)

        assert len(output) == 1

        first_row = data[0]
        first_output = output[0]

        assert first_output[u"shape_id"] == first_row[u"shape_id"]
        assert first_output[u"shape_pt_lat"] == float(first_row[u"shape_pt_lat"])
        assert first_output[u"shape_pt_lon"] == float(first_row[u"shape_pt_lon"])
        assert first_output[u"shape_pt_sequence"] == int(first_row[u"shape_pt_sequence"])
        assert first_output[u"shape_dist_traveled"] == float(first_row[u"shape_dist_traveled"])

    def test_stops_schema_correct(self):
        """ Stops schema works on good data """
        data = mocks.GtfsSingleRowMock().stops()
        schema = GtfsCsvSchema()
        output = schema.apply(GtfsNames.STOPS, data)

        assert len(output) == 1

        first_row = data[0]
        first_output = output[0]

        assert first_output[u"stop_id"] == first_row[u"stop_id"]
        assert first_output[u"stop_lat"] == float(first_row[u"stop_lat"])
        assert first_output[u"stop_lon"] == float(first_row[u"stop_lon"])
        assert first_output[u"stop_name"] == first_row[u"stop_name"]

    def test_routes_schema_correct(self):
        """ Routes schema works on good data """
        data = mocks.GtfsSingleRowMock().routes()
        schema = GtfsCsvSchema()
        output = schema.apply(GtfsNames.ROUTES, data)

        assert len(output) == 1

        first_row = data[0]
        first_output = output[0]

        assert first_output[u"route_id"] == first_row[u"route_id"]
        assert first_output[u"route_short_name"] == first_row[u"route_short_name"]
        assert first_output[u"route_long_name"] == first_row[u"route_long_name"]
        assert first_output[u"route_type"] == int(first_row[u"route_type"])

    def test_stop_times_schema_correct(self):
        """ Stop Times schema works on good data """
        data = mocks.GtfsSingleRowMock().stop_times()
        schema = GtfsCsvSchema()
        output = schema.apply(GtfsNames.STOP_TIMES, data)

        assert len(output) == 1

        first_row = data[0]
        first_output = output[0]

        assert first_output[u"trip_id"] == first_row[u"trip_id"]

        expected_arrival_time = dt.time(16,15,0)
        expected_departure_time = expected_arrival_time
        assert first_output[u"arrival_time"] == expected_arrival_time
        assert first_output[u"departure_time"] == expected_departure_time
        assert first_output[u"stop_id"] == first_row[u"stop_id"]
        assert first_output[u"stop_sequence"] == int(first_row[u"stop_sequence"])
        assert first_output[u"pickup_type"] == int(first_row[u"pickup_type"])
        assert first_output[u"drop_off_type"] == int(first_row[u"drop_off_type"])

        expected_distance = float(first_row[u"shape_dist_traveled"])
        assert first_output[u"shape_dist_traveled"] == expected_distance

    def test_trip_schema_correct(self):
        """ Stop Times schema works on good data """
        data = mocks.GtfsSingleRowMock().trips()
        schema = GtfsCsvSchema()
        output = schema.apply(GtfsNames.TRIPS, data)

        assert len(output) == 1

        first_row = data[0]
        first_output = output[0]

        assert first_output[u"trip_id"] == first_row[u"trip_id"]
        assert first_output[u"route_id"] == first_row[u"route_id"]
        assert first_output[u"shape_id"] == first_row[u"shape_id"]
        assert first_output[u"service_id"] == first_row[u"service_id"]
        assert first_output[u"direction_id"] == int(first_row[u"direction_id"])
        assert first_output[u"trip_headsign"] == first_row[u"trip_headsign"]



