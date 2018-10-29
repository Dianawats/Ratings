import unittest
from app.scores import Scores

class TestScores(unittest.TestCase):
    def setUp(self):
        self.scores = Scores()

    def tearDown(self):
        pass

    def test_all_scores(self):
        self.assertTrue(self.scores)

    # def test_login(self):
    #     pass
    


if __name__ == "__main__":
    unittest.main()