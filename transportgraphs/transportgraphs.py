"""
transportgraphs:

Classes for working with sets of gtfs.models model objects.
"""
import gtfs.modelbuilder as builder
from gtfs.models import GtfsNames

class GtfsKnowledgeBase(object):
    """ Naive implementation """

    def __init__(self, provider, schema=None):
        self.modelbuilder = builder.GtfsModelBuilder(provider, schema)
        self.cache = {}

    def get_all_routes(self):
        """ Get all routes in the dataset"""
        self.cache_results(
            GtfsNames.ROUTES,
            self.modelbuilder.get_routes)
        return self.cache[GtfsNames.ROUTES]

    def get_all_trip_elements(self):
        """ Get all trip elements in the dataset """
        self.cache_results(
            GtfsNames.TRIPS,
            self.modelbuilder.get_trip_elements)
        return self.cache[GtfsNames.TRIPS]

    def get_route_by_name(self, name):
        """ Get the Route object corresponding to the
            given name or None. Argument 'name' should be
            a unicode string corresponding to the route's
            short name. """
        routes = self.get_all_routes()
        filtered = [x for x in routes if name == x.get_route_short_name()]

        if len(filtered) > 0:
            return filtered[0]
        return None

    def get_trip_elements_for_route(self, route):
        """ Get the Stop objects object corresponding to the
            given name or None """
        trip_elements = self.get_all_trip_elements()
        route_id = route.get_route_id()

        return [
            x for x in trip_elements if x.get_route_id() == route_id
            ]

    def cache_results(self, gtfs_name, function):
        """ Call the function passed in and cache the result at
            the given gtfs_name """
        if not self.cache.has_key(gtfs_name):
            self.cache[gtfs_name] = function()
