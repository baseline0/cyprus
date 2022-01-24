from typing import List

from malta.rule import Rule


class RuleSet:

    def __init__(self):

        # the list of symbols which are valid
        # this is the list of all catalysts, inputs and outputs
        self.alphabet = []

        # the set of rules
        self.rules = []

    def set_alphabet(self, alphabet: List[str]) -> None:
        self.alphabet = alphabet

    def set_rules(self, rules: List[Rule]) -> None:

        self.rules = rules

        if not self.alphabet:
            # if None or empty list
            # generate the alphabet from their presence in rules
            self.detect_alphabet_from_rules()
            # end state: alphabet and rules are consistent
        else:
            # ensure that the rules match the already existing alphabet
            for r in rules:
                # TODO
                print(r)

    def detect_alphabet_from_rules(self):

        self.alphabet = []

        temp = set()

        for r in self.rules:
            for c in r.catalyst:
                temp.update(c)
            for c in r.input:
                temp.update(c)
            for c in r.output:
                temp.update(c)

        self.alphabet = list(temp)
