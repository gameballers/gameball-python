from gameball.api_requestor import APIRequestor
from gameball.models.order_object import orderObject
from gameball.models.order_object import lineItem
import gameball.constants
import gameball.utils

def send_order(order):
    api_requestor_instance = APIRequestor()

    body = {
        "playerUniqueId": order.player_unique_id,
        "orderId": order.order_id,
        "orderDate": order.order_date,
        "totalPrice" :  order.total_price,
        "totalPaid" : order.total_paid,
        "totalDiscount" : order.total_discount,
        "totalShipping" : order.total_shipping,
        "totalTax" : order.total_tax,
        "lineItems" : order.line_items,
        "discountCodes" : order.discount_codes,
        "redeemedAmount" : order.redeemed_amount,
        "holdReference" : order.hold_reference,
        "extra" : order.extra,
        "guest" : order.guest,
        "source" : order.source
    }

    body = gameball.utils.handle_channel_merging(body, order.email, order.mobile)

    response = api_requestor_instance.request(method='POST',url=gameball.constants.order, params = body)
    return response