import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)


import unittest

from malta.dot_colour import DotColour
from malta.digraph_generator import ContentItem, ContentItemFactory, NameGenerator, DigraphGenerator
from malta.digraph_generator import Cluster


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


    def test_demo1():
        # simple. small. nested one deep

        c = Cluster(name="top")
        c.contents = ['a', 'b', 'c']
        

        d = Cluster(name="nested")
        d.contents = ['d', 'e', 'f']
        
        c.add_cluster(d)

        dg = DigraphGenerator()
        dg.digraph.add_cluster(c)

        dg.run(fname='./viz/out/graph1.dot')


    def test_demo2():
    
        c = Cluster(name="top")
        c.contents = ['a', 'b', 'c']
        
        peer = Cluster(name="peer")
        peer.contents = ['a1', 'b1', 'c1']
        
        d = Cluster(name="nested")
        d.contents = ['d', 'e', 'f']

        e = Cluster(name="nested_2")
        e.contents = ['g', 'h', 'i']

        d.add_cluster(e)
        c.add_cluster(d)


        dg = DigraphGenerator()
        dg.digraph.add_cluster(c)
        dg.digraph.add_cluster(peer)

        dg.run(fname='./viz/out/graph2.dot')
