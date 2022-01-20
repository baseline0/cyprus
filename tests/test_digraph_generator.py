import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)


import unittest

from viz.dot_colour import DotColour, get_rand_colours
from viz.digraph_generator import ContentItem


class TestDigraphGenerator(unittest.TestCase):

    def test_1(self):

        color = str(DotColour.aliceblue.name)

        c = ContentItem(name="cod", colour=color)
        print(c)
