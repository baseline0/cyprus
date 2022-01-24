from malta.mmultiset import MMultiset


class Membrane:
    # https://pythonhosted.org/multiset/

    __slots__ = ["name", "descr", "contents"]

    def __init__(self, name: str, descr: str = None, contents=None):
        # =List[MembraneItem]):
        if  isinstance(name, str):
            self.name = name
        else:
            raise ValueError

        self.descr = descr

        # We expect a multiset of MembraneItems
        if contents is None:
            self.contents = MMultiset()  # adds json_serialize
            # self.contents = Multiset()
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
