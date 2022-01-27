import random
from random import randint
from typing import List

import matplotlib.pyplot as plt
import networkx as nx
import networkx.convert
from anytree import NodeMixin, Node
from anytree import RenderTree, PreOrderIter

from mmultiset import MMultiset, make_mmultiset


def save_graph_to_file(fname: str, g) -> None:
    print(f"see: {fname}")
    # TODO FIX
    # a = nx.nx_agraph.to_agraph(g)
    # nx.nx_agraph.write_dot(a, "./graph_/")
    nx.draw(g)
    nx.draw_planar(g)
    plt.draw()
    plt.savefig(fname)


def get_polytree(num_nodes: int = 10):
    """
    A polytree (or directed tree or oriented tree or singly
    connected network) is a directed acyclic graph (DAG)
    whose underlying undirected graph is a tree

    https://dsplab.feri.um.si/glossary/directed-tree/

    directed tree
    A weakly connected, directed forest. Equivalently, the underlying graph
    structure (which ignores edge orientations) is an undirected tree.
    In convention B, this is known as a polytree.

    https://networkx.org/documentation/stable/reference/algorithms/tree.html

    https://memgraph.com/docs/mage/query-modules/python/nxalg

    The graph is always a (directed) tree.
    P. L. Krapivsky and S. Redner, Organization of Growing Random Networks, Phys. Rev. E, 63, 066123, 2001.
    https://networkx.org/documentation/stable/reference/generated/networkx.generators.directed.gn_graph.html

    """

    g = nx.gn_graph(num_nodes)
    save_graph_to_file("directed_tree_example.png", g)

    return g


def random_dag(nodes: int = 5):
    """
    Generate a random Directed Acyclic Graph (DAG) with a given number of nodes and edges

    so the matplotlib image is tagged as "not a dag", but perhaps it is. but what we really
    want is a polytree
    """
    g = nx.DiGraph()

    # maximum number of edges in a directed graph with n vertices (which has no cycles):  n−1
    # proof left to reader
    edges = nodes - 1

    for i in range(nodes):
        g.add_node(i)

    while edges > 0:
        a = randint(0, nodes - 1)
        b = a
        while b == a:
            b = randint(0, nodes - 1)
        g.add_edge(a, b)
        if nx.is_directed_acyclic_graph(g):
            edges -= 1
        else:
            # we closed a loop!
            g.remove_edge(a, b)

    # is this really a dag? check it
    save_graph_to_file('an_example_of_random_dag.png', g)

    return g


class MultisetTreeNode(MMultiset, NodeMixin):
    """
    A node for use with anytree that contains a multiset
    """

    def __init__(self, name: str, length: int, width: int, parent=None, children=None, ):
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


def get_random_selection_from_alphabet(num: int, alphabet: List[str], max_samples: int = 10) -> dict:
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


def get_rand_number_and_multiplicity_of_items(alphabet: List[str], max_multiplicity: int = 1):
    if not alphabet:
        raise ValueError
    if max_multiplicity < 1:
        max_multiplicity = 1
        print("max_multiplicity set to 1")

    items = {}

    num_letter = random.randint(1, len(alphabet))
    letters = random.sample(alphabet, num_letter)

    for x in letters:
        items[x] = random.randint(1, max_multiplicity)

    return items


def get_membrane_tree1(alphabet: List[str]) -> Node:
    """
    use anytree.node with additional attr: contents = multiset
    tree must have node named: root
    """

    if not alphabet:
        print('expecting a list of membrane identifiers')
        raise ValueError

    root = get_root_node()

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


def get_membrane_tree2(alphabet: List[str]) -> (Node, nx.Graph):
    """
        a little more complex nesting
        done manually.
        FUTURE - obtain a random graph from networkx

    """

    # outer membrane has no initial objects (empty multiset)

    # get a small random dag.
    # walk the dag
    # at each node, add in random number of items
    num_nodes = 10
    g = get_polytree(num_nodes)

    # make num nodes and populate. do parent nodes later.
    nodes = []
    root = get_root_node()
    nodes.append(root)

    for i in range(1, num_nodes):
        items = get_rand_number_and_multiplicity_of_items(alphabet)
        contents = make_mmultiset(items)
        y = Node(name=str(i), parent=root, contents=contents)
        nodes.append(y)

    # sanity
    # assert (len(nodes) == num_nodes)

    # - do for traversal from bottom
    # for x in list(nx.dfs_edges(g, source=0)):

    # correct the parent but
    # never adjust root (index 0)
    #
    # example: outedges
    #   [e for e in G.edges]
    #   [(0, 1), (1, 2), (2, 3)]
    for e in g.edges:
        print(f"edge: {e}")

        # cant expect tuples to be ordered
        if e[0] > e[1]:
            idx_self = e[1]  # node id
            idx_child = e[0]  # child id
        else:
            idx_self = e[0]  # node id
            idx_child = e[1]  # child id

        # go to child, add idx_self as parent
        nodes[idx_child].parent = nodes[idx_self]

    return root, g


def get_root_node() -> Node:
    # outer membrane has no initial objects (empty multiset)
    root = Node(name="root", contents=MMultiset())
    return root


class MemStruct:
    def __init__(self):
        pass

    def save_to_file(self, fname: str):
        pass


def convert_tree_to_membranes(g: nx.Graph) -> MemStruct:
    """
    root is root of directed tree (polytree)
    note: need to constantly associated networkx.Graph g and MultisetTree Node root to capture
    both the membrane structure AND the multiset contents. so TODO make appropriate data struct
    """

    if not isinstance(g, nx.Graph):
        raise ValueError

    x = networkx.convert.to_dict_of_dicts(g)
    y = networkx.convert.to_dict_of_lists(g)

    m = MemStruct()

    return m
