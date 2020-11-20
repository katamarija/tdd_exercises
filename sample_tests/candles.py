class Candle:
   color = "beige"

   def __init__(self, wicks=1):
       self.wicks = wicks
       self.burn_time_remaining = 10 * self.wicks

   def burn(self):
       self.burn_time_remaining -= 1
