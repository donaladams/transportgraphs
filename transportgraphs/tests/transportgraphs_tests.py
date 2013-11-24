import os
import transportgraphs.transportgraphs as tg
from gtfs.schema import GtfsCsvSchema
import gtfs.models as models
from gtfs.gtfsprovider import GtfsProviderCsv

DATA_DIRECTORY = os.path.join(os.path.abspath(os.curdir), "tests/test_data")

class TestGtfsKnowledgeBase(object):

    def test_get_all_routes(self):
        """ Should return a list of valid models.Route objects """
        schema = GtfsCsvSchema()
        provider = GtfsProviderCsv(DATA_DIRECTORY)
        kbase = tg.GtfsKnowledgeBase(provider, schema)
        routes = kbase.get_all_routes()

        assert all([type(x) == models.Route for x in routes])
        assert all([x.is_valid() for x in routes])

    def test_get_existing_route_by_name_(self):
        """ Should retrieve the 54A route. Route details:
            "0-54A-y12-1","54A","Marlfield - Garda Station","3" """
        schema = GtfsCsvSchema()
        provider = GtfsProviderCsv(DATA_DIRECTORY)
        kbase = tg.GtfsKnowledgeBase(provider, schema)

        route = kbase.get_route_by_name(u"54A")

        assert route is not None
        assert route.get_route_short_name() == u"54A"
        assert route.get_route_id() == u"0-54A-y12-1"

    def test_get_false_route_by_name(self):
        """ Should return None as route name does not exist """
        schema = GtfsCsvSchema()
        provider = GtfsProviderCsv(DATA_DIRECTORY)
        kbase = tg.GtfsKnowledgeBase(provider, schema)
        route = kbase.get_route_by_name(u"ABCDEF")

        assert route is None

    def test_get_trip_elements_for_route(self):
        """ Should retrieve the 54A route. Route details:
            "0-54A-y12-1","54A","Marlfield - Garda Station","3" """
        schema = GtfsCsvSchema()
        provider = GtfsProviderCsv(DATA_DIRECTORY)
        kbase = tg.GtfsKnowledgeBase(provider, schema)

        route_name = u"54A"
        # Get the Route object for the route we want
        route = kbase.get_route_by_name(route_name)
        assert type(route) == models.Route

        # Get the trip elements
        trip_elements = kbase.get_trip_elements_for_route(route)
        assert bool(trip_elements)
        assert all(
            [type(t) == models.TripElement for t in trip_elements]
            )
        assert all(
            [t.is_valid() for t in trip_elements]
            )
        assert all(
            [t.get_route_id()==route.get_route_id() for t in trip_elements]
            )












