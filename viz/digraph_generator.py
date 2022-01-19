
import random
import string

import networkx as nx


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
    

# TODO put in dotutils

class Digraph:

    START = "{"
    END = "}"

    def __init__(self, label=None) -> None:
        self.label = label

    @classmethod
    def start(cls, name: str = 'd') -> str:
        return f"digraph {name} " + Digraph.START

    @classmethod
    def end(cls) -> str:
        return Digraph.END


class Subgraph:

    START = "{"
    END = "}"

    def __init__(self, label=None) -> None:
        if label is None:
            self.label = name_gen.get_rand_name()
        else:
            self.label = label

    @classmethod
    def start(cls, name: str = 'd') -> str:
        return f"subgraph {name} " + Subgraph.START

    @classmethod
    def end(cls) -> str:
        return '}'


class Cluster:

    START = "{"
    END = "}"

    def __init__(self, label=None) -> None:

        if label is None:
            self.label = name_gen.get_rand_name()
        else:
            self.label = label

    @staticmethod
    def start(name: str = 'd') -> str:
        return f"subgraph cluster_{name} " + Subgraph.START

    @classmethod
    def end(cls) -> str:
        return Cluster.END


class DigraphGenerator:

    @staticmethod
    def run() -> None:
        # use of writelines helps to avoid \n

        with open('graph1.dot', 'w') as fp:
            fp.writelines('digraph d {')

            fp.writelines('}')

# --------------------        


if __name__ == "__main__":

    # gen = digraph_generator()
    # gen.run()

    demo()
