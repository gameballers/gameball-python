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