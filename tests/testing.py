# Gameball main object instantiation
import gameball
gameball.api_key = '7c7636658209418c9a82306a421f76a5'
gameball.transaction_key = '26e1967d89114388bdd1772587c336c8'


# generates random player_unique_id
import uuid
player_id = str(uuid.uuid4())


# initialize player
player_request = gameball.playerObject(player_unique_id= player_id)
player_request.add_player_attribute("displayName", "Python-v2")
player_request.add_player_attribute("age", 21)
player_request.add_player_attribute("gender", 'M')
player_request.add_custom_player_attribute("location", "Miami")
player_request.add_custom_player_attribute("graduationDate", "2022-07-04T21:06:29.158Z")
player_request.add_custom_player_attribute("isMarried", False)
player_response = gameball.initialize_player(player_request)
print(player_response)


# get player info in English
player_info_response = gameball.get_player_info(player_unique_id= player_id, language= gameball.Languages.English)
print(player_info_response)


# get player info in Arabic
player_info_response = gameball.get_player_info(player_unique_id= player_id, language= gameball.Languages.Arabic)
print(player_info_response)


# get player info without header
player_info_response = gameball.get_player_info(player_unique_id= player_id)
print(player_info_response)


# get the referral code from the response to be used later
referral_code = player_info_response['referralCode']


# send an event
event_request = gameball.eventObject(player_unique_id= player_id)
event_request.add_event("place_order",
    {"total_amount":100,
        "category":[
        "electronics",
        "cosmetics"]
    }
)
event_request.add_event("review")
event_request.add_event("reserve", {"rooms" : 2})
event_request.add_player_attribute("email", "jon.snow@example.com")
event_request.add_player_attribute("dateOfBirth", "1980-09-19T00:00:00.000Z")
event_request.add_player_attribute("joinDate", "2019-09-19T21:06:29.158Z")
event_request.add_custom_player_attribute("location", "Paris")
event_request.add_custom_player_attribute("graduationDate", "2018-07-04T21:06:29.158Z")
event_request.add_custom_player_attribute("isMarried", True)
send_event_response = gameball.send_event(event_request)
print(send_event_response)


# generates random player_unique_id for the referred player
referred_player_id = str(uuid.uuid4())


# create referral
referral_request = gameball.referralObject(player_code = referral_code, player_unique_id = referred_player_id)
referral_request.add_player_attribute("displayName", " Tyrion Lannister")
referral_request.add_player_attribute("firstName", "Tyrion")
referral_request.add_player_attribute("lastName", "Lannister")
referral_request.add_player_attribute("email", "tyrion@example.com")
referral_request.add_player_attribute("gender", "M")
referral_request.add_player_attribute("dateOfBirth", "1978-01-11T00:00:00.000Z")
referral_request.add_player_attribute("joinDate", "2019-09-19T21:06:29.158Z")
referral_request.add_custom_player_attribute("location", "Miami")
referral_request.add_custom_player_attribute("graduationDate", "2018-07-04T21:06:29.158Z")
referral_request.add_custom_player_attribute("isMarried", False)
referral_response = gameball.create_referral(referral_request)
print(referral_response)


# get the player balance
balance_response = gameball.get_player_balance(player_unique_id= player_id)
print(balance_response)


# hold points
hold_response = gameball.hold_points(player_unique_id= player_id, amount= 10)
print(hold_response)


# get the hold reference from the response to be used later
hold_reference = hold_response['holdReference']


# generates random transaction_id
transaction_id = str(uuid.uuid4())


# redeem points
redeem_response = gameball.redeem_points(player_unique_id= player_id, hold_reference= hold_reference, transaction_id= transaction_id)
print(redeem_response)


# get the transaction_id from the response to be used in reversing
transaction_to_reverse_id = redeem_response['transactionId']


# generates random transaction_id for the new transaction
new_transaction_id = str(uuid.uuid4())


# reverse transaction
reverse_transaction_response = gameball.reverse_transaction(player_unique_id= player_id, transaction_id= new_transaction_id, reversed_transaction_id= transaction_to_reverse_id)
print(reverse_transaction_response)


# hold points to reverse hold and then get the hold reference from the response to be reversed
hold_response = gameball.hold_points(player_unique_id= player_id, amount= 10)
hold_reference = hold_response['holdReference']


# reverse hold
reverse_hold_response = gameball.reverse_hold(player_unique_id= player_id, hold_reference= hold_reference)
print(reverse_hold_response)


# generates random transaction_id
transaction_id = str(uuid.uuid4())


#reward points
reward_request = gameball.rewardObject(player_unique_id= player_id, amount= 100, transaction_id= transaction_id)
reward_request.add_player_attribute("displayName", " Tyrion Lannister")
reward_request.add_player_attribute("firstName", "Tyrion")
reward_request.add_player_attribute("lastName", "Lannister")
reward_request.add_player_attribute("email", "tyrion@example.com")
reward_request.add_player_attribute("gender", "M")
reward_request.add_player_attribute("dateOfBirth", "1978-01-11T00:00:00.000Z")
reward_request.add_player_attribute("joinDate", "2019-09-19T21:06:29.158Z")
reward_request.add_custom_player_attribute("location", "Miami")
reward_request.add_custom_player_attribute("graduationDate", "2018-07-04T21:06:29.158Z")
reward_request.add_custom_player_attribute("isMarried", False)
reward_response = gameball.reward_points(reward_request)
print(reward_response)


# generates random transaction_id
transaction_id = str(uuid.uuid4())


# send an action
action_request = gameball.actionObject(player_unique_id = player_id)
action_request.add_player_attribute("displayName", "Python_v2")
action_request.add_player_attribute("name","Mohamad")
action_request.add_event("place_order", {"total_price":1500})
action_request.add_event("view_product_page")
action_request.add_points_transaction(transaction_id= transaction_id, reward_amount=20)
action_response = gameball.send_action(action_request)
print(action_response)


# create a coupon
coupon_request = gameball.couponObject(player_unique_id= player_id)
coupon_request.set_code(14736)
coupon_request.set_value(20.5)
coupon_response = gameball.create_discount_coupon(coupon_request)
print(coupon_response)


# get the coupon code to be used later
coupon_code = coupon_response['code']


# validate a coupon
coupon_validation_response = gameball.validate_discount_coupon(player_unique_id= player_id, code= coupon_code)
print(coupon_validation_response)


# redeem a coupon
coupon_redeemption_response = gameball.redeem_discount_coupon(player_unique_id= player_id, code= coupon_code)
print(coupon_redeemption_response)

#ALL passed
print("all test cases passed")
