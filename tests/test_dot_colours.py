import unittest

from viz.dot_colour import get_rand_colours, DotColour


class TestDotColour(unittest.TestCase):

    def test_1(self):

        palette = get_rand_colours()
        print(palette)
