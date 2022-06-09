import unittest
import itertools


def sum_nested(lst):
    # flat = list(itertools.chain(*lst))
    # return sum(flat)
    flat = []
    for elem in lst:
        if type(elem) is list:
            for item in elem:
                flat.append(item)
        else:
            flat.append(elem)
    # flat = [item for sublist in lst for item in sublist]
    return sum(flat)

"""
These lines below are for testing purposes. Please, don't touch them :)
This code makes it possible to run a test on your solution during code review (or before, it's up to you!
If you run the following code, you can test your solution, just like on Codewars: python -m unittest sum-of-a-lists.TestSumNested.test_basics

"""


class TestSumNested(unittest.TestCase):

    def test_basics(self):
        self.assertEqual(sum_nested([1]), 1)
        self.assertEqual(sum_nested(list(range(11))), 55)
        self.assertEqual(sum_nested([[1], []]), 1)
        self.assertEqual(sum_nested([[1, 2, 3, 4]]), 10)
        self.assertEqual(sum_nested([1, [1], [1, [1]], [1, [1], [1, [1]]]]), 8)
        self.assertEqual(sum_nested([[[[], [], [[[[[[[[[[]]]]]]]]]]], [], [], [[[], [[]]]]], []]), 0)

    if __name__ == '__main__':
        unittest.main()

