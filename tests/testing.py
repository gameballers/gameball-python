# Gameball main object instantiation

# If the module isn't in the same directory:
import json


import gameball

# import gameball
gameball.api_key = "API_KEY"
gameball.transaction_key = "TRANSACTION_KEY"

# generates random player_unique_id
import uuid
player_id = "5621841723580"

# Initialize Player
player_request = gameball.playerObject("python_user_04", 
    player_attributes = gameball.playerAttributes(
        "Andy Robertson",
        "Andy",
        "Robertson",
        "01123023916",
        "andy_001@example.com",
        "M",
        "1996-09-19T00:00:00.000Z",
        "2021-10-19T00:00:00.000Z"
    ),
    referrer_code="4C321990EeRQD-"
)
player_response = gameball.initialize_player(player_request)
print(player_response)


# send an order
order_id = str(uuid.uuid4())
product_id = str(uuid.uuid4())
order_request = gameball.orderObject(
        player_unique_id = player_id,
        order_id = order_id,
        order_date = '',
        total_price = 70,
        total_paid = 70,
        total_discount = 0, 
        total_shipping = 0,
        total_tax = 0,
        redeemed_amount = None,
        hold_reference = None,
        guest = False,
        discount_codes = [],
        extra = {}       
    )

line_item = gameball.lineItem(
        product_id = product_id,
        sku = product_id,
        title = "T-shirt",
        category = ["Summer Collection"],
        collection = ["Summer Collection"], 
        tags = ["Summer Collection"],
        weight = 93.5,
        vendor = "Zara", 
        quantity = 1
    )

order = gameball.orderObject("python_user_04", "order_python_06",None,200,200)

order.add_lineItem(line_item)
order_response = gameball.send_order(order_request)
print(order_response)

# reward player
reward = gameball.rewardObject("python_user_04",400,"python_trans_01")
print(reward)

# batch balance request
batch_request = gameball.batchObject('POST', 'balance',
    None,
    {"playerUniqueIds": ["python_user_04","python_user_03"]}
)

# delete batch
batch_request = gameball.delete_batch("3237832")
print(batch_request)


# send event
event = gameball.eventObject("python_user_04")
event.add_event(
    'place_order', {
        "product_id": "product_01",
        "total_paid": 200
    })
event_request = gameball.send_event(event)
print(event_request)


# attach tags
player_response = gameball.attach_tags("python_user_01", "VIP,Platinum")
print(player_response)

# detach tags
player_response = gameball.detach_tags("python_user_01", "Platinum")
print(player_response)


# get leaderboard
leaderboard = gameball.leaderboard(player_unique_id="python_user_04")
print(leaderboard)