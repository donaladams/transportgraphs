"""
modelbuilder:

Contains class for providing instances of GtfsObject.
"""

import gtfs.models as models

class GtfsModelBuilder(object):
    """ Returns sets of GtfsObjects corresponding from
        the dataset used by the injected GtfsProvider. """

    def __init__(self, provider, schema=None):
        self.provider = provider
        if schema is not None:
            self.provider.set_schema(schema)

    def get_agencies(self):
        """ Returns Agency object for
            each of the Agencies given by the provider """
        data = self.provider.load_agency()
        return [models.Agency(x) for x in data]

    def get_calendar_dates_elements(self):
        """ Returns CalenderDatesElement object for
            each of the CalenderDates given by the provider """
        data = self.provider.load_calendar_dates()
        return [
            models.CalendarDatesElement(x) for x in data
            ]

    def get_calendar_elements(self):
        """ Returns CalenderElement object for
            each of the Calender elements given by the provider """
        data = self.provider.load_calendar()
        return [models.CalendarElement(x) for x in data]

    def get_shape_elements(self):
        """ Returns Shape object for
            each of the Shapes given by the provider """
        data = self.provider.load_shapes()
        return [models.ShapeElement(x) for x in data]

    def get_stops(self):
        """ Returns Stop class for
            each of the Stops given by the provider """
        data = self.provider.load_stops()
        return [models.Stop(x) for x in data]

    def get_routes(self):
        """ Returns Route class for
            each of the Routes given by the provider """
        data = self.provider.load_routes()
        return [models.Route(x) for x in data]

    def get_stop_times(self):
        """ Returns StopTime class for
            each of the Stop Times given by the provider """
        data = self.provider.load_stop_times()
        return [models.StopTime(x) for x in data]

    def get_trip_elements(self):
        """ Returns Trip class for
            each of the Trip elements given by the provider """
        data = self.provider.load_trips()
        return [models.TripElement(x) for x in data]

