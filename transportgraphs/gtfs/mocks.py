

class GtfsSingleRowMock(object):
    """ Returns a single valid row of data for each
        gtfs object type
        """

    def agency(self):
        return [{
            u'agency_url': u'http://www.journeyplanner.transportforireland.ie',
            u'agency_name':
            u'Dublin Bus',
            u'agency_timezone': u'Europe/Dublin'}
            ]

    def calendar_dates(self):
        return [{
            u'date': u'20121225',
            u'service_id': u'1',
            u'exception_type': u'2'}
            ]

    def calendar(self):
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

    def shapes(self):
        return [{
            u'shape_pt_lat': u'53.3916142452115',
            u'shape_id': u'0-102-y12-1.85.O',
            u'shape_pt_lon': u'-6.11627088439508',
            u'shape_pt_sequence': u'1',
            u'shape_dist_traveled': u'0'}
            ]

    def stops(self):
        return [{
            u'stop_lat': u'53.3522439241978',
            u'stop_name': u'Parnell Square, Rotunda',
            u'stop_lon': u'-6.26369319257185',
            u'stop_id': u'8220DB000002'}
            ]

    def routes(self):
        return [{
            u'route_type': u'3',
            u'route_id': u'0-1-y12-1',
            u'route_short_name': u'1',
            u'route_long_name': u'Simmonscourt View - Shanard Avenue'}
            ]

    def stop_times(self):
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

    def trips(self):
        return [{
            u'route_id': u'0-1-y12-1',
            u'direction_id': u'0',
            u'trip_headsign': u'Shanard Avenue - Simmonscourt View',
            u'service_id': u'1',
            u'shape_id': u'0-1-y12-1.1.O',
            u'trip_id': u'4777.2.0-1-y12-1.1.O'}
            ]