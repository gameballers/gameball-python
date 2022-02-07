from datetime import datetime
import gameball.utils

class playerAttributes(object):
    def __init__(
        self,
        display_name,
        first_name,
        last_name,
        mobile,
        email,
        gender,
        date_of_birth,
        join_date,
        tags,
    	custom = {}
    ):

        self.display_name = display_name
        self.first_name = first_name
        self.last_name = last_name 
        self.mobile = mobile 
        self.email = email 
        self.gender =gender 
        self.date_of_birth =date_of_birth 
        self.join_date = join_date 
        self.tags = tags 
        self.custom = custom 

    def add_custom_attribute(self, key, value):
        self.custom[key] = value

    def add_extra_info(self, key, value):
        self.extra[key] = value

class lineItem(object):
    def __init__(
        self,
        product_id,
        sku,
        title,
        category,
        collection,
        tags,
        weight,
        vendor, 
        quantity
    ):

        self.product_id = product_id
        self.sku = sku
        self.title = title
        self.category = category 
        self.collection =collection 
        self.tags =tags 
        self.weight =weight 
        self.vendor =vendor 
        self.quantity =quantity