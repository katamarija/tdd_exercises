class Card:
   def __init__(self, number, spending_limit, balance=0):
       self._number = number
       self._balance = balance
       self._spending_limit = spending_limit

   @property
   def balance(self):
       return self._balance

   @property
   def number(self):
       return self._number

   @property
   def spending_limit(self):
       return self._spending_limit

   def charge(self, amount):
       temp_balance = self._balance + amount

       if self._spending_limit < temp_balance:
           return False

       self._balance = temp_balance
       return True

   def refund(self, amount):
       self._balance -= amount
       return True
