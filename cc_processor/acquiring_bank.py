class AcquiringBank:

    def authorize_transaction(self, card, amount):
        if amount < 10:
            return True
        return False
