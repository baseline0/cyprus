import unittest

from multiset import Multiset

from malta.malta import Rule


class TestRule(unittest.TestCase):

    def test_multiset(self):
        # basics of multiset. yes use this.
        #
        # initial membrane has:
        #     {a, b, b, c, c, c}
        # catalyst is:
        #     {a}
        # rule input is:
        #     {b, b}
        # rule output is:
        #     {e, x, y}
        # final membrane has:
        #     {a, c, c, c, e, x, y}

        # the membrane contents
        membrane_contents = Multiset()
        membrane_contents.add('a')
        membrane_contents.add('b', 2)
        membrane_contents.add('c', 3)

        print(f"initial membrane has: {membrane_contents}")

        # the rule catalyst
        catalyst = Multiset()
        catalyst.add('a')
        print(f"catalyst is: {catalyst}")

        self.assertTrue(catalyst.issubset(membrane_contents))

        # the rule input
        rule_input = Multiset()
        rule_input.add('b', 2)
        print(f"rule input is: {rule_input}")

        self.assertTrue(rule_input.issubset(membrane_contents))

        membrane_contents.difference_update(rule_input)
        expected = Multiset()
        expected.add('a')
        expected.add('c', 3)
        self.assertEqual(membrane_contents, expected)

        # the rule output
        output = Multiset()
        output.add('e')
        output.add('x')
        output.add('y')
        print(f"rule output is: {output}")

        membrane_contents += output

        # the membrane after the rule is applied
        print(f"final membrane has: {membrane_contents}")

    def test_rules(self):
        # r = Rule()
        # print(r)
        pass