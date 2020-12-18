class Day3:
    def __init__(self):
        self.x_position = 0
        self.y_position = 0


    def count_trees_hit(self, hill, right, down):
        self.x_position = 0
        self.y_position = 0
        trees_hit = 0
        while self.y_position < len(hill):
            if hill[self.y_position][self.x_position] == "#":
                trees_hit += 1
            self.x_position += right
            if self.x_position >= len(hill[self.y_position]):
                self.x_position -= len(hill[self.y_position])
            self.y_position += down
        return trees_hit
