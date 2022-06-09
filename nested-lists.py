import unittest


def list_depth(l):

    # return int(isinstance(l, list)) and max(map(list_depth, l or [0])) + 1

    sq_brkt_counter = 0
    empty_list = []
    for i in str(l):
        if i == '[':
            # 1. for each open sq brkt add 1
            sq_brkt_counter += 1
        elif i == ']':

            empty_list.append(sq_brkt_counter)
            # 1. as above -1
            sq_brkt_counter -= 1
    return max(empty_list) 


"""
These lines below are for testing purposes. Please, don't touch them :)
This code makes it possible to run a test on your solution during code review (or before, it's up to you!
If you run the following code, you can test your solution, just like on Codewars: python -m unittest nested-lists.TestListDepth.test_basics
"""


class TestListDepth(unittest.TestCase):

    def test_basics(self):
        self.assertEqual(list_depth([1, [2, [3, [4, [5, [6], 5], 4], 3], 2], 1]), 6)
        self.assertEqual(list_depth([True]), 1)
        self.assertEqual(list_depth([]), 1)
        self.assertEqual(list_depth([2, "yes", [True, False]]), 2)
        self.assertEqual(list_depth([2.0, [2, 0], 3.7, [3, 7], 6.7, [6, 7]]), 2)

    if __name__ == '__main__':
        unittest.main()
