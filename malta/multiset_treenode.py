import random
from typing import List
from string import ascii_lowercase

from anytree import Node, RenderTree, PreOrderIter
from anytree import NodeMixin, Node

from multiset import Multiset

from mmultiset import MMultiset, make_mmultiset


class MultisetTreeNode(MMultiset, NodeMixin):
    """
    A node for use with anytree that contains a multiset
    """

    def __init__(self, name: str, length: int, width: int, parent=None, children=None,):
        # super(MMultiset, self).__init__()

        self.name = name
        self.length = length
        self.width = width
        self.parent = parent

        if children:  # set children only if given
            self.children = children


# > DotExporter(dan,
# ...             nodeattrfunc=lambda node: "fixedsize=true, width=1, height=1, shape=diamond",
# ...             edgeattrfunc=lambda parent, child: "style=bold"


class MultisetTreeFactory:

    @staticmethod
    def get_mt1() -> MultisetTreeNode:
        udo = Node("Udo")
        marc = Node("Marc", parent=udo)
        lian = Node("Lian", parent=marc)
        dan = Node("Dan", parent=udo)
        jet = Node("Jet", parent=dan)
        jan = Node("Jan", parent=dan)
        joe = Node("Joe", parent=dan)

        return udo

    @staticmethod
    def get_mt2() -> MultisetTreeNode:
        node_names = ['m1', 'm2', 'm3', 'm4', 'm5']

        root = Node("root")
        children = []

        for n in node_names:
            children.append(Node(n, parent=root))

        return root


def add_items(mt: Node, items: dict):
    """
    items is dict with name (key:str) and quantity (int)
    to add to multiset.
    """

    if not isinstance(mt, Node):
        raise ValueError

    if not isinstance(items, dict):
        raise ValueError

    for k, v in items.items():
        mt.add(k, v)


def show_multiset_tree(x: Node):
    for pre, fill, node in RenderTree(x):
        print("%s%s" % (pre, node.name))


def get_random_selection_from_alphabet(num: int, alphabet: List[str], max_samples: int=10) -> dict:
    """
    num: the number of letters that should be selected from alphabet
    max_samples: the maximum multiplicity of the number selected

    FUTURE - compare size of alphabet to number (num) requested
    FUTURE - ensure that distinct letters in alphabet are returned
    """
    d = {}

    if num < 0:
        num = 1
        print('setting min to 1. expect positive')
    if max_samples < 0:
        max_samples = 10
        print('setting max_samples to 10. expect positive')

    from random import sample

    for i in range(num):
        selected = sample(alphabet, 1).pop()
        multiplicity = random.randint(1, max_samples)
        d[selected] = multiplicity

    return d


def randomly_populate(mt: MultisetTreeNode, alphabet: List[str]):
    for node in PreOrderIter(mt):
        items = get_random_selection_from_alphabet(alphabet)
        for k, v in items.items():
            node.add(k, v)


def get_membrane_tree1(alphabet: List[str]) -> Node:
    """
    use anytree.node with additional attr: contents = multiset
    tree must have node named: root
    """

    if not alphabet:
        print('expecting a list of membrane identifiers')
        raise ValueError

    # outer membrane has no initial objects (empty multiset)
    root = Node(name="root", contents=MMultiset())

    # manually make tree for now
    # FUTURE - call random networkx generator

    # make a single internal membrane with all items
    # guaranteed to have catalyst
    # FUTURE - add a utility that ensures that the contents are avaialble for a specific rule to fire.
    items = {}
    count = 1
    for x in alphabet:
        items[x] = count
        count += 1

    contents = make_mmultiset(items)

    s0 = Node(name="sub0", parent=root, contents=contents)

    return root
