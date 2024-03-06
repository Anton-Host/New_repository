from git_repository_new_file import mathematic
import unittest

class NameTestCase(unittest.TestCase):

    def test_mathematic(self):
        res = mathematic(7,9)
        self.assertEqual(res,16)