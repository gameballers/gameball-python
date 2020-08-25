class couponObject(object):
    def __init__(
        self,
        player_unique_id,
        code = None,
        start_at = None,
        ends_at = None,
        entitled_collection_ids = {},
        entitled_product_ids = {},
        once_per_customer = None,
        prerequisite_quantity_range = None,
        prerequisite_shipping_price_range = None,
        prerequisite_subtotal_range = None,
        prerequisite_collection_ids = {},
        prerequisite_product_ids = {},
        usage_limit = None,
        Value = None,
        value_type = None,
        cap = None
    ):
        self.player_unique_id = player_unique_id
        self.code = code
        self.start_at = start_at
        self.ends_at = ends_at
        self.entitled_collection_ids = entitled_collection_ids
        self.entitled_product_ids = entitled_product_ids
        self.once_per_customer = once_per_customer
        self.prerequisite_quantity_range = prerequisite_quantity_range
        self.prerequisite_shipping_price_range = prerequisite_shipping_price_range
        self.prerequisite_subtotal_range = prerequisite_subtotal_range
        self.prerequisite_collection_ids = prerequisite_collection_ids
        self.prerequisite_product_ids = prerequisite_product_ids
        self.usage_limit = usage_limit
        self.Value = Value
        self.value_type = value_type
        self.cap = cap


    def set_code(self, code):
        self.code = code
    

    def set_start_time(self, start_time):
        self.start_at = start_time


    def set_end_time(self, end_time):
        self.ends_at = end_time


    def set_usage_limit(self, usage_limit):
        self.usage_limit = usage_limit


    def set_value(self, value):
        self.value = value
    

    def set_value_type(self, value_type):
        self.value_type = value_type


    def set_cap(self, cap):
        self.cap = cap