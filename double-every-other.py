import unittest
# import pdb


def double_every_other(lst):
    res = []
    for el in range(len(lst)):
        if el % 2 != 0:
            res.append(lst[el]*2)
        else:
            res.append(lst[el])
    

# pdb.run('double_every_other(lst)')

"""
These lines below are for testing purposes. Please, don't touch them :)
This code makes it possible to run a test on your solution during code review (or before, it's up to you!
If you run the following code, you can test your solution, just like on Codewars: python -m unittest double-every-other.TestDoubleEveryOther.test_basics
"""


class TestDoubleEveryOther(unittest.TestCase):

    def test_basics(self):
        self.assertEqual(double_every_other([1, 2, 3, 4, 5]), [1, 4, 3, 8, 5])
        self.assertEqual(double_every_other([1, 19, 6, 2, 12, -3]), [1, 38, 6, 4, 12, -6])
        self.assertEqual(double_every_other([-1000, 1653, 210, 0, 1]), [-1000, 3306, 210, 0, 1])

    if __name__ == '__main__':
        unittest.main()
