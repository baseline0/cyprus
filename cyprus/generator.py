# a tool to create membranes for cyprus

from io import FileIO
from typing import TextIO

from string import ascii_lowercase


## grammar
#
# program        := {env}
# env            := "[", body, "]"
# membrane       := "(", body, ")"
# body           := <name>, {statement}
# statement      := membrane | expr
# expr           := exists | reaction | priority
# exists         := "exists", "~", name, {name}
# reaction       := "reaction", <"as", name>, "~", name, {name}, "::",
#                    {symbol} 
# priority       := "priority", "~", name, ">>", name
# name           := number | atom
# atom           := [A-Za-z], {[A-Za-z0-9]}
# number         := [0-9], {[0-9]} | {[0-9]}, ".", [0-9], {[0-9]}
# symbol         := atom | "!", name, <"!!", name> | "$", [name]

ENV_START   ="["
ENV_END     ="]"

MEM_START   ="("
MEM_END     =")"


class AtomConcept:
    def __init__(self, name:str) -> None:
        self.name=name

    def __repr__(self) -> str:
        return self.name

class AtomQuantity:
    def __init__(self, a:AtomConcept) -> None:
        self.atom = a
        self.count = 0

class Contents:
    # things that are in a environment or membrane at the start.

    def __init__(self) -> None:

        # a dict of tuples -the atom name and its quantity 
        self.inventory = {}

    def add(self, atom:AtomConcept, count:int):

        if count < 0:
            raise ValueError

        if atom.name not in self.inventory:
            self.inventory[atom.name] = count
        else:
            self.inventory[atom.name] = self.inventory[atom.name] + count


class MembraneConcept:

    def __init__(self):
        pass

    def __repr__(self) -> str:
        pass

    def to_file(self, fp:FileIO):
        pass


class RuleConcept:
    # for reactions

    def __init__(self) -> None:
        self.catalyst = []
        self.input = []
        self.output = []
        
    def __repr__(self) -> str:
        pass

class EnvironmentConcept:
    def __init__(self) -> None:
        self.membranes = []

        # a list of atoms
        self.contents = []
        
    def __repr__(self) -> str:
        pass

    def to_file(self, fp:TextIO) -> None:

        if fp is None:
            raise ValueError

        for m in self.membranes:
            m.to_file(fp)

        for c in self.contents:
            c.to_file(fp)


class Generator:

    def __init__(self) -> None:
        self.OUT_DIR="./sims/"

        self.envs = []
        
        self.n_atoms=0
        # self.n_membranes=0

    def set_n_atoms(self, num:int=10):

        if num < 0:
            raise ValueError

        if num > 26:
            print('max 26 atoms at this time')
            num = 26

        self.n_atoms=num
        self.atoms = []

        names = ascii_lowercase[:num]

        for n in names:
            self.atoms.append(AtomConcept(n))

    def generate_2_atom_rule(self):

        r = RuleConcept()




        return r


    def run(self, fname:str = "generated.cyp"):

        # generate:
        #   a random number of atoms
        #   a random number of membranes
        #   a random number of rules that convert atoms into other atoms with a catalyst (unchanging atom) 
        #   a random number of rules that dissolve a membrane
        #   a random number of rules that osmose (simplified: just move across membrane)
        #   TODO a random number of rules that osmose (actual gradient must exist for atom to move across membrane)
        
        print('')




        self.save(fname=fname)

    def save(self, fname_prefix:str):

        # write to file

        with open(self.OUT_DIR + fname_prefix + ".cyp", 'w') as fp:
            fp.write('hello')

            for e in self.envs:
                e.to_file(fp)


    def to_dot(self, fname_prefix:str):
        # write in dot format

        with open(fname_prefix + '.png', 'w') as fp:
            fp.write('digraph d {')

            fp.write('}')

def convert_dot_to_png(fname:str):

        import os
        os.system('dot -Tpng generated.dot -o generated.png')
