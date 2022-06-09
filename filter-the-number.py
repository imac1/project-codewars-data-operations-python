import numbers
import unittest


def filter_string(string):
    # your code here
    # for i in range(len(string)):
    #     numbers = []
    #     if string[i].isnumeric():
    #         numbers.append(string[i])
    # for i in numbers:
    #     return i

    x = int(''.join(filter(str.isdigit, string)))
    return x
    


"""
These lines below are for testing purposes. Please, don't touch them :)
This code makes it possible to run a test on your solution during code review (or before, it's up to you!
If you run the following code, you can test your solution, just like on Codewars: python -m unittest filter-the-number.TestFilterTheNumber.test_basics
"""


class TestFilterTheNumber(unittest.TestCase):

    def test_basics(self):
        self.assertEqual(filter_string("123"), 123, 'Just return the numbers')
        self.assertEqual(filter_string("a1b2c3"), 123, 'Just return the numbers')
        self.assertEqual(filter_string("aa1bb2cc3dd"), 123, 'Just return the numbers')
        self.assertEqual(filter_string("aa 112 3dd"), 1123, 'Just return the numbers')
        self.assertEqual(filter_string("11bb2c23c3"), 112233, 'Just return the numbers')

    if __name__ == '__main__':
        unittest.main()
