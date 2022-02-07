from gameball.exceptions.gameball_exception import GameballException
from datetime import datetime
import gameball.utils

class playerObject(object):
    def __init__(
        self,
        player_unique_id,
        player_attributes,
        email = None,
        mobile = None,
        referrer_code = None,
        level_order = None
    ):
        if len(str(player_unique_id)) < 1 or len(str(player_unique_id)) > 50:
            raise GameballException('player_unique_id should be between 1 and 50 letters')
        else:
            self.player_unique_id = player_unique_id
        
        if player_attributes is None:
            self.player_attributes = playerAttributes()
            
        self.player_attributes = player_attributes
        self.email = email
        self.mobile = mobile
        self.referrer_code = referrer_code
        self.level_order = level_order

    
    def add_player_attribute(self, attribute_name, value):
        self.player_attributes[attribute_name] = value
    
    def add_custom_player_attribute(self, attribute_name, value):
        custom_chk = self.player_attributes.get('custom', None)
        if custom_chk is None:
            self.player_attributes['custom'] = {}
        self.player_attributes['custom'][attribute_name] = value

class playerAttributes(object):
    def __init__(
        self,
        display_name = None,
        first_name = None,
        last_name = None,
        mobile = None,
        email = None,
        gender = None,
        date_of_birth = None,
        join_date = None,
        tags = None,
    	custom = None
    ):
        self.displayName = display_name
        self.firstName = first_name
        self.lastName = last_name 
        self.mobile = mobile 
        self.email = email
        self.gender = gender
        self.lastName = last_name
        self.dateOfBirth = date_of_birth
        self.joinDate = join_date
        self.tags = tags
        self.custom = custom
        

    def add_custom_attribute(self, key, value):
        self.custom[key] = value