from gameball.exceptions.gameball_exception import GameballException
from datetime import datetime
import gameball.utils

class playerObject(object):
    def __init__(
        self,
        player_unique_id,
        player_attributes = {},
    ):
        if len(str(player_unique_id)) < 1 or len(str(player_unique_id)) > 50:
            raise GameballException('player_unique_id should be between 1 and 50 letters')
        else:
            self.player_unique_id = player_unique_id
            
        self.player_attributes = player_attributes
    
    def add_player_attribute(self, attribute_name, value):
        self.player_attributes[attribute_name] = value
    
    def add_custom_player_attribute(self, attribute_name, value):
        custom_chk = self.player_attributes.get('custom', None)
        if custom_chk is None:
            self.player_attributes['custom'] = {}
        self.player_attributes['custom'][attribute_name] = value
