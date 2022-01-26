import unittest

import json
from malta.factory import Factory
from malta.util import prettyprint_json
from malta.membrane_item import MembraneItem


class TestMembraneItem(unittest.TestCase):

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


class TestMembrane(unittest.TestCase):

    def test1(self):
        m = Factory.get_membrane_example1()

        out = json.dumps(m, default=lambda o: o.json_serialize(), indent=2)
        prettyprint_json(out)

        y = json.loads(out)

        print(y)
        self.assertTrue(y, m)

