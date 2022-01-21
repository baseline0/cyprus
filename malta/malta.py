from typing import List
from multiset import Multiset

from malta.util import prettyprint_json


class MembraneItem:
    """
    an object that lives within a membrane,
    interacts with other objects with respect to defined rules
    """

    def __init__(self, name: str, descr: str = None, colour: str = None):
        #
        self.name = name

        # short name for visualizations
        # truncate name
        self.symbol = name[0:4]

        # more details as needed
        self.description = descr

        # the dot colour string.
        self.colour = colour


class Membrane:
    # https://pythonhosted.org/multiset/

    def __init__(self, name: str, descr: str = None, contents=Multiset[MembraneItem]):
        self.name = name
        self.descr = descr
        self.contents = contents


class Rule:
    def __init__(self):
        # what is necessary for the rule to fire but what is not consumed
        self.catalyst = Multiset()

        # what is consumed by the firing of the rule
        self.input = Multiset()

        # what is produced by the firing of the rule
        self.output = Multiset()

    def __repr__(self) -> str:
        s = "rule\n"
        s += f"\tcatalysts: {self.catalyst}\n"
        s += f"\tinput: {self.input}\n"
        s += f"\toutput: {self.output}\n"

        return s


class RuleSet:

    def __init__(self):

        # the list of symbols which are valid
        # this is the list of all catalysts, inputs and outputs
        self.alphabet = []

        # the set of rules
        self.rules = []

    def set_alphabet(self, alphabet: List[str]) -> None:
        self.alphabet = alphabet

    def set_rules(self, rules: List[Rule]) -> None:

        self.rules = rules

        if not self.alphabet:
            # if None or empty list
            # generate the alphabet from the implict use in rules
            self.detect_alphabet_from_rules()
            # end state: alphabet and rules are consistent
        else:
            # ensure that the rules match the already existing alphabet
            for r in rules:
                # TODO
                print(r)

    def detect_alphabet_from_rules(self):

        self.alphabet = []

        temp = set()

        for r in self.rules:
            for c in r.catalysts:
                temp.update(c)
            for c in r.input:
                temp.update(c)
            for c in r.output:
                temp.update(c)

        self.alphabet = list(temp)


def apply(rule: Rule, m: Membrane):
    # fire once if possible.
    # Future - apply as many times as possible
    # Future - apply probabilistically

    if rule.catalysts.issubset(m.contents):
        # catalysts present
        if rule.input.issubset(m.contents):
            # inputs here. fire rule.
            m.contents.remove(rule.input)
            m.contents.add(rule.output)


class Environment:
    """
    top level membrane
    """

    def __init__(self, membranes: List[Membrane],
                 rules: List[Rule],
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

        for r in self.rules():
            # does it apply? run it. update contents of the respective membrane
            for m in self.membranes:
                apply(r, m)


class Simulation():

    def __init__(self) -> None:

        self.grammar = None

    def load(self, fname: str):

        with open(fname, "r") as f:
            data = json.load(f)

            prettyprint_json(data=data)

        print(data)

    def load_config(self, fname: str):
        """
        read in config file

        """

        try:
            self._generate_grammar()
        except:
            raise Exception

    def _generate_grammar(self):
        pass

    def next(self):
        # do next tick
        # go through each membrane. apply rules.
        # if no change, is complete or HALT condition.

        print('tick')

    def run(self):

        MAX_TICKS = 10
        COMPLETE = False
        i = 0

        while i < MAX_TICKS and not COMPLETE:
            self.next()
            i += 1


# --------------------


if __name__ == "__main__":

    sim = Simulation()

    sim.load_config("./examples/hello.json")
    sim.run()