import unittest

from malta.environment import Environment, apply
from malta.membrane import Membrane
from malta.mmultiset import MMultiset
from malta.rule import Rule
from membrane_item import MembraneItem
from simulation import get_multiset_of_item_names_from_membrane_items


class TestEnvironment(unittest.TestCase):

    # def test1(self):
    #     e = Environment()

    def test_apply_rule(self):

        mi1 = MembraneItem('b', descr='broccoli')
        mi2 = MembraneItem('c', descr='carrot')
        contents = get_multiset_of_item_names_from_membrane_items([mi1, mi2])
        m = Membrane(name='m1', descr='hello', contents=contents)

        r_catalyst = MMultiset()
        r_catalyst.add('b')

        r_input = MMultiset()
        r_input.add('c')

        r_output = MMultiset()
        r_output.add('w')

        r = Rule(name='r1', descr='', catalyst=r_catalyst, rule_input=r_input, rule_output=r_output)

        apply(r, m)

        # expected end state:
        #   catalyst b is preserved
        #   the presence of catalyst (b) and rule input (c) causes rule to fire.
        #   the firing of the rule consumes (c) and produces w
        expected = MMultiset()
        expected.add('b')
        expected.add('w')
        self.assertEqual(m.contents, expected)
