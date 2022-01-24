import unittest

import json
import jsons

from typing import List

from tests.factory import Factory

from util import prettyprint_json
from mmultiset import Multiset
from malta.malta import Rule
from malta.malta import Membrane, MembraneItem


class TestMalta(unittest.TestCase):

    def test_serialize_membrane_item(self):
        def as_membrane_item(d: dict = None):
            if '__MembraneItem__' in d:
                return MembraneItem(name=d["name"])
            return d

        mi = MembraneItem(name="gold", descr="ounces")
        out = json.dumps(mi, indent=4, default=lambda o: o.json_serialize())
        print(out)
        # y = json.loads(out, object_hook=as_membrane_item())
        # y = json.loads(out, object_hook=lambda d: membrane_item_deserialize(dict))

        # works w hack isinstance in __init__
        y = json.loads(out)
        print(y)

        # AssertionError: 'gold' != {'name': 'gold', 'symbol': 'gold', 'descr': 'ounces', 'colour': "['wheat2']"}
        self.assertEqual(mi.name, y["name"])


class TestRules(unittest.TestCase):

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


class TestMembrane(unittest.TestCase):

    def test1(self):
        m = Factory.get_membrane_example1()

        out = json.dumps(m, default=lambda o: o.json_serialize(), indent=2)
        prettyprint_json(out)

        y = json.loads(out)

        print(y)
        self.assertTrue(y, m)
