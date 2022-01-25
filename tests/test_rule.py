import unittest

from multiset import Multiset

from malta.rule import Rule


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

    def test1(self):
        catalyst = Multiset()
        catalyst.add('a')

        rule_input = Multiset()
        rule_input.add('b', 3)

        rule_output = Multiset()
        rule_output.add('z', 10)

        r = Rule(name="test rule",
                 descr="abc",
                 catalyst=catalyst,
                 rule_input=rule_input,
                 rule_output=rule_output)

        out = json.dumps(r, default=lambda o: o.json_serialize(), indent=2)
        prettyprint_json(out)

        y = json.loads(out)

        print(y)
        self.assertTrue(y, r)