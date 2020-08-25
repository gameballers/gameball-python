import gameball
gameball.api_key = "gb_test_..."
gameball.transaction_key = "gb_test_..."

redeem_response = gameball.redeem_points(player_unique_id= "player456", hold_reference= "2342452352435234", transaction_id= "tra_123456789")