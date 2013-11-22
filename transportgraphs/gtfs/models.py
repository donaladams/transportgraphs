"""
gtfs.py:

Data model for General Transit Feed Specification (GTFS) data.

"""
class GtfsNames:
    AGENCY = 0
    CALENDAR = 1
    CALENDAR_DATES = 2
    ROUTES = 3
    SHAPES = 4
    STOPS = 5
    STOP_TIMES = 6
    TRIPS = 7

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
    """ Base class for Gtfs Objects. Contains
        common functionality between the objects. """

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
        raise NotImplementedError(
            "unique id should be defined in derived class. Do not use this class directly! "
            )

    def __eq__(self, other):
        """ Basing equality on id """
        return self.unique_id() == other.unique_id()

    def __str__(self):
        return unicode(self).encode(UTF8)


class Route(GtfsObject):
    """ Corresponds to a single row in the route dataset """
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
        """ Returns a unique key for this object.
            This is simply the route_id for the object """
        return self.get_route_id()

    def __unicode__(self):
        return u"Route: {0}, {1}, {2}, {3}".format(
            self.get_route_id(),
            self.get_route_short_name(),
            self.get_route_long_name(),
            self.get_route_type()
            )


class TripElement(GtfsObject):
    """ Corresponds to a single row in the trips dataset """

    def __init__(self, data_dict):
        super(TripElement, self).__init__(TRIPS_KEYS, data_dict)

    def get_route_id(self):
        return self.get(u"route_id")

    def get_service_id(self):
        return self.get(u"service_id")

    def get_trip_id(self):
        return self.get(u"trip_id")

    def get_shape_id(self):
        return self.get(u"shape_id")

    def get_trip_headsign(self):
        return self.get(u"trip_headsign")

    def get_direction_id(self):
        return self.get(u"direction_id")

    def unique_id(self):
        """ Returns a unique key for this object.
            This is a tuple of (route_id, service_id, trip_id) """
        return (self.get_route_id(), self.get_service_id(), self.get_trip_id())

    def __unicode__(self):
        return u"TripElement: {0}, {1}, {2}, {3}, {5}, {6}".format(
            self.get_route_id(),
            self.get_service_id(),
            self.get_trip_id(),
            self.get_shape_id(),
            self.get_trip_headsign(),
            self.get_direction_id()
            )


class Stop(GtfsObject):
    """ Corresponds to a single row in the stops dataset """

    def __init__(self, data_dict):
        super(Stop, self).__init__(STOPS_KEYS, data_dict)

    def get_stop_id(self):
        return self.get(u"stop_id")

    def get_stop_name(self):
        return self.get(u"stop_name")

    def get_stop_lat(self):
        return self.get(u"stop_lat")

    def get_stop_lon(self):
        return self.get(u"stop_lon")

    def unique_id(self):
        """ Returns a unique key for this object.
            This is simply stop_id. """
        return self.get_stop_id()

    def __unicode__(self):
        return u"Stop: {0}, {1}, {2}, {3}".format(
            self.get_stop_id(),
            self.get_stop_name(),
            self.get_stop_lat(),
            self.get_stop_lon(),
            )


class StopTime(GtfsObject):
    """ Corresponds to a single row in the stop_times dataset """
    def __init__(self, data_dict):
        super(StopTime, self).__init__(STOP_TIMES_KEYS, data_dict)

    def get_trip_id(self):
        return self.get(u"trip_id")

    def get_arrival_time(self):
        return self.get(u"arrival_time")

    def get_departure_time(self):
        return self.get(u"departure_time")

    def get_stop_id(self):
        return self.get(u"stop_id")

    def get_stop_sequence(self):
        return self.get(u"stop_sequence")

    def get_pickup_type(self):
        return self.get(u"pickup_type")

    def get_drop_off_type(self):
        return self.get(u"drop_off_type")

    def get_shape_dist_traveled(self):
        return self.get(u"shape_dist_traveled")

    def unique_id(self):
        """ Returns a unique key for this object.
            This is as tuple of the required values. """
        return (
            self.get_trip_id(),
            self.get_arrival_time(),
            self.get_departure_time(),
            self.get_stop_id(),
            self.get_stop_sequence()
            )

    def __unicode__(self):
        return u"StopTime: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}".format(
            self.get_trip_id(),
            self.get_arrival_time(),
            self.get_departure_time(),
            self.get_stop_id(),
            self.get_stop_sequence(),
            self.get_pickup_type(),
            self.get_drop_off_type(),
            self.get_shape_dist_traveled()
            )


class Agency(GtfsObject):
    """ Represents an element in the agency dataset """
    def __init__(self, data_dict):
        super(Agency, self).__init__(AGENCY_KEYS, data_dict)

    def get_agency_name(self):
        return self.get(u"agency_name")

    def get_agency_url(self):
        return self.get(u"agency_url")

    def get_agency_timezone(self):
        return self.get(u"agency_timezone")

    def unique_id(self):
        """ Returns a unique key for this object.
            This is simply stop_id. """
        return self.get_agency_name()

    def __unicode__(self):
        return u"Agency: {0}, {1}, {2}".format(
            self.get_agency_name(),
            self.get_agency_url(),
            self.get_agency_timezone()
            )

class CalenderElement(GtfsObject):
    """ Represents an element in the calendar dataset """
    def __init__(self, data_dict):
        super(Agency, self).__init__(CALENDAR_KEYS, data_dict)
        raise NotImplementedError()


class CalenderDatesElement(GtfsObject):
    """ Represents an element in the calendar dates dataset """
    def __init__(self, data_dict):
        super(CalenderDatesElement, self).__init__(CALENDAR_DATES_KEYS, data_dict)
        raise NotImplementedError()


class Shape(GtfsObject):
    """ Represents an element in the shapes dataset """
    def __init__(self, data_dict):
        super(Shape, self).__init__(SHAPES_KEYS, data_dict)
        raise NotImplementedError()


