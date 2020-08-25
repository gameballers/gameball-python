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