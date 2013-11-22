""" """

import os
import utils.ucsv
from utils.decorators import CheckPathIsValid
from abc import ABCMeta, abstractmethod
from gtfs.schema import GtfsSchema
from gtfs.models import GtfsNames
import gtfs.mocks as mocks

class GtfsProvider(object):
    """ General interface for accessing GTFS. The load_X methods should
        return a list of dictionaries, with the field name as key and
        field value as value. """

    __metaclass__ = ABCMeta

    def __init__(self, schema=None):
        if schema is not None:
            self.schema = schema
        else:
            self.schema = None

        self.requires_schema = True

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

    def set_schema(self, schema):
        self.schema = schema

    def apply_schema(self, gtfs_name, data):
        """ Processes data with schema. If schema not required, returns data as is.
            Otherwise, RuntimeError is thrown. """
        if self.schema is not None:
            return self.schema.apply(gtfs_name, data)
        elif self.requires_schema:
            raise RuntimeError("Must supply a schema when requires_schema set to True")
        else:
            return data


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

    def __init__(self, directory, schema=None):
        super(GtfsProviderCsv, self).__init__(schema)
        self.directory = directory

    def load_agency(self):
        """ Loads agency file to a list. """
        data = self.load_gtfs_file(self.directory, self.AGENCY_FILE)
        return self.apply_schema(GtfsNames.AGENCY, data)

    def load_calendar_dates(self):
        """ Loads calendar_dates file to a list. """
        data = self.load_gtfs_file(self.directory, self.CALENDAR_DATES_FILE)
        return self.apply_schema(GtfsNames.CALENDAR_DATES, data)

    def load_calendar(self):
        """ Loads calendar file to a list. """
        data = self.load_gtfs_file(self.directory, self.CALENDAR_FILE)
        return self.apply_schema(GtfsNames.CALENDAR, data)

    def load_shapes(self):
        """ Loads shapes file to a list. """
        data = self.load_gtfs_file(self.directory, self.SHAPES_FILE)
        return self.apply_schema(GtfsNames.SHAPES, data)

    def load_stops(self):
        """ Loads stops file to a list. """
        data = self.load_gtfs_file(self.directory, self.STOPS_FILE)
        return self.apply_schema(GtfsNames.STOPS, data)

    def load_routes(self):
        """ Loads routes file to a list. """
        data = self.load_gtfs_file(self.directory, self.ROUTES_FILE)
        return self.apply_schema(GtfsNames.ROUTES, data)

    def load_stop_times(self):
        """ Loads stop_times file to a list. """
        data = self.load_gtfs_file(self.directory, self.STOP_TIMES_FILE)
        return self.apply_schema(GtfsNames.STOP_TIMES, data)

    def load_trips(self):
        """ Loads trips file to a list. """
        data = self.load_gtfs_file(self.directory, self.TRIPS_FILE)
        return self.apply_schema(GtfsNames.TRIPS, data)

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
        data = mocks.GtfsSingleRowMock().agency()
        return self.apply_schema(GtfsNames.AGENCY, data)

    def load_calendar_dates(self):
        data = mocks.GtfsSingleRowMock().calendar_dates()
        return self.apply_schema(GtfsNames.CALENDAR_DATES, data)

    def load_calendar(self):
        data = mocks.GtfsSingleRowMock().calendar()
        return self.apply_schema(GtfsNames.CALENDAR, data)

    def load_shapes(self):
        data = mocks.GtfsSingleRowMock().shapes()
        return self.apply_schema(GtfsNames.SHAPES, data)

    def load_stops(self):
        data = mocks.GtfsSingleRowMock().stops()
        return self.apply_schema(GtfsNames.STOPS, data)

    def load_routes(self):
        data = mocks.GtfsSingleRowMock().routes()
        return self.apply_schema(GtfsNames.ROUTES, data)

    def load_stop_times(self):
        data = mocks.GtfsSingleRowMock().stop_times()
        return self.apply_schema(GtfsNames.STOP_TIMES, data)

    def load_trips(self):
        data = mocks.GtfsSingleRowMock().trips()
        return self.apply_schema(GtfsNames.TRIPS, data)









