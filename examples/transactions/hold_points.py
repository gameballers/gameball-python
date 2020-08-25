import gameball
gameball.api_key = "gb_test_..."
gameball.transaction_key = "gb_test_..."

hold_response = gameball.hold_points(player_unique_id= "player456", amount= 98.89)