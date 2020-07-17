import unittest
from bowling import Game

class BowlingTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_all_gutterballs(self):
        self.helper_test_roll(20, 0)
        self.assertEqual(0, self.game.score())


    def helper_test_roll(self, rolls, pins):
        for roll in range(rolls):
            self.game.roll(pins)

    def test_perfect_game(self):
        self.helper_test_roll(12, 10)
        self.assertEqual(300, self.game.score())

if __name__ == '__main__':
    unittest.main()
