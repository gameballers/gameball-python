import gameball
gameball.api_key = "gb_test_..."

player_request = gameball.playerObject(" player123")
player_request.add_player_attribute("displayName", " Jon Snow")
player_request.add_player_attribute("email", "jon.snow@example.com")
player_request.add_player_attribute("dateOfBirth", "1980-09-19T00:00:00.000Z")
player_request.add_player_attribute("joinDate", "2019-09-19T21:06:29.158Z")
player_response = gameball.initialize_player(player_request)