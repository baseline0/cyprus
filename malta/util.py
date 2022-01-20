import json
import random
import string


def prettyprint_json(data):
    json.dumps(data, indent=4, sort_keys=True)


class NameGenerator:
    # use as prefix for cluster items

    def __init__(self) -> None:
        self.letters = string.ascii_lowercase

        self.num_chars = 4

    def get_rand_name(self) -> str:
        name = ''
        for i in range(self.num_chars):
            name += random.choice(self.letters)
        return name


name_gen = NameGenerator()
