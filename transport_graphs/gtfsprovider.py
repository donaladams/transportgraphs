""" """

import os
import utils.ucsv
from utils.decorators import CheckPathIsValid
import gtfs
from abc import ABCMeta, abstractmethod

class GtfsProvider(object):
    """ General interface for accessing GTFS. The load_X methods should
        return a list of dictionaries, with the field name as key and
        field value as value. """

    __metaclass__ = ABCMeta

    @abstractmethod
    def load_agency(self):
        pass

    @abstractmethod
    def load_calendar_dates(self):
        pass

    @abstractmethod
    def load_calendar(self):
        pass

    @abstractmethod
    def load_shapes(self):
        pass

    @abstractmethod
    def load_stops(self):
        pass

    @abstractmethod
    def load_routes(self):
        pass

    @abstractmethod
    def load_stop_times(self):
        pass

    @abstractmethod
    def load_trips(self):
        pass


@CheckPathIsValid
def read_csv(path):
    """ Reads a csv into a list. Throws ValueException if
        path is incorrect (done in decorator). """
    content = []
    with open(path, 'rb') as csvfile:
        dictreader = utils.ucsv.UnicodeDictReader(csvfile)
        for row in dictreader:
            content.append(row)

    return content


class GtfsProviderCsv(GtfsProvider):
    """ Implementation of GtfsProvier that reads the data
        from Csvs"""

    """ Standard names for GTFS files """
    AGENCY_FILE = "agency.txt"
    CALENDAR_DATES_FILE = "calendar_dates.txt"
    CALENDAR_FILE = "calendar.txt"
    SHAPES_FILE = "shapes.txt"
    STOPS_FILE = "stops.txt"
    ROUTES_FILE = "routes.txt"
    STOP_TIMES_FILE = "stop_times.txt"
    TRIPS_FILE = "trips.txt"

    def __init__(self, directory):
        self.directory = directory

    def load_agency(self):
        """ Loads agency file to a list. """
        return self.load_gtfs_file(self.directory, self.AGENCY_FILE)

    def load_calendar_dates(self):
        """ Loads calendar_dates file to a list. """
        return self.load_gtfs_file(self.directory, self.CALENDAR_DATES_FILE)

    def load_calendar(self):
        """ Loads calendar file to a list. """
        return self.load_gtfs_file(self.directory, self.CALENDAR_FILE)

    def load_shapes(self):
        """ Loads shapes file to a list. """
        return self.load_gtfs_file(self.directory, self.SHAPES_FILE)

    def load_stops(self):
        """ Loads stops file to a list. """
        return self.load_gtfs_file(self.directory, self.STOPS_FILE)

    def load_routes(self):
        """ Loads routes file to a list. """
        return self.load_gtfs_file(self.directory, self.ROUTES_FILE)

    def load_stop_times(self):
        """ Loads stop_times file to a list. """
        return self.load_gtfs_file(self.directory, self.STOP_TIMES_FILE)

    def load_trips(self):
        """ Loads trips file to a list. """
        return self.load_gtfs_file(self.directory, self.TRIPS_FILE)

    def load_gtfs_file(self, directory, filename):
        """ Loads a GTFS file into a list """
        try:
            filepath = os.path.join(self.directory, filename)
            return read_csv(filepath)
        except ValueError as value_error:
            print value_error
        except Exception as exeption:
            print exeption

        return None


class GtfsProviderSingleRowMock(GtfsProvider):
    """ Returns a single valid row of data. Doesn't need to go to
        filesystem """

    def load_agency(self):
        return [{
            u'agency_url': u'http://www.journeyplanner.transportforireland.ie',
            u'agency_name':
            u'Dublin Bus',
            u'agency_timezone': u'Europe/Dublin'}
            ]

    def load_calendar_dates(self):
        return [{
            u'date': u'20121225',
            u'service_id': u'1',
            u'exception_type': u'2'}
            ]

    def load_calendar(self):
        return [{
            u'end_date': u'20121231',
            u'monday': u'1',
            u'tuesday': u'1',
            u'friday': u'1',
            u'wednesday': u'1',
            u'thursday': u'1',
            u'start_date': u'20121118',
            u'sunday': u'0',
            u'service_id': u'1',
            u'saturday': u'0'}
            ]

    def load_shapes(self):
        return [{
            u'shape_pt_lat': u'53.3916142452115',
            u'shape_id': u'0-102-y12-1.85.O',
            u'shape_pt_lon': u'-6.11627088439508',
            u'shape_pt_sequence': u'1',
            u'shape_dist_traveled': u'0'}
            ]

    def load_stops(self):
        return [{
            u'stop_lat': u'53.3522439241978',
            u'stop_name': u'Parnell Square, Rotunda',
            u'stop_lon': u'-6.26369319257185',
            u'stop_id': u'8220DB000002'}
            ]

    def load_routes(self):
        return [{
            u'route_type': u'3',
            u'route_id': u'0-1-y12-1',
            u'route_short_name': u'1',
            u'route_long_name': u'Simmonscourt View - Shanard Avenue'}
            ]

    def load_stop_times(self):
        return [{
            u'pickup_type': u'0',
            u'shape_dist_traveled': u'0',
            u'arrival_time': u'16:15:00',
            u'stop_sequence': u'1',
            u'stop_id': u'8240DB003813',
            u'drop_off_type': u'0',
            u'trip_id': u'1.1714.0-33A-y12-1.155.I',
            u'departure_time': u'16:15:00'}
            ]

    def load_trips(self):
        return [{
            u'route_id': u'0-1-y12-1',
            u'direction_id': u'0',
            u'trip_headsign': u'Shanard Avenue - Simmonscourt View',
            u'service_id': u'1',
            u'shape_id': u'0-1-y12-1.1.O',
            u'trip_id': u'4777.2.0-1-y12-1.1.O'}
            ]









