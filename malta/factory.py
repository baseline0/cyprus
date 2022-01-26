from typing import List

import json
from anytree import Node
from malta.environment import Environment
from malta.dot_colour import get_rand_colour
from malta.dot import ContentItem
from malta.membrane_item import MembraneItem
from malta.membrane import Membrane
from malta.util import NameGenerator
from malta.rule import make_rule
from malta.mmultiset import MMultiset, make_mmultiset
from malta.ruleset import RuleSet


class Factory:
    """
    provide known and constructed examples of key classes for tests and simulation reference code
    """

    @staticmethod
    def get_membrane_item1() -> MembraneItem:
        mi = MembraneItem(name="factory", descr="units")
        return mi

    @staticmethod
    def get_membrane_item_collection1() -> List[MembraneItem]:
        """
        digital ag genomics
        """
        mi1 = MembraneItem(name="parent1", descr="germplasm")
        mi2 = MembraneItem(name="parent2", descr="germplasm")
        mi3 = MembraneItem(name="F1", descr="germplasm")
        mi4 = MembraneItem(name="F2", descr="germplasm")
        mi5 = MembraneItem(name="F3", descr="germplasm")
        return [mi1, mi2, mi3, mi4, mi5]

    @staticmethod
    def get_rand_membrane_item() -> MembraneItem:
        name = NameGenerator.get_rand_name()
        mi = MembraneItem(name=name, descr=name, colour=get_rand_colour())
        return mi

    @staticmethod
    def get_environment1() -> Environment:
        """
        special case:
            CONSTRAINT:
                the environment has items that also exist in a membrane

        update for tree
        """

        alphabet = ['a', 'b', 'c', 'w']

        # details on the membranes items for summary report
        with open("./config/sim1_items.json") as f:
            out = json.load(f)

        all_items = []
        for k, v in out.items():
            all_items.append(MembraneItem(k, descr=v))

        # ---------------------
        # make rules
        catalyst = {'b': 1}
        r_input = {'c': 1}
        r_output = {'w': 1}
        r = make_rule(name='r1', descr="make w from c when b present", catalyst=catalyst, rule_input=r_input, rule_output=r_output)

        ruleset = RuleSet()
        ruleset.rules.append(r)

        # ---------------------
        # make membrane tree
        root = Node(name="root", contents=MMultiset())

        items = {}
        items['a'] = 1
        items['b'] = 2
        items['c'] = 3
        contents = make_mmultiset(items)

        s0 = Node(name="sub0", parent=root, contents=contents)

        e = Environment(tree=root, rules=ruleset, all_items=all_items)

        return e


class ContentItemFactory:

    @classmethod
    def get_items_for_names(cls, names, colour: str = None):  # -> List(ContentItem):
        # all same colour
        items = []
        if colour is None:
            colour = get_rand_colour()

        for n in names:
            items.append(ContentItem(name=n, colour=colour))
        return items

    @classmethod
    def get_items(cls, n: int = 10, colour: str = None):  # -> List(ContentItem):
        # same colour

        items = []

        if colour is None:
            colour = get_rand_colour()

        for n in range(n):
            items.append(ContentItem(colour=colour))
        return items

    # @staticmethod
    # def get_multi_coloured_items(n: int = 10):
    #     # TODO
