import gtfs.models as models
from gtfsprovider import GtfsProvider
from gtfs.schema

class GtfsModelBuilder(object):

    def __init__(self, provider, schema):
        self.provider = provider
        self.provider.set_schema(schema)

