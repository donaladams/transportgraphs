"""
gtfs.py:

Utility classes for loading General Transit Feed Specification (GTFS) data.

"""
import os
import utils.ucsv
from utils.decorators import CheckPathIsValid

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

@CheckPathIsValid
def read_csv(path):
    """ Reads a csv into a list. Throws ValueException if
        path is incorrect. """
    content = []
    with open(path, 'rb') as csvfile:
        dictreader = utils.ucsv.UnicodeDictReader(csvfile)
        for row in dictreader:
            content.append(row)

    return content

def load_gtfs_file(directory, filename):
    """ Loads a GTFS file into a list """
    try:
        filepath = os.path.join(directory, filename)
        return read_csv(filepath)
    except ValueError as value_error:
        print value_error

    except Exception as exeption:
        print exeption

    return None

def load_agency(directory):
    """ Loads agency file to a list. """
    return load_gtfs_file(directory, AGENCY_FILE)

def load_calendar_dates(directory):
    """ Loads calendar_dates file to a list. """
    return load_gtfs_file(directory, CALENDAR_DATES_FILE)

def load_calendar(directory):
    """ Loads calendar file to a list. """
    return load_gtfs_file(directory, CALENDAR_FILE)

def load_shapes(directory):
    """ Loads shapes file to a list. """
    return load_gtfs_file(directory, SHAPES_FILE)

def load_stops(directory):
    """ Loads stops file to a list. """
    return load_gtfs_file(directory, STOPS_FILE)

def load_routes(directory):
    """ Loads routes file to a list. """
    return load_gtfs_file(directory, ROUTES_FILE)

def load_stop_times(directory):
    """ Loads stop_times file to a list. """
    return load_gtfs_file(directory, STOP_TIMES_FILE)

def load_trips(directory):
    """ Loads trips file to a list. """
    return load_gtfs_file(directory, TRIPS_FILE)




