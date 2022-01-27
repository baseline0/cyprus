import unittest

from anytree import Node, RenderTree, PostOrderIter
from anytree.exporter import DotExporter
from anytree.walker import Walker

from malta.multiset_treenode import MultisetTreeFactory, show_multiset_tree, get_random_selection_from_alphabet
from malta.util import get_alphabet1
from mmultiset import MMultiset


class TestMembraneTree(unittest.TestCase):

    # def test_1(self):
    #     x = 1
    #     # mt = MultisetTreeNode("test", 4, 4)
    #     mt = MultisetTreeNode(name="test", length=4, width=4)

    def test_anytree(self):

        udo = MultisetTreeFactory().get_mt1()
        print(udo)

        for pre, fill, node in RenderTree(udo):
            print("%s%s" % (pre, node.name))

        DotExporter(udo).to_picture("examples/udo.png")

    def test_walk(self):

        udo = MultisetTreeFactory().get_mt1()

        w = Walker()
        w.walk(udo, udo)

        print([node.name for node in PostOrderIter(udo)])

    def test_multiset_in_tree(self):

        mt2 = MultisetTreeFactory().get_mt2()

        show_multiset_tree(mt2)

        alphabet = get_alphabet1(10)

        items = {}
        items['a'] = 2
        items['b'] = 5
        items['w'] = 1

        # add_items()

    def test_get_random_selection_from_alphabet(self):

        alphabet = get_alphabet1(15)
        x = get_random_selection_from_alphabet(5, alphabet)
        print(x)

    # def test_randomly_populate(self):
    #     alphabet = get_alphabet1(10)
    #     # mt = MultisetTreeNode(name="test_rp", length=4, width=3)
    #     mt = MultisetTreeNode("test_rp", 4, 3)
    #     randomly_populate(mt, alphabet)
    #
    #     print(mt)
    #     # walk

    def test2(self):

        root = Node(name="root", contents=MMultiset())

        contents = MMultiset()
        contents.add('a', 1)
        contents.add('b', 4)
        s0 = Node(name="sub0", parent=root, contents=contents)

        print([node.name for node in PostOrderIter(root)])

        for node in PostOrderIter(root):
            print(f'{node.name} has: {node.contents}')
