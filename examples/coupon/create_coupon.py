import gameball
gameball.api_key = "gb_test_..."
gameball.transaction_key = "gb_test_..."

coupon_request = gameball.couponObject(player_unique_id= 151515)
coupon_request.set_code(14736)
coupon_request.set_value(20.5)
coupon_response = gameball.create_discount_coupon(coupon_request)