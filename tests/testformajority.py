import unittest
from problems.majaority_element import majority_count

class TestMajorityCount(unittest.TestCase):
    def test_majority_count(self):
        self.assertEqual(majority_count([3, 2, 3]), 3)
        self.assertEqual(majority_count([2, 2, 1, 1, 1, 2, 2]), 2)
        self.assertEqual(majority_count([1, 1, 1, 2, 3, 4, 1]), 1)
        self.assertEqual(majority_count([1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7]), 7)
        self.assertEqual(majority_count([1, 2, 3, 3, 3, 3, 3]), 3)
        self.assertEqual(majority_count([4, 4, 4, 4, 4, 4, 4]), 4)
        self.assertEqual(majority_count([5, 5, 5, 5, 5, 5, 5, 5]), 5)
        self.assertEqual(majority_count([6, 6, 6, 6, 6, 6, 6, 6, 6]), 6)
        self.assertEqual(majority_count([7, 7, 7, 7, 7, 7, 7, 7, 7, 7]), 7)
        self.assertEqual(majority_count([8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]), 8)

if __name__ == '__main__':
    unittest.main()