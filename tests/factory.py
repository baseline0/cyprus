from typing import List

from malta.malta import MembraneItem, Membrane


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
