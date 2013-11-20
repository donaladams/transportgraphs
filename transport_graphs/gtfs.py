"""
gtfs.py:

Utility classes for loading General Transit Feed Specification (GTFS) data.

"""

AGENCY_FILE = "agency.txt"
CALENDAR_DATES_FILE = "calendar_dates.txt"
CALENDAR_FILE = "calendar.txt"
SHAPES_FILE = "shapes.txt"
STOPS_FILE = "stops.txt"
ROUTES_FILE = "routes.txt"
STOP_TIMES_FILE = "stop_times.txt"
TRIPS_FILE = "trips.txt"

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





