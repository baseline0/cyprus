import unittest

# get a simulation.
# run it to completion.
# confirm end state is as expected

from malta.membrane_item import MembraneItem
from simulation import get_item_names_from_membrane_items


class TestSimulation(unittest.TestCase):

    def test1(self):

        mi1 = MembraneItem('b', descr='broccoli')
        mi2 = MembraneItem('c', descr='carrot')
        membrane_contents = [mi1, mi2]

        ids_only = get_item_names_from_membrane_items(membrane_contents)

        expected = ['b', 'c']

        self.assertEqual(ids_only, expected)
