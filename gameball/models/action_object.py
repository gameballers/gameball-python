from datetime import datetime
import gameball.utils

class actionObject(object):
    def __init__(
        self,
        player_unique_id,
        player_attributes = {},
        events = {},
        points_transaction= None        
    ):
        self.player_unique_id = player_unique_id
        self.player_attributes = player_attributes
        self.events = events
        self.points_transaction = points_transaction

    def add_player_attribute(self, attribute_name, value):
        self.player_attributes[attribute_name] = value

    def add_event(self, event_name, event_metadata = {}):
        self.events[event_name] = event_metadata
    
    def add_points_transaction(self, transaction_id, reward_amount = None, hold_reference = None):
        self.points_transaction = {}
        self.points_transaction["transactionId"] = transaction_id
        self.points_transaction["transactionTime"] = gameball.utils.encode_date(datetime.utcnow())
        self.points_transaction["hash"] = gameball.utils.hash_body(self.player_unique_id, datetime.utcnow().strftime("%y%m%d%H%M%S"))

        if reward_amount is not None:
            self.points_transaction["rewardAmount"] = reward_amount
            self.points_transaction["hash"] = gameball.utils.hash_body(self.player_unique_id, datetime.utcnow().strftime("%y%m%d%H%M%S"), reward_amount)

        if hold_reference is not None:
            self.points_transaction["holdReference"] = hold_reference


