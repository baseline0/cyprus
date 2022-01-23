import unittest

# from malta.malta import Rule
from multiset import Multiset
from malta.malta import MembraneItem
from malta.malta import multiset_to_dict
import json

import jsons

from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass
class Shape:
    # https://jsons.readthedocs.io/en/latest/faq.html#why-not-just-use-dict

    name: str
    area: float


@dataclass_json
@dataclass
class Shape2:
    # https://pypi.org/project/dataclasses-json/
    int_field: int

    # def __init__(self, val: int):
    #     self.int_field = val


class TestMalta(unittest.TestCase):

    def test_rules(self):
        # r = Rule()
        # print(r)
        pass

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

    def test_dict(self):
        m = Multiset()
        m.add('a')
        m.add('b', 2)
        m.add('c', 3)
        print(m)

        from malta.malta import json_serialize

        x = json.dumps(m, default=lambda o: json_serialize(o))
        print(f"X IS: {x}")
        # with open('multiset.json', 'w') as f:
        #     json.dump(m.__str__, f, indent=2)

    def test_multiset_to_dict(self):
        m = Multiset()
        m.add('a')
        d = multiset_to_dict(m)
        expected = {'a': 1}
        self.assertEqual(d, expected)
        print(d)

    def test_jsons(self):
        # https://pypi.org/project/jsons/

        b = Shape('triangle', 3.2)
        out = jsons.dump(b)
        print(out)

        c = jsons.load(out, Shape)
        self.assertTrue(b, c)

    def test_shape2(self):
        x = Shape2(1)

        # Encoding to JSON. Note the output is a string, not a dictionary.
        y = x.to_json()  # {"int_field": 1}
        print(y)

        # Encoding to a (JSON) dict
        y = x.to_dict()  # {'int_field': 1}
        print(y)

        # Decoding from JSON. Note the input is a string, not a dictionary.
        y = x.from_json('{"int_field": 1}')  # SimpleExample(1)
        print(y)

        # Decoding from a (JSON) dict
        y = x.from_dict({'int_field': 1})  # SimpleExample(1)
        print(y)

    def test_foo(self):
        class Foo:
            __slots__ = ["bar"]

            def __init__(self):
                self.bar = 0

            def json_serialize(self):
                return {'bar': self.bar}

        y = json.dumps(Foo(), default=lambda o: o.json_serialize())
        print(y)

    def test_foo2(self):
        __slots__ = ['m']

        # works. use this.

        class Foo2(Multiset):

            def __init__(self):
                Multiset.__init__(self)
                self.m = Multiset()

            def json_serialize(self):
                return {'m': self.m.__str__()}

        y = json.dumps(Foo2(), default=lambda o: o.json_serialize())
        print(f"Foo2 multiset: {y}")

        x = json.loads(y) #, object_hook=Foo2)
        print(x)

    def test_serialize_membrane_item(self):
        def as_membrane_item(d: dict = None):
            if '__MembraneItem__' in d:
                return MembraneItem(name=d["name"])
            return d

        mi = MembraneItem(name="gold", descr="ounces")
        out = json.dumps(mi, indent=4, default=lambda o: o.json_serialize())
        print(out)
        # y = json.loads(out, object_hook=as_membrane_item())
        y = json.loads(out) # , object_hook=MembraneItem)
        print(y)

        # AssertionError: 'gold' != {'name': 'gold', 'symbol': 'gold', 'descr': 'ounces', 'colour': "['wheat2']"}
        self.assertEqual(mi.name, y["name"])
