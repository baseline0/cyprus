import os
import sys
import unittest

from malta.dot_colour import DotColour
from malta.util import NameGenerator
from malta.dot import ContentItem, ContentItemFactory, DigraphGenerator
from malta.dot import Factory

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)


class TestDigraphGenerator(unittest.TestCase):

    def test_1(self):

        color = str(DotColour.aliceblue.name)

        c = ContentItem(name="cod", colour=color)
        print(c)

    def test_2(self):

        factory = ContentItemFactory()

        items = factory.get_items(4)

        for i in items:
            print(i)

    def test_3(self):

        ng = NameGenerator()

        names = []
        for i in range(5):
            names.append(ng.get_rand_name())

        print(names)

    def test_demo1(self):

        c = Factory.get_cluster_1()

        dg = DigraphGenerator()
        dg.digraph.add_cluster(c)

        dg.save_dot(fname='./out/graph1.dot')
        # dg.save_png()

    def test_demo2(self):

        [c, peer] = Factory.get_cluster_2()

        dg = DigraphGenerator()
        dg.digraph.add_cluster(c)
        dg.digraph.add_cluster(peer)

        dg.save_dot(fname='./out/graph2.dot')
