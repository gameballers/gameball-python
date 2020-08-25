# **Gameball Python SDK**
---
The Gameball Python SDK provides convinient access to the Gameball API frpm applicatopns written in the Python langauage. 
## Documentation
---
Please refer to the  [Gameball API docs](https://docs.gameball.co).
## Installation
---
You don't need this source code unless you want to modify the SDK. If you just
want to use the SDK, just run:
```py
pip install gameball
```
### Requirements
-   Python 3.4+ (PyPy supported)
-   Requests library 2.20 and later
## Usage
---
The SDK needs to be configured with your account's API & Transaction keys available in your [Gameball Dashboard](https://help.gameball.co/en/articles/3467114-get-your-account-integration-details-api-key-and-transaction-key)

```py
import gameball
gameball.api_key = "gb_test_..."
gameball.transaction_key = "gb_test_..."
```

### Commands:
```py
# creates a new player with the given player attributes.
gameball.initialize_player(player)

# performs action based on event triggered by users.
gameball.send_event(event)

# refers a new user through player with the given player code.
gameball.create_referral(referral)

# obtains player's balance value.
gameball.get_player_balance(player_unique_id)

# holds a specific amount of points from the player’s points balance. 
gameball.hold_points(player_unique_id, amount, transaction_time)

# enables the player to use Gameball points as a payment method since it can be substituted for monetary values.
gameball.redeem_points(player_unique_id, amount, transaction_time, hold_reference, transaction_on_client_system_id) 

# cancels a purchase reward or refund a points redemption transactions in Gameball.
gameball.reverse_transaction(player_unique_id, transaction_time, transaction_on_client_system_id, reversed_transaction_on_client_system_id)

# cancels previously held points identified by the given hold reference.
gameball.reverse_hold(player_unique_id, hold_reference, transaction_time) 

# rewards a player with points equivalent to the given amount.
gameball.reward_points(player_unique_id, amount, transaction_time, transaction_on_client_system_id, player_attributes = {})

# obtains player's information.
gameball.get_player_info(player_unique_id, lannguage= None)

# performs action based on event triggered by users or transactions.
gameball.send_action(action)

# create discount coupon to a specific user
gameball.create_discount_coupon(coupon)

# redeems discount coupon by a specific user
gameball.redeem_discount_coupon(player_unique_id, code, transaction_time)

# validates discount coupon by a specific user
gameball.validate_discount_coupon(player_unique_id, code, transaction_time)
```
### Examples
#### Sending an Event Example
```py
# Example 1
import gameball
gameball.api_key = "gb_test_..."

event_request = gameball.eventObject(player_unique_id= "player123")
event_request.add_event("place_order",
    {"total_amount":100,
        "category":[
        "electronics",
        "cosmetics"]
    }
)
event_request.add_event("review")
send_event_response = gameball.send_event(event_request)


# Example 2
import gameball
gameball.api_key = "gb_test_..."

event_request = gameball.eventObject(player_unique_id= " player123")
event_request.add_event("reserve", {"rooms" : 2})
event_request.add_player_attribute("displayName", " Jon Snow")
event_request.add_player_attribute("email", "jon.snow@example.com")
event_request.add_player_attribute("dateOfBirth", "1980-09-19T00:00:00.000Z")
event_request.add_player_attribute("joinDate","2019-09-19T21:06:29.158Z")
send_event_response = gameball.send_event(event_request)


# Example 3
import gameball
gameball.api_key = "gb_test_..."

event_request = gameball.eventObject(player_unique_id= " player123")
event_request.add_event("reserve", {"rooms" : 2})
event_request.add_player_attribute("displayName", " Jon Snow")
event_request.add_player_attribute("email", "jon.snow@example.com")
event_request.add_player_attribute("dateOfBirth", "1980-09-19T00:00:00.000Z")
event_request.add_player_attribute("joinDate", "2019-09-19T21:06:29.158Z")
event_request.add_custom_player_attribute("location", "Miami")
event_request.add_custom_player_attribute("graduationDate", "2018-07-04T21:06:29.158Z")
event_request.add_custom_player_attribute("isMarried", False)
send_event_response = gameball.send_event(event_request)
```
#### Create a Referral Example
```py
# Example 1
import gameball
gameball.api_key = "gb_test_..."

referral_request = gameball.referralObject(player_code = "CODE11", player_unique_id = "player456")
referral_response = gameball.create_referral(referral_request)


# Example 2
import gameball
gameball.api_key = "gb_test_..."

referral_request = gameball.referralObject(player_code = "CODE11", player_unique_id = "player456")
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
```
#### Reward Examples
```py
#Example 1
import gameball
gameball.api_key = "gb_test_..."
gameball.transaction_key = "gb_test_..."

reward_request = gameball.rewardObject(player_unique_id= "player123", amount= 99.98, transaction_id= "tra_123456789")
reward_response = gameball.reward_points(reward_request)


#Example 2
import gameball
gameball.api_key = "gb_test_..."
gameball.transaction_key = "gb_test_..."

reward_request = gameball.rewardObject(player_unique_id= "player456", amount= 2500, transaction_id= "tra_123456789")
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
```
#### Get Player Balance Example 
```py
import gameball
gameball.api_key = "gb_test_..."
gameball.transaction_key = "gb_test_..."

balance_response = gameball.get_player_balance(player_unique_id= "player456")
```
#### Hold Points Example 
```py
import gameball
gameball.api_key = "gb_test_..."
gameball.transaction_key = "gb_test_..."

hold_response = gameball.hold_points(player_unique_id= "player456", amount= 98.89)
```
#### Redeem Example 
```py
import gameball
gameball.api_key = "gb_test_..."
gameball.transaction_key = "gb_test_..."

redeem_response = gameball.redeem_points(player_unique_id= "player456",
                                        hold_reference= "2342452352435234", transaction_id= "tra_123456789")

```
#### Reverse Transaction Example
```py
import gameball
gameball.api_key = "gb_test_..."
gameball.transaction_key = "gb_test_..."

reverse_transaction_response = gameball.reverse_transaction(player_unique_id= "player456",transaction_id= "1234567890",
                                                            reversed_transaction_id= '234567891')
```
#### Reverse Hold Example
```py
import gameball
gameball.api_key = "gb_test_..."
gameball.transaction_key = "gb_test_..."

reverse_hold_response = gameball.reverse_hold(player_unique_id= "player456", hold_reference= "9245fe4a-d402-451c-b9ed-9c1a04247482")
```
#### Sending an Action Example
```py
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
```
#### Get Player Info Example
```py
# Example 1
import gameball
gameball.api_key = "gb_test_..."
gameball.transaction_key = "gb_test_..."

player_info_response = gameball.get_player_info(player_unique_id= 17315)


# Example 2
import gameball
gameball.api_key = "gb_test_..."
gameball.transaction_key = "gb_test_..."

player_info_response = gameball.get_player_info(player_unique_id= 17315, language= gameball.Languages.Arabic)

```
#### Initialize Player Example
```py
import gameball
gameball.api_key = "gb_test_..."

player_request = gameball.playerObject(" player123")
player_request.add_player_attribute("displayName", " Jon Snow")
player_request.add_player_attribute("email", "jon.snow@example.com")
player_request.add_player_attribute("dateOfBirth", "1980-09-19T00:00:00.000Z")
player_request.add_player_attribute("joinDate", "2019-09-19T21:06:29.158Z")
player_response = gameball.initialize_player(player_request)
```

### Handling exceptions
Unsuccessful requests raise exceptions. The raised exception will reflect the sort of error that occurred with appropriate message and error code . Please refer to the  [Gameball API docs](https://docs.gameball.co).
## Contribution
---
The master branch of this repository contains the latest stable release of the SDK.
## Contact
---
For usage questions\suggestions drop us an email at support[ at ]gameball.co. Please report any bugs as issues.