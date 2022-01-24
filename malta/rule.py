from malta.mmultiset import MMultiset


class Rule:

    __slots__ = ["name", "descr", "catalyst", "rule_input", "rule_output"]

    def __init__(self, name: str, descr: str, catalyst: MMultiset, rule_input: MMultiset, rule_output: MMultiset):

        if isinstance(name, dict):
            self.set_from_dict(d=name)
            return

        self.name = name
        self.descr = descr

        # what is necessary for the rule to fire but what is not consumed
        if catalyst is None:
            self.catalyst = MMultiset()
        else:
            self.catalyst = catalyst

        # what is consumed by the firing of the rule
        if rule_input is None:
            self.rule_input = MMultiset()
        else:
            self.rule_input = rule_input

        # what is produced by the firing of the rule
        if rule_output is None:
            self.rule_output = MMultiset()
        else:
            self.rule_output = rule_output

    def __repr__(self) -> str:
        s = "rule\n"
        s += f"\tcatalysts: {self.catalyst}\n"
        s += f"\tinput: {self.rule_input}\n"
        s += f"\toutput: {self.rule_output}\n"
        return s

    def set_from_dict(self, d: dict):

        if "name" in d.keys():
            self.name = d["name"]
        if "descr" in d.keys():
            self.descr = d["descr"]
        if "catalyst" in d.keys():
            self.catalyst = d["catalyst"]
        if "rule_input" in d.keys():
            self.rule_input = d["rule_input"]
        if "rule_output" in d.keys():
            self.rule_output = d["rule_output"]

    def json_serialize(self):
        d = {}

        d["name"] = self.name
        d["descr"] = self.descr
        d['catalyst'] = self.catalyst.__str__()
        d['rule_input'] = self.rule_input.__str__()
        d['rule_output'] = self.rule_output.__str__()

        return d

