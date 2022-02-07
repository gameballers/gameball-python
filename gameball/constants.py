from __future__ import absolute_import, division, print_function
import enum

# Configuration variables

api_key = None
transaction_key = None
default_http_client = None
api_base = "https://api.gameball.co/api/v3.0/"
test_api_base = "https://api.dev.gameball.app/api/v3.0/"

events = 'integrations/event'
referral = 'integrations/referral'
order = 'integrations/order'
reward_points = 'integrations/transaction/cashback'
player_points_balance = 'integrations/transaction/balance'
hold_Points = 'integrations/transaction/hold'
redeem_points = 'integrations/transaction/redeem'
refund_transaction = 'integrations/transaction/refund'
manual_transaction = 'integrations/transaction/manual'
list_transactions = 'integrations/transaction/list'
leaderboard = 'integrations/leaderboard'
reverse_hold = 'integrations/transaction/hold/{hold_reference}'
player_notifications = 'integrations/notifications/{player_unique_id}'
mark_notifications = 'integrations/notifications'
config = 'integrations/config'
create_player = 'integrations/player'
player_info = 'integrations/player/{player_unique_id}'
player_balance = 'integrations/player/{player_unique_id}/balance'
player_progress = 'integrations/player/{player_unique_id}/progress'
player_tags = 'integrations/player/{player_unique_id}/tags'
player_tags = 'integrations/player/{player_unique_id}/tags'
start_batch = 'integrations/batch'
get_batch = 'integrations/batch/{batch_id}'
delete_batch = 'integrations/batch/{batch_id}'
create_coupon = 'integrations/coupon'
validate_coupon = 'integrations/coupon/validate'
redeem_coupon = 'integrations/coupon/redeem'
send_action = 'integrations/action'


class Languages(enum.Enum):
   English = 'en'
   Italian = 'it'
   Polish = 'pl'
   Portuguese = 'pt'
   German = 'de'
   Spanish = 'es'
   French = 'fr'
   Arabic = 'ar'
