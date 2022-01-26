from typing import List, TextIO

from anytree import Node, PostOrderIter
from malta.ruleset import RuleSet
from malta.rule import apply
from malta.membrane_item import MembraneItem
from malta.membrane import Membrane


class Environment:
    """
    This contains the mulitset tree
        the root of the tree is the top level (most external) membrane

    """

    def __init__(self, tree: Node,
                 rules: RuleSet,
                 all_items: List[MembraneItem]):

        self.tree = tree

        self.rules = rules

        # the details on the items that are in the membranes and in the environment.
        # useful for legends, status updates.
        self.all_items = all_items

        # FUTURE
        # the stop / halting condition
        # self.stop = stop

    def apply_rules(self, root: Node):
        # TODO - randomize rule order or add in rule priority
        # TODO - randomize membrane selection ?

        for node in PostOrderIter(root):
            print(f'{node.name} has: {node.contents}')

            for r in self.rules.rules:
                # does it apply? run it. update contents of the respective membrane
                node.contents = apply(r, node.contents)

    def save_as_dot_digraph(self, fname: str):
        """
        create a .dot file with a digraph which corresponds
        to the membrane structure and contents.
        """

        with open(fname, 'w') as f:
            f.write('update for use of anytree')

        raise Exception

        # with open(fname, 'w') as f:
        #     f.write('digraph d {\n')
        #
        #     f.write('\nnode[style=filled];\n')
        #
        #     if not isinstance(self.contents, MMultiset):
        #         raise ValueError
        #     else:
        #         for c in self.contents:
        #             s = self.get_items_details_as_dot(c)
        #             f.write(s)
        #
        #     for m in self.membranes:
        #         self.process_membrane_as_dot(f, m)
        #
        #     f.write('}')

    def process_membrane_as_dot(self, f: TextIO, m: Membrane):
        """
        process a single membrane,
            its contents and its submembranes
        """

        if not isinstance(m, Membrane):
            raise ValueError

        for c in m.contents:
            s = self.get_items_details_as_dot(c)
            f.write(s)

        # TODO
        try:
            if hasattr(m, 'membranes'):
                for mm in m.membranes:
                    self.process_membrane_as_dot(f, mm)
        except Exception:
            raise ValueError('recursive membranes is wip. TODO')

    def get_membrane_item_by_name(self, name) -> MembraneItem:
        """
        all_items needs to include any unique items that, at start up, only exist in
        the environment.
        """

        for mi in self.all_items:
            if mi.name == name:
                return mi

        return None

    def get_items_details_as_dot(self, name: str):
        """
        the membrane has the name of the content in its multiset
        however, when drawing the dot diagram, we would like the colour for the node
        """

        mi = self.get_membrane_item_by_name(name)
        if isinstance(mi, MembraneItem):
            c = mi.colour
        else:
            raise ValueError

        if isinstance(c, str):
            if c:
                s = f'\n{name}[color={c}]\n'
            else:
                s = f'{name}\n'
        return s
