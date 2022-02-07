from datetime import datetime
import gameball.utils

class orderObject(object):
    def __init__(
        self,
        player_unique_id,
        order_id,
        order_date,
        total_price,
        total_paid,
        total_shipping = None,
        total_tax = None, 
        total_discount = None,
        redeemed_amount = None,
        hold_reference = None,
        guest = False,
        line_items = [],
        discount_codes = [],
        extra = {},
        email = None,
        mobile = None
    ):

        self.player_unique_id = player_unique_id
        self.order_id = order_id
        self.order_date = order_date or gameball.utils.encode_date(datetime.utcnow()) 
        self.total_price = total_price 
        self.total_paid =total_paid 
        self.total_discount =total_discount 
        self.total_shipping =total_shipping 
        self.total_tax =total_tax 
        self.line_items =line_items 
        self.discount_codes =discount_codes 
        self.redeemed_amount =redeemed_amount 
        self.hold_reference =hold_reference 
        self.extra =extra 
        self.guest =guest 
        self.email =email 
        self.mobile =mobile
        self.source = 1

    def add_lineItem(self, line_Item):
        self.line_items.append({
            "productId": line_Item.product_id,
            "sku" : line_Item.product_id,
            "title" : line_Item.title,
            "category" : line_Item.category,
            "collection" : line_Item.collection, 
            "tags" : line_Item.tags,
            "weight" : line_Item.weight,
            "vendor" : line_Item.vendor, 
            "quantity" : line_Item.quantity
        })

    def add_extra_info(self, key, value):
        self.extra[key] = value

class lineItem(object):
    def __init__(
        self,
        product_id=None,
        sku=None,
        title=None,
        category=None,
        collection=None,
        tags=None,
        weight=None,
        vendor=None, 
        quantity=1
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