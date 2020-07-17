class Game:
    def __init__(self):
        self.frame = []

    def roll( self, frame, first_roll, second_roll ):
        self.frame = Frame(first_roll, second_roll)
        self.rolls.append( pins )

    def score(self):
        total = 0
        roll_index = 0
        for roll in range(10):
            total += self.scoreFrame(roll_index)
            roll_index += 2
        return total

    def scoreFrame(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index+1]

class Frame:
    def __init__(self, first_roll, second_roll):
        self.first_roll = first_roll
        self.second_roll = second_roll
