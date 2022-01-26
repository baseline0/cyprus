import json
import random
import string
from string import ascii_lowercase
from typing import List


def prettyprint_json(data):
    json.dumps(data, indent=4, sort_keys=True)


class NameGenerator:
    # use as prefix for cluster items

    @staticmethod
    def get_rand_name(letters=string.ascii_lowercase, num_chars: int = 4, prefix: str = None) -> str:
        if prefix:
            name = prefix + '_'
        else:
            name = ''

        for i in range(num_chars):
            name += random.choice(letters)
        return name


def get_alphabet1(num: int) -> List[str]:
    """
    return a list of 1 character strings
    """

    if num > 26:
        num = 26
        print('limiting to ascii lowercase. write a new alphabet getter')

    return ascii_lowercase[0:num - 1]
