import gameball
gameball.api_key = "gb_test_..."
gameball.transaction_key = "gb_test_..."

# Example 1
player_info_response = gameball.get_player_info(player_unique_id= 17315)


# Example 2
player_info_response = gameball.get_player_info(player_unique_id= 17315, language= gameball.Languages.Arabic)
