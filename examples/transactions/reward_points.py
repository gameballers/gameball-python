# Example 1
import gameball
gameball.api_key = "gb_test_..."
gameball.transaction_key = "gb_test_..."

reward_request = gameball.rewardObject(player_unique_id= "player123", amount= 99.98, transaction_id= "tra_123456789")
reward_response = gameball.reward_points(reward_request)


# Example 2
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