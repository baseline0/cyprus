# a tool to create membranes for cyprus

from typing import TextIO


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

    def to_file(self, fp:)


class RuleConcept:
    # for reactions

    def __init__(self) -> None:
        pass
        
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
        

    def run(self, fname:str):
        # write to file

        with open(self.OUT_DIR + fname, 'w') as fp:
            fp.write('hello')

            for e in self.envs:
                e.to_file(fp)


