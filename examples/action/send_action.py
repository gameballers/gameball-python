# Example 1
import gameball
gameball.api_key = "gb_test_..."
gameball.transaction_key = "gb_test_..."

action_request = gameball.actionObject(player_unique_id= "151515")
action_request.add_player_attribute("displayName", "Python_v2")
action_request.add_player_attribute("name","Mohamad")
action_request.add_points_transaction(transaction_id= "810008204529", reward_amount= 20)
action_response = gameball.send_action(action_request)


# Example 2
import gameball
gameball.api_key = "gb_test_..."
gameball.transaction_key = "gb_test_..."

action_request = gameball.actionObject(player_unique_id = "151515")
action_request.add_event("place_order", {"total_price":1500})
action_request.add_event("view_product_page")
action_request.add_points_transaction(transaction_id= "810008204529", hold_reference="1f306d48-706d-4e26-aeac-b3718ae7e5e2")
action_response = gameball.send_action(action_request)


# Example 3
import gameball
gameball.api_key = "gb_test_..."
gameball.transaction_key = "gb_test_..."

action_request = gameball.actionObject(player_unique_id = "151515")
action_request.add_player_attribute("displayName", "Python_v2")
action_request.add_player_attribute("name","Mohamad")
action_request.add_event("place_order", {"total_price":1500})
action_request.add_event("view_product_page")
action_request.add_points_transaction(transaction_id= "810008204529", reward_amount=20, hold_reference="1f306d48-706d-b3718ae7e5e2")
action_response = gameball.send_action(action_request)