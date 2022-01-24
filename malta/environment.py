from typing import List

from malta.ruleset import RuleSet
from malta.rule import Rule
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
                 contents: List[MembraneItem]):  # , stop ):

        # a list of items not in a membrane but in environment
        self.contents = contents

        self.membranes = membranes

        self.rules = rules

        # the stop / halting condition
        # self.stop = stop

    def apply_rules(self):
        # TODO - randomize rule order or add in rule priority
        # TODO - randomize membrane selection ?

        for r in self.rules.rules:
            # does it apply? run it. update contents of the respective membrane
            for m in self.membranes:
                apply(r, m)


