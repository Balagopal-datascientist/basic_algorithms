
import unittest
# from prantha import complete_prantha as prantha
def prantha(string):
    counter=0
    temp=0
    for i in string:
        if i =='(':
            counter+=1
        elif i== ')' and counter:
            counter-=1
        else:
            temp+=1
    return counter+temp
class TestPrantha(unittest.TestCase):
    def test_valid_parentheses(self):
        self.assertEqual(prantha("()())()"), 1)
        self.assertEqual(prantha(")("), 2)
        self.assertEqual(prantha("()"), 0)
        self.assertEqual(prantha("((()))"), 0)
        self.assertEqual(prantha("((())"), 1)
        self.assertEqual(prantha("(()))"), 1)
        self.assertEqual(prantha(")("), 2)
        self.assertEqual(prantha(""), 0)
        self.assertEqual(prantha("((((("), 5)
        self.assertEqual(prantha(")))))"), 5)

if __name__ == '__main__':
    unittest.main()