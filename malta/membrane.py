from malta.mmultiset import MMultiset

from typing import List


class Membrane:
    """
    contents is a list of strings that are the names of the membrane items
    contents needs to be a multiset so it is compatible with set operations for rules.
    """
    # https://pythonhosted.org/multiset/

    __slots__ = ["name", "descr", "contents"]

    def __init__(self, name: str, descr: str, contents=List[str]):
        # =List[MembraneItem]):
        if  isinstance(name, str):
            self.name = name
        else:
            raise ValueError

        self.descr = descr

        # We expect a Multiset where the items in the multiset are the names of the corresponding
        # MembraneItems
        if not isinstance(contents, MMultiset):
            raise ValueError
        else:
            self.contents = contents

    def json_serialize(self) -> dict:
        d = {}
        d["name"] = self.name
        d["descr"] = self.descr
        d["contents"] = self.contents
        return d


def deserialize(d: dict) -> Membrane:
    m = Membrane()

    if "name" in d.keys():
        m.name = d["name"]

    if "descr" in d.keys():
        m.descr = d["descr"]

    if "contents" in d.keys():
        m.contents = d["contents"]

    return m
