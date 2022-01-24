from typing import List

from malta.environment import Environment
from malta.dot_colour import get_rand_colour
from malta.dot import ContentItem
from malta.membrane_item import MembraneItem
from malta.membrane import Membrane
from malta.util import NameGenerator


class Factory:
    """
    provide known and constructed examples of key classes for tests
    """

    @staticmethod
    def get_membrane_item1() -> MembraneItem:
        mi = MembraneItem(name="factory", descr="units")
        return mi

    @staticmethod
    def get_membrane_item_collection1() -> List[MembraneItem]:
        """
        digital ag genomics
        """
        mi1 = MembraneItem(name="parent1", descr="germplasm")
        mi2 = MembraneItem(name="parent2", descr="germplasm")
        mi3 = MembraneItem(name="F1", descr="germplasm")
        mi4 = MembraneItem(name="F2", descr="germplasm")
        mi5 = MembraneItem(name="F3", descr="germplasm")
        return [mi1, mi2, mi3, mi4, mi5]

    @staticmethod
    def get_membrane_example1() -> Membrane:
        m = Membrane(name='example1', descr='test json ops')
        membrane_items = Factory.get_membrane_item_collection1()

        num = 1
        for mi in membrane_items:
            m.contents.add(mi.name, num)
            num += 1

        return m

    @staticmethod
    def get_rand_membrane_item() -> MembraneItem:
        name = NameGenerator.get_rand_name()
        mi = MembraneItem(name=name, descr=name, colour=get_rand_colour())
        return mi

    @staticmethod
    def get_environment1() -> Environment:
        e = Environment()
        return e


class ContentItemFactory:

    @classmethod
    def get_items_for_names(cls, names, colour: str = None):  # -> List(ContentItem):
        # all same colour
        items = []
        if colour is None:
            colour = get_rand_colour()

        for n in names:
            items.append(ContentItem(name=n, colour=colour))
        return items

    @classmethod
    def get_items(cls, n: int = 10, colour: str = None):  # -> List(ContentItem):
        # same colour

        items = []

        if colour is None:
            colour = get_rand_colour()

        for n in range(n):
            items.append(ContentItem(colour=colour))
        return items

    # @staticmethod
    # def get_multi_coloured_items(n: int = 10):
    #     # TODO