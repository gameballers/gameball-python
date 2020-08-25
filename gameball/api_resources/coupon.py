from gameball.api_requestor import APIRequestor
import gameball.constants
import gameball.utils
from gameball.models.coupon_object import couponObject
from datetime import datetime


def create_discount_coupon(coupon):
    api_requestor_instance = APIRequestor()
    body_hashed = gameball.utils.hash_body(coupon.player_unique_id)

    body={
    "playerUniqueId": coupon.player_unique_id,
    "transactionTime":gameball.utils.encode_date(datetime.utcnow()),
    "hash": body_hashed
    }

    if coupon.code is not None:
        body["code"] = coupon.code

    if coupon.start_at is not None:
        body["startAt"] = coupon.start_at

    if coupon.ends_at is not None:
        body["endsAt"] = coupon.ends_at

    if coupon.usage_limit is not None:
        body["usageLimit"] = coupon.usage_limit

    if coupon.value is not None:
        body["value"] = coupon.value

    if coupon.value_type is not None:
        body["valueType"] = coupon.value_type

    if coupon.cap is not None:
        body["cap"] = coupon.cap

    response = api_requestor_instance.request(method='POST',url=gameball.constants.create_coupon, params = body)
    return response


def redeem_discount_coupon(player_unique_id, code):
    api_requestor_instance = APIRequestor()
    
    body_hashed = gameball.utils.hash_body(player_unique_id)

    body={
    "playerUniqueId": player_unique_id,
    "code": code,
    "transactionTime":gameball.utils.encode_date(datetime.utcnow()),
    "hash": body_hashed
    }
    response = api_requestor_instance.request(method='POST',url=gameball.constants.redeem_coupon, params = body)
    return response


def validate_discount_coupon(player_unique_id, code):
    api_requestor_instance = APIRequestor()
    
    body_hashed = gameball.utils.hash_body(player_unique_id)

    body={
    "playerUniqueId": player_unique_id,
    "code": code,
    "transactionTime":gameball.utils.encode_date(datetime.utcnow()),
    "hash": body_hashed
    }
    response = api_requestor_instance.request(method='POST',url=gameball.constants.validate_coupon, params = body)
    return response

