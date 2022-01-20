
from ast import Sub
import sys
import random
import string

import networkx as nx

from typing import TextIO
from enum import Enum

from dot_colour import DotColour


class NameGenerator:
    # use as prefix for cluster items

    def __init__(self) -> None:
        self.letters = string.ascii_lowercase   
        self.length = 10

    def get_rand_name(self) -> str:
        name = ''
        for i in range(self.length):
            name = name.join(random.choice(self.letters))
        return name


name_gen = NameGenerator()


def demo():

    from networkx.generators.random_graphs import random_lobster

    n = 10
    p1 = 0.5
    p2 = 0.7
    g = random_lobster(n, p1, p2, seed=None)

    adjacency_matrix = nx.adjacency_matrix(g)
    print(adjacency_matrix)

    # get a random graph
    # TODO


class ContentItem:
    def __init__(self, name:str=None, colour:DotColour=None) -> None:
        if name is None:
            self.name = name_gen.get_rand_name()
        else:
            self.name = name.replace(' ', '')

        #if colour is None:


class Base:

    def start(self, name: str = 'd') -> str:
        pass

    @classmethod
    def end(cls) -> str:
        pass

    def write_contents(self) -> str:
        pass

    def get_label(self) -> str:
        pass

def write_cluster(fp:TextIO, c: Base):

    try:

        fp.writelines(c.start())
    
        fp.writelines(f"{x} \n" for x in c.contents)

        for subcluster in c.clusters:
            write_cluster(fp, subcluster)

        fp.write(c.get_label())            
        fp.writelines(c.end())

    except IOError:
        sys.exit()


# TODO put in dotutils
class Subgraph(Base):
    
    START = "{"
    END = "}"

    def __init__(self, label=None) -> None:
        if label is None:
            self.label = name_gen.get_rand_name()
        else:
            self.label = label

    def start(self) -> str:
        return f"subgraph {self.label} " + Subgraph.START + '\n'

    @classmethod
    def end(cls) -> str:
        return Subgraph.END + '\n'


class Cluster(Base):

    START = "{"
    END = "}"

    def __init__(self, name=None, label=None) -> None:

        if name is None:
            self.name = name_gen.get_rand_name()
        else:
            # whitespace in names confounds dot
            self.name = name.replace(' ', '')

        # the cluster label in diagram
        if label is None:
            self.label = name
        else:            
            self.label = label 

        # nesting
        self.clusters = []

        # the objects in the membrane
        self.contents = []

    def add_cluster(self, c):
        self.clusters.append(c)

    def start(self) -> str:
        return f"subgraph cluster_{self.name} {Cluster.START} " + '\n'

    def get_label(self) -> str:
        if self.label is None:
            return ''
        else:
            s = f"label = \"{self.label}\""
            return s

    @classmethod
    def end(cls) -> str:
        return Cluster.END + '\n'


class Digraph:

    START = "{"
    END = "}"

    def __init__(self, label: str = 'd') -> None:
        self.label = label
        self.clusters = []

    @classmethod
    def start(cls, name: str = 'd') -> str:
        return f"digraph {name} " + Digraph.START + '\n'

    @classmethod
    def end(cls) -> str:
        return Digraph.END + '\n'

    def add_cluster(self, c: Cluster):
        self.clusters.append(c)


class DigraphGenerator:

    def __init__(self):
        self.digraph = Digraph()
        self.clusters = []
        self.fp = None

    def run(self, fname: str) -> None:     

        # use of writelines helps to avoid appending \n

        self.fp = open(fname, 'w')

        self.fp.writelines(self.digraph.start())

        for c in self.digraph.clusters:
            write_cluster(self.fp, c)

        self.fp.writelines(self.digraph.end())
        self.fp.close()


def demo1():
    # simple. small. nested one deep

        c = Cluster(name="top")
        c.contents = ['a', 'b', 'c']
        

        d = Cluster(name="nested")
        d.contents = ['d', 'e', 'f']
        
        c.add_cluster(d)

        dg = DigraphGenerator()
        dg.digraph.add_cluster(c)

        dg.run(fname='./viz/out/graph1.dot')


def demo2():
    
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


        dg = DigraphGenerator()
        dg.digraph.add_cluster(c)
        dg.digraph.add_cluster(peer)

        dg.run(fname='./viz/out/graph2.dot')


# --------------------        


if __name__ == "__main__":

    # demo1()
    demo2()

    # demo()
