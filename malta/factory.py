from typing import List
from malta.dot import Cluster


class Factory:

    @classmethod
    def get_cluster_1(cls) -> Cluster:
        # simple. small. nested one deep

        c = Cluster(name="top")
        c.contents = ['a', 'b', 'c']

        d = Cluster(name="nested")
        d.contents = ['d', 'e', 'f']

        c.add_cluster(d)

        return c

    @classmethod
    def get_cluster_2(cls) -> List[Cluster]:

        c = Cluster(name="top")
        c.contents = ['a', 'b', 'c']

        peer = Cluster(name="peer")
        peer.contents = ['a1', 'b1', 'c1']

        d = Cluster(name="nested")
        d.contents = ['d', 'e', 'f']

        e = Cluster(name="nested_2")
        e.contents = ['g', 'h', 'i']

        d.add_cluster(e)
        c.add_cluster(d)

        return [c, peer]
