from __future__ import absolute_import, division, print_function

import os

from gameball.api_resources.transactions import get_player_balance, reverse_transaction, reverse_hold
from gameball.api_resources.transactions import hold_points, redeem_points, reward_points, rewardObject
from gameball.api_resources.events import send_event, eventObject
from gameball.api_resources.player import initialize_player, playerObject, get_player_info
from gameball.api_resources.referral import create_referral, referralObject
from gameball.api_resources.coupon import create_discount_coupon, redeem_discount_coupon, validate_discount_coupon, couponObject
from gameball.api_resources.action import send_action, actionObject
from constants import Languages

from datetime import datetime

# Gameball Python bindings
# API docs at https://docs.gameball.co/
# Authors:
# Mohamad Elshimy <mohamedwaelelshimy@gmail.com>
# --------------- <---------------------------->

# Configuration variables

api_key = None
transaction_key = None
default_http_client = None


# Sets some basic information about the running application that's sent along
# with API requests. Useful for plugin authors to identify their plugin when
# communicating with Gameball.
#
# Takes a name and optional version and plugin URL.
# Not Operational yet
def set_app_info(name, partner_id=None, url=None, version=None):
    global app_info
    app_info = {
        "name": name,
        "partner_id": partner_id,
        "url": url,
        "version": version,
    }
