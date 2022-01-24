import json
from typing import List
from multiset import Multiset

from util import name_gen, prettyprint_json
from dot_colour import get_rand_colour


def json_serialize(m: Multiset) -> dict:
    d = {}
    s = m.__str__()
    s = s.replace("{", '')
    s = s.replace("}", '')
    s = s.replace("'", '')
    s = s.replace(":", '')
    s = s.replace(",", '')

    # may need to split into tuples here?
    tokens = s.split(' ')

    for t in tokens:
        if t in d.keys():
            d[t] += 1
        else:
            d[t] = 1
    return d


def multiset_to_dict(m: Multiset) -> dict:
    # multiset does not have __dict__
    # but we want to use json load/dump
    # works for m.__str__ = {'a'}

    d = {}

    s = m.__str__()
    s = s.replace("{", '')
    s = s.replace("}", '')
    s = s.replace("'", '')

    # may need to split into tuples here?
    tokens = s.split(':')

    for t in tokens:
        if t in d.keys():
            d[t] += 1
        else:
            d[t] = 1

    return d


class MembraneItem:
    """
    an object that lives within a membrane,
    interacts with other objects with respect to defined rules
    """

    __slots__ = ["name", "symbol", "descr", "colour"]

    def __init__(self, name: str, descr: str = None, colour: str = None):
        #
        if isinstance(name, str):
            self.name = name
        elif isinstance(name, dict):
            # via json loads. find better way
            self.set_from_dict(name)
        else:
            raise ValueError

        # short name for visualizations
        # truncate name
        if len(name) > 5:
            self.symbol = name[0:4]
        else:
            self.symbol = name

        # more details as needed
        self.descr = descr

        # the dot colour string.
        if colour is None:
            c = get_rand_colour()
            if c is list:
                # list of one?!
                self.colour = c[0]
            else:
                self.colour = c
        else:
            self.colour = colour

    def set_from_dict(self, d: dict):
        if "name" in d.keys():
            self.name = d["name"]
        if "descr" in d.keys():
            self.descr = d["descr"]
        if "symbol" in d.keys():
            self.symbol = d["symbol"]
        if "colour" in d.keys():
            self.colour = d["colour"]

    def __eq__(self, other):

        if isinstance(other, MembraneItem):
            return self.name == other.name
        return False

    def json_serialize(self) -> dict:
        d = {}
        d["name"] = self.name
        d["symbol"] = self.symbol
        d["descr"] = self.descr
        d["colour"] = self.colour
        return d


def membrane_item_deserialize(d: dict) -> MembraneItem:
    mi = MembraneItem()

    if "name" in d.keys():
        mi.name = d["name"]
    if "descr" in d.keys():
        mi.descr = d["descr"]
    if "symbol" in d.keys():
        mi.symbol = d["symbol"]
    if "colour" in d.keys():
        mi.colour = d["colour"]

    return mi


def get_rand_membrane_item() -> MembraneItem:
    name = name_gen.get_rand_name()
    mi = MembraneItem(name=name, descr=name, colour=get_rand_colour())
    return mi


class Membrane:
    # https://pythonhosted.org/multiset/

    def __init__(self, name: str, descr: str = None, contents=None):
        # =List[MembraneItem]):
        self.name = name
        self.descr = descr
        if contents is None:
            self.contents = []
        else:
            self.contents = contents


class Rule:

    __slots__ = ["name", "descr", "catalyst", "rule_input", "rule_output"]

    def __init__(self, name: str, descr: str, catalyst: Multiset, rule_input: Multiset, rule_output: Multiset):

        if isinstance(name, dict):
            self.set_from_dict(d=name)
            return

        self.name = name
        self.descr = descr

        # what is necessary for the rule to fire but what is not consumed
        if catalyst is None:
            self.catalyst = Multiset()
        else:
            self.catalyst = catalyst

        # what is consumed by the firing of the rule
        if rule_input is None:
            self.rule_input = Multiset()
        else:
            self.rule_input = rule_input

        # what is produced by the firing of the rule
        if rule_output is None:
            self.rule_output = Multiset()
        else:
            self.rule_output = rule_output

    def __repr__(self) -> str:
        s = "rule\n"
        s += f"\tcatalysts: {self.catalyst}\n"
        s += f"\tinput: {self.rule_input}\n"
        s += f"\toutput: {self.rule_output}\n"
        return s

    def set_from_dict(self, d: dict):

        if "name" in d.keys():
            self.name = d["name"]
        if "descr" in d.keys():
            self.descr = d["descr"]
        if "catalyst" in d.keys():
            self.catalyst = d["catalyst"]
        if "rule_input" in d.keys():
            self.rule_input = d["rule_input"]
        if "rule_output" in d.keys():
            self.rule_output = d["rule_output"]

    def json_serialize(self):
        d = {}

        d["name"] = self.name
        d["descr"] = self.descr
        d['catalyst'] = self.catalyst.__str__()
        d['rule_input'] = self.rule_input.__str__()
        d['rule_output'] = self.rule_output.__str__()

        return d


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
            # generate the alphabet from their presence in rules
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
            for c in r.catalyst:
                temp.update(c)
            for c in r.input:
                temp.update(c)
            for c in r.output:
                temp.update(c)

        self.alphabet = list(temp)


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


class Simulation:
    MAX_TICKS = 10
    COMPLETE = False

    def __init__(self) -> None:
        self.grammar = None
        self.output_dir = "./out/"

        # useful for when we use index to trigger file saves or image output
        self.current_index = 0

        # need to load config or programmatically populate: Environment()
        self.membrane_env = None

    def save(self, fname: str):
        with open(fname, 'w') as f:
            json.dump(self.membrane_env.__dict__, f, indent=4)

    def load(self, fname: str):
        # read in config file
        with open(fname, "r") as f:
            data = json.load(f)

            prettyprint_json(data=data)

        print(data)
        membranes = data['membranes']
        rules = data['rules']
        contents = data['contents']
        self.membrane_env = Environment(membranes, rules, contents)
        # self._generate_grammar()

    # def _generate_grammar(self):
    #     pass

    def next(self):
        # do next tick
        # go through each membrane. apply rules.
        # if no change, is complete or HALT condition.

        print(f'tick: {self.current_index}')
        self.current_index += 1
        self.membrane_env.apply_rules()

        # if self.current_index == 5:
        #     print('save img')

    def run(self):
        self.current_index = 0

        while self.current_index < Simulation.MAX_TICKS and not Simulation.COMPLETE:
            self.next()


def run1():
    sim = Simulation()

    mi1 = MembraneItem('b', descr='broccoli')
    mi2 = MembraneItem('c', descr='carrot')
    membrane_contents = [mi1, mi2]
    m = Membrane(name='m1', descr='hello', contents=membrane_contents)

    r_catalyst = Multiset()
    r_catalyst.add('b')

    r_input = Multiset()
    r_input.add('c')

    r_output = Multiset()
    r_output.add('w')

    r = Rule(name='r1', descr='', catalyst=r_catalyst, rule_input=r_input, rule_output=r_output)

    env_contents = MembraneItem(name='a', descr='apple')

    ruleset = RuleSet()
    ruleset.rules = [r]

    e = Environment(membranes=[m], rules=ruleset, contents=[env_contents])
    sim.membrane_env = e
    sim.save("./examples/run1.json")

    # sim.load("./examples/run1.json")
    # sim.run()


# --------------------


if __name__ == "__main__":
    run1()
