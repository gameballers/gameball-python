class rewardObject(object):
    def __init__(
        self,
        player_unique_id,
        amount,
        transaction_id,
        merchant = None,
        email = None,
        mobile = None
    ):
        self.player_unique_id = player_unique_id
        self.amount = amount
        self.transaction_id = transaction_id
        self.merchant = merchant
        self.email = email
        self.mobile = mobile