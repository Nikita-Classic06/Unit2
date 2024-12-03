
from runner_and_tournament import Runner, Tournament
import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.b1 = Runner("Усэйн", 10)
        self.b2 = Runner("Андрей", 9)
        self.b3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for i, k in cls.all_results.items():
            print(k)

    def test_1(self):
        p = Tournament(90, self.b1, self.b3)
        self.all_results[len(self.all_results)] = p.start()
        last_result = list(self.all_results.values())[-1]
        self.assertTrue(last_result[len(last_result)] == "Ник")

    def test_2(self):
        p = Tournament(90, self.b2, self.b3)
        self.all_results[len(self.all_results)] = p.start()
        last_result = list(self.all_results.values())[-1]
        self.assertTrue(last_result[len(last_result)] == "Ник")


    def test_3(self):
        p = Tournament(90, self.b1, self.b2, self.b3)
        self.all_results[len(self.all_results)] = p.start()
        last_result = list(self.all_results.values())[-1]
        self.assertTrue(last_result[len(last_result)] == "Ник")


if __name__ == "__main__":
    TournamentTest()