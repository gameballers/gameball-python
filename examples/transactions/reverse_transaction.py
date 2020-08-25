import gameball
gameball.api_key = "gb_test_..."
gameball.transaction_key = "gb_test_..."

reverse_transaction_response = gameball.reverse_transaction(player_unique_id= "player456",transaction_id= "1234567890",reversed_transaction_id= '234567891')