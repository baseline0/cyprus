from typing import List

from malta.ruleset import RuleSet
from malta.rule import Rule
from malta.mmultiset import MMultiset
from malta.membrane_item import MembraneItem
from malta.membrane import Membrane


def apply(r: Rule, m: Membrane):
    # fire once if possible.
    # Future - apply as many times as possible
    # Future - apply probabilistically

    if r.catalyst.issubset(m.contents):
        # catalysts present
        if r.rule_input.issubset(m.contents):
            # inputs here. fire rule.
            m.contents -= r.rule_input
            m.contents += r.rule_output


class Environment:
    """
    top level membrane
    """

    def __init__(self, membranes: List[Membrane],
                 rules: RuleSet,
                 contents: MMultiset,
                 all_items: List[MembraneItem]):

        self.membranes = membranes

        self.rules = rules

        # a list of items not in a membrane but in environment
        self.contents = contents

        # the details on the items that are in the membranes and in the environment.
        # useful for legends, status updates.
        self.all_items = all_items

        # the stop / halting condition
        # self.stop = stop

    def apply_rules(self):
        # TODO - randomize rule order or add in rule priority
        # TODO - randomize membrane selection ?

        for r in self.rules.rules:
            # does it apply? run it. update contents of the respective membrane
            for m in self.membranes:
                apply(r, m)

    def save_as_dot_digraph(self, fname:str):
        """
        create a .dot file with a digraph which corresponds
        to the membrane structure and contents.
        """

        with open(fname, 'w') as f:
            f.write('digraph d {')

            s = self.contents.as_dot()
            f.write(s)

            for m in self.membranes:
                f.write(m.as_dot())

            f.write('}')



