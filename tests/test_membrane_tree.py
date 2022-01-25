import unittest

from anytree import Node, RenderTree
from anytree.exporter import DotExporter

from malta.membrane_tree import MembraneTree


class TestMembraneTree(unittest.TestCase):

    def test_1(self):

        mt = MembraneTree()

    def test_anytree(self):

        udo = Node("Udo")
        marc = Node("Marc", parent=udo)
        lian = Node("Lian", parent=marc)
        dan = Node("Dan", parent=udo)
        jet = Node("Jet", parent=dan)
        jan = Node("Jan", parent=dan)
        joe = Node("Joe", parent=dan)

        print(udo)

        for pre, fill, node in RenderTree(udo):
            print("%s%s" % (pre, node.name))



        DotExporter(udo).to_picture("udo.png")