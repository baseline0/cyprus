from lib2to3.pgen2.token import STAR
import random
import string

class name_generator:
    # use as prefix for cluster items

    def __init__(self) -> None:
        self.letters = string.ascii_lowercase   
        self.length = 10

    def rand_name(self) -> str:
        name = ''.join(random.choice(self.letters) for i in range(self.length))
        return name

name_gen = name_generator()


import networkx as nx

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

class digraph:

    START="{"
    END="}"

    def __init__(self, label=None) -> None:
        self.label = label

    @classmethod
    def start(name:str='d') -> str:
        return f"digraph {name} " + digraph.START

    @classmethod
    def end() -> str:
        return digraph.END


class subgraph:

    START="{"
    END="}"

    def __init__(self, label=None) -> None:
        if label is None:
            label = name_gen.rand_name()
        else:
            self.label = label

    @classmethod
    def start(name:str='d') -> str:
        return f"subgraph {name} " + subgraph.START



    @classmethod
    def end() -> str:
        return '}'

class cluster:

    START="{"
    END="}"

    def __init__(self, label=None) -> None:

        if label is None:
            label = name_gen.rand_name()
        else:
            self.label = label

    def start(self, name:str='d') -> str:
        return f"subgraph cluster_{name} " + subgraph.START



    @classmethod
    def end() -> str:
        return cluster.END



class digraph_generator:
    

    def run(self)-> None: 
        # use of writelines helps to avoid \n

        with open('graph1.dot', 'w') as fp:
            fp.writelines('digraph d {')




            fp.writelines('}')

# --------------------        

if __name__ == "__main__":

    # gen = digraph_generator()
    # gen.run()

    demo()