import json
import unittest
from dataclasses import dataclass

import jsons
from dataclasses_json import dataclass_json
from multiset import Multiset


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


class TestBasic(unittest.TestCase):
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
        # works. use this.

        class Foo2(Multiset):
            __slots__ = ['m']

            def __init__(self):
                Multiset.__init__(self)
                self.m = Multiset()

            def json_serialize(self):
                return {'m': self.m.__str__()}

        y = json.dumps(Foo2(), default=lambda o: o.json_serialize())
        print(f"Foo2 multiset: {y}")

        x = json.loads(y)  # , object_hook=Foo2)
        print(x)
