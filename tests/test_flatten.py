import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from cyprus.parser import flatten

import unittest

class TestFlatten(unittest.TestCase):

    def test_simple(self):

        x = ["a", "cat", "dog"]

        y = flatten(x)
        self.assertEquals(x,y)



    def test_nested(self):

        x = ["a", [1, 2], "dog"]

        y = flatten(x)
        z = ["a", 1, 2, "dog"]
        self.assertEquals(y,z)
