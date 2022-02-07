class eventObject(object):
    def __init__(
        self,
        player_unique_id,
        events = {},
        email = None,
        mobile = None
    ):
        self.player_unique_id = player_unique_id
        self.events = events
        self.email = email
        self.mobile = mobile

    def add_event(self, event_name, event_metadata = {}):
        self.events[event_name] = event_metadata
