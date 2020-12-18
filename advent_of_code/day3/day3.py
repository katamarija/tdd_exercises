class Day3:
    def __init__(self):
        self.x_position = 0
        self.y_position = 0


    def count_trees_hit(self, hill):
        trees_hit = 0
        while self.y_position < len(hill):
            print(self.y_position, self.x_position, hill[self.y_position][self.x_position])
            if hill[self.y_position][self.x_position] == "#":
                trees_hit += 1
            self.x_position += 3
            if self.x_position >= len(hill[self.y_position]):
                self.x_position -= len(hill[self.y_position])
            self.y_position += 1
        return trees_hit

"""
0,0
3,1
6,2 = 2,2
9,3 = 5,3 = 1,3 = 4 columns, index goes up to 3
subtract 4 until you are under 3
"""
