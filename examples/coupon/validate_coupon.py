import gameball
gameball.api_key = "gb_test_..."
gameball.transaction_key = "gb_test_..."

coupon_validation_response = gameball.validate_discount_coupon(player_unique_id= 17315, code= 12347)
