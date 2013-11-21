"""
gtfs.py:

Data model for General Transit Feed Specification (GTFS) data.

"""

UTF8 = 'utf-8'

AGENCY_KEYS = [
    u"agency_name",
    u"agency_url",
    u"agency_timezone"
    ]

CALENDAR_DATES_KEYS = [
    u"service_id",
    u"date",
    u"exception_type"
    ]

CALENDAR_KEYS = [
    u"service_id",
    u"monday",
    u"tuesday",
    u"wednesday",
    u"thursday",
    u"friday",
    u"saturday",
    u"sunday",
    u"start_date",
    u"end_date"
    ]

SHAPES_KEYS = [
    u"shape_id",
    u"shape_pt_lat",
    u"shape_pt_lon",
    u"shape_pt_sequence",
    u"shape_dist_traveled"
    ]

STOPS_KEYS = [
    u"stop_id",
    u"stop_name",
    u"stop_lat",
    u"stop_lon"
    ]

ROUTES_KEYS = [
    u"route_id",
    u"route_short_name",
    u"route_long_name",
    u"route_type"
     ]

STOP_TIMES_KEYS = [
    u"trip_id",
    u"arrival_time",
    u"departure_time",
    u"stop_id",
    u"stop_sequence",
    u"pickup_type",
    u"drop_off_type",
    u"shape_dist_traveled"
    ]

TRIPS_KEYS = [
    u"route_id",
    u"service_id",
    u"trip_id",
    u"shape_id",
    u"trip_headsign",
    u"direction_id"
    ]

class GtfsObject(object):
    """ Base class for Gtfs Objects """

    def __init__(self, required_keys, data_dict):
        self.required_keys = required_keys
        self.data = data_dict

    def get(self, key):
        """ Gets a value stored at a given key in the object """
        return self.data.get(key, None)

    def is_valid(self):
        """ Validates object """
        return set(self.required_keys) == set(self.data.keys())

    def unique_id(self):
        """ Returns a unique key for this object.
            Should be defined in derived classes """
        pass

class Route(GtfsObject):
    """ Corresponds to a single row in the route data set """
    def __init__(self, data_dict):
        super(Route, self).__init__(ROUTES_KEYS, data_dict)

    def get_route_id(self):
        return self.get(u"route_id")

    def get_route_short_name(self):
        return self.get(u"route_short_name")

    def get_route_long_name(self):
        return self.get(u"route_long_name")

    def get_route_type(self):
        return self.get(u"route_type")

    def unique_id(self):
        """ Returns a unique key for this object """
        return self.get_route_id()

    def __str__(self):
        return unicode(self).encode(UTF8)

    def __unicode__(self):
        return u"Route: {0}, {1}, {2}, {3}".format(
            self.get_route_id(),
            self.get_route_short_name(),
            self.get_route_long_name(),
            self.get_route_type()
            )

