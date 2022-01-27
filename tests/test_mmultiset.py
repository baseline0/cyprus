import json
import unittest

from multiset import Multiset

from malta.mmultiset import multiset_to_dict, json_serialize


class TestMMultiset(unittest.TestCase):

    def test_dict(self):
        m = Multiset()
        m.add('a')
        m.add('b', 2)
        m.add('c', 3)
        print(m)

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
