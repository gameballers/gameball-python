class rewardObject(object):
    def __init__(
        self,
        player_unique_id,
        amount,
        transaction_id,
        player_attributes = {}

    ):
        self.player_unique_id = player_unique_id
        self.amount = amount
        self.transaction_id = transaction_id
        self.player_attributes = player_attributes

    def add_player_attribute(self, attribute_name, value):
        self.player_attributes[attribute_name] = value
    
    def add_custom_player_attribute(self, attribute_name, value):
        custom_chk = self.player_attributes.get('custom', None)
        if custom_chk is None:
            self.player_attributes['custom'] = {}
        self.player_attributes['custom'][attribute_name] = value