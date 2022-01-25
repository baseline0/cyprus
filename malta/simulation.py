from typing import List

from anytree import Node, RenderTree, PostOrderIter

from malta.environment import Environment
from malta.membrane_item import MembraneItem
from malta.mmultiset import MMultiset
from malta.rule import Rule
from malta.ruleset import RuleSet


class Simulation:
    MAX_TICKS = 10
    COMPLETE = False

    def __init__(self) -> None:
        self.output_dir = "./sims/"

        # useful for when we use index to trigger file saves or image output
        self.current_index = 0

        # need to load config or programmatically populate: Environment()
        self.environment = None

    def save(self, fname: str):
        # with open(fname, 'w') as f:
        #     json.dump(self.membrane_env.__dict__, f, indent=4)
        pass

    def load(self, fname: str):
        # # read in config file
        # with open(fname, "r") as f:
        #     data = json.load(f)
        #
        #     prettyprint_json(data=data)
        #
        # print(data)
        # membranes = data['membranes']
        # rules = data['rules']
        # contents = data['contents']
        # self.membrane_env = Environment(membranes, rules, contents)
        # # self._generate_grammar()
        pass

    def next(self):
        # do next tick
        # go through each membrane. apply rules.
        # if no change, is complete or HALT condition.

        print(f'tick: {self.current_index}')
        self.current_index += 1
        self.environment.apply_rules(self.root)

        # if self.current_index == 5:
        #     print('save img')

    def run(self):
        self.current_index = 0

        print('running membrane simulation')
        print(f'see output: {self.output_dir}')

        while self.current_index < Simulation.MAX_TICKS and not Simulation.COMPLETE:
            self.next()

        print('DONE.')


def get_item_names_from_membrane_items(items: List[MembraneItem], names: List[str] = None) -> List[str]:
    """
    the environment needs a list of MembraneContents
    but the membrane and rule just use the names as identifiers.
    """

    if names is None:
        names = []
        # process the list
        for mi in items:
            names.append(mi.name)

        print(f'number of items is: {len(names)}')
        print(f'{names}')
        return names
    elif isinstance(names, List):
        # we are appending to an existing list
        # convert the existing list into a set.
        # process the list.
        # convert back to a list
        print('TODO')
        raise ValueError("FIXME")
    else:
        raise ValueError


def get_multiset_of_item_names_from_membrane_items(items: List[MembraneItem], names: List[str] = None) -> MMultiset:
    """
    the environment needs a list of MembraneContents
    but the membrane and rule just use the names as identifiers.
    """
    # FIXME - add in multiplicity of items to initialization

    if names is None:
        names = MMultiset()
        # process the list
        for mi in items:
            names.add(mi.name)
        return names
    elif isinstance(names, List):
        # we are appending to an existing list
        # convert the existing list into a set.
        # process the list.
        # convert back to a list
        print('TODO')
        raise ValueError("FIXME")
    else:
        raise ValueError


class SimulationFactory:

    @staticmethod
    def get_sim1() -> Simulation:
        sim = Simulation()

        alphabet = ['a', 'b', 'c', 'w']

        # details on the membranes items for summary report
        m_a = MembraneItem('a', descr='asset')
        m_b = MembraneItem('b', descr='budget')
        m_c = MembraneItem('c', descr='capital')
        m_w = MembraneItem('w', descr='win')
        all_items = [m_a, m_b, m_c, m_w]

        # ---------------------
        # make rules
        r_catalyst = MMultiset()
        r_catalyst.add('b')

        r_input = MMultiset()
        r_input.add('c')

        r_output = MMultiset()
        r_output.add('w')

        r = Rule(name='r1', descr='', catalyst=r_catalyst, rule_input=r_input, rule_output=r_output)

        ruleset = RuleSet()
        ruleset.rules = [r]

        # ---------------------
        # make membrane tree
        root = Node(name="root", contents=MMultiset())

        contents = MMultiset()
        contents.add('a', 1)
        contents.add('b', 4)
        s0 = Node(name="sub0", parent=root, contents=contents)

        e = Environment(tree=root, rules=ruleset, all_items=all_items)
        sim.environment = e
        sim.root = root

        return sim


# def set_cataysts()
# def set_rule_inputs()
# def set_rule_outputs()

def run1():
    sim = SimulationFactory.get_sim1()
    # sim.save("./output/run1.json")
    # TODO sim.load("./examples/run1.json")
    sim.run()


# --------------------


if __name__ == "__main__":
    run1()


# CURRENT STATE
#
# /usr/bin/python3.8 /home/mark/projects/baseline0/cyprus/malta/simulation.py
# running membrane simulation
# see output: ./sims/
# tick: 0
# sub0 has: {a, b, b, b, b}
# root has: {}
# tick: 1
# sub0 has: {a, b, b, b, b}
# root has: {}
# tick: 2
# sub0 has: {a, b, b, b, b}
# root has: {}
# tick: 3
# sub0 has: {a, b, b, b, b}
# root has: {}
# tick: 4
# sub0 has: {a, b, b, b, b}
# root has: {}
# tick: 5
# sub0 has: {a, b, b, b, b}
# root has: {}
# tick: 6
# sub0 has: {a, b, b, b, b}
# root has: {}
# tick: 7
# sub0 has: {a, b, b, b, b}
# root has: {}
# tick: 8
# sub0 has: {a, b, b, b, b}
# root has: {}
# tick: 9
# sub0 has: {a, b, b, b, b}
# root has: {}
# DONE.