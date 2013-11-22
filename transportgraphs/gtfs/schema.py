""" Contains information for correctly building and validating
    gtfs objects """

import utils.typeconverters as converters
from gtfs.models import GtfsNames


"""
Mapping of fields to type converters.
"""
UNICODE_TO_FLOAT = converters.UnicodeToFloat()
UNICODE_TO_INT = converters.UnicodeToInt()
UNICODE_TO_UNICODE = converters.UnicodeCheck()
UNICODE_TO_TIMEZONE = converters.UnicodeToTimeZone()
UNICODE_TO_DATETIME = converters.UnicodeToDatetime()
UNICODE_TO_TIME = converters.UnicodeToTime()

class GtfsSchema(object):
    """ Base class for Gtfs Schemas """

    def __init__(self):
        self.schema_lookup = {}

    def apply(self, gtfs_name, data):
        """ Given data in the form of a list of dictionaries, this will
            coerce the data to fit the schema, if possible. """
        converters = self.schema_lookup.get(gtfs_name)
        keys = converters.keys()
        converted = []
        for row in data:
            clean_dict = {
                key: converters[key].convert(row[key]) for key in keys
            }
            converted.append(clean_dict)

        return converted


class GtfsCsvSchema(GtfsSchema):
    """ Class containing information about how to
        convert values for different fields in GTFS
        objects from basic unicode input. """

    AGENCY_SCHEMA = {
        u"agency_name": UNICODE_TO_UNICODE,
        u"agency_url": UNICODE_TO_UNICODE,
        u"agency_timezone": UNICODE_TO_TIMEZONE,
        }

    CALENDAR_DATES_SCHEMA = {
        u"service_id": UNICODE_TO_UNICODE,
        u"date": UNICODE_TO_DATETIME,
        u"exception_type": UNICODE_TO_INT,
        }

    CALENDAR_SCHEMA = {
        u"service_id": UNICODE_TO_UNICODE,
        u"monday": UNICODE_TO_INT,
        u"tuesday": UNICODE_TO_INT,
        u"wednesday": UNICODE_TO_INT,
        u"thursday": UNICODE_TO_INT,
        u"friday": UNICODE_TO_INT,
        u"saturday": UNICODE_TO_INT,
        u"sunday": UNICODE_TO_INT,
        u"start_date": UNICODE_TO_DATETIME,
        u"end_date": UNICODE_TO_DATETIME,
        }

    SHAPES_SCHEMA = {
        u"shape_id": UNICODE_TO_UNICODE,
        u"shape_pt_lat": UNICODE_TO_FLOAT,
        u"shape_pt_lon": UNICODE_TO_FLOAT,
        u"shape_pt_sequence": UNICODE_TO_INT,
        u"shape_dist_traveled": UNICODE_TO_FLOAT,
        }

    STOPS_SCHEMA = {
        u"stop_id": UNICODE_TO_UNICODE,
        u"stop_name": UNICODE_TO_UNICODE,
        u"stop_lat": UNICODE_TO_FLOAT,
        u"stop_lon": UNICODE_TO_FLOAT,
        }

    ROUTES_SCHEMA = {
        u"route_id": UNICODE_TO_UNICODE,
        u"route_short_name": UNICODE_TO_UNICODE,
        u"route_long_name": UNICODE_TO_UNICODE,
        u"route_type": UNICODE_TO_INT
        }

    STOP_TIMES_SCHEMA = {
        u"trip_id": UNICODE_TO_UNICODE,
        u"arrival_time": UNICODE_TO_TIME,
        u"departure_time": UNICODE_TO_TIME,
        u"stop_id": UNICODE_TO_UNICODE,
        u"stop_sequence": UNICODE_TO_INT,
        u"pickup_type": UNICODE_TO_INT,
        u"drop_off_type": UNICODE_TO_INT,
        u"shape_dist_traveled": UNICODE_TO_FLOAT,
        }

    TRIPS_SCHEMA = {
        u"route_id": UNICODE_TO_UNICODE,
        u"service_id": UNICODE_TO_UNICODE,
        u"trip_id": UNICODE_TO_UNICODE,
        u"shape_id": UNICODE_TO_UNICODE,
        u"trip_headsign": UNICODE_TO_UNICODE,
        u"direction_id": UNICODE_TO_INT,
        }

    def __init__(self):
        super(GtfsCsvSchema, self).__init__()

        self.schema_lookup = {
            GtfsNames.AGENCY: self.AGENCY_SCHEMA,
            GtfsNames.CALENDAR: self.CALENDAR_SCHEMA,
            GtfsNames.CALENDAR_DATES: self.CALENDAR_DATES_SCHEMA,
            GtfsNames.ROUTES: self.ROUTES_SCHEMA,
            GtfsNames.SHAPES: self.SHAPES_SCHEMA,
            GtfsNames.STOPS: self.STOPS_SCHEMA,
            GtfsNames.STOP_TIMES: self.STOP_TIMES_SCHEMA,
            GtfsNames.TRIPS: self.TRIPS_SCHEMA,
        }











