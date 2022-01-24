import json

from malta.environment import Environment
from malta.membrane_item import MembraneItem
from malta.membrane import Membrane
from malta.mmultiset import MMultiset
from malta.rule import Rule
from malta.ruleset import RuleSet
from malta.util import prettyprint_json


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


class SimulationFactory:

    @staticmethod
    def get_sim1() -> Simulation:
        sim = Simulation()

        mi1 = MembraneItem('b', descr='broccoli')
        mi2 = MembraneItem('c', descr='carrot')
        membrane_contents = [mi1, mi2]
        m = Membrane(name='m1', descr='hello', contents=membrane_contents)

        r_catalyst = MMultiset()
        r_catalyst.add('b')

        r_input = MMultiset()
        r_input.add('c')

        r_output = MMultiset()
        r_output.add('w')

        r = Rule(name='r1', descr='', catalyst=r_catalyst, rule_input=r_input, rule_output=r_output)

        env_contents = MembraneItem(name='a', descr='apple')

        ruleset = RuleSet()
        ruleset.rules = [r]

        e = Environment(membranes=[m], rules=ruleset, contents=[env_contents])
        sim.membrane_env = e

        return sim


def run1():

    sim = SimulationFactory.get_sim1()
    # sim.save("./output/run1.json")
    # TODO sim.load("./examples/run1.json")
    sim.run()

# --------------------


if __name__ == "__main__":
    run1()
