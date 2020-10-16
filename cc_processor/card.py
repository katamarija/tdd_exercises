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

   @classmethod
   def _luhn_valid(cls, number):
       check_number = 0
       for i in range(len(number)-2, -1, -2):
           if int(number[i]) * 2 > 9:
               check_number += (int(number[i]) * 2) - 9
           else:
               check_number += int(number[i]) * 2
       for i in range(len(number)-1, -1, -2):
           check_number += int(number[i])
       if check_number % 10 == 0:
           return True
       else:
           return False

   @property
   def valid(self):
       return Card._luhn_valid(self.number)
