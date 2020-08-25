import gameball
gameball.api_key = "gb_test_..."
gameball.transaction_key = "gb_test_..."

balance_response = gameball.get_player_balance(player_unique_id= "player456")