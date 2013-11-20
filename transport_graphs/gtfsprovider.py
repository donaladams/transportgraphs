""" """

import os
import utils.ucsv
from utils.decorators import CheckPathIsValid
import gtfs
from abc import ABCMeta, abstractmethod

class GtfsProvider(object):
    """ General interface for accessing GTFS """

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











