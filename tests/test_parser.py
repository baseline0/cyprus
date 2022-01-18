import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from cyprus.program import parse, get_pretty_tree
from cyprus.program import tokenize_file
from funcparserlib.parser import NoParseError

import unittest

class ParseTest(unittest.TestCase):

  def test1(self):

    try:
      tree = parse(tokenize_file('./tests/examples/example1.cyp'))  
      print(get_pretty_tree(tree))
    except NoParseError as e:
      print(e)


# E{Program}
# `-- {Environment}
#     |-- Token('name', 'env')
#     `-- {Statement}
#         `-- {Membrane}
#             |-- Token('number', '1')
#             |-- {Statement}
#             |   `-- {Membrane}
#             |       |-- Token('number', '2')
#             |       |-- {Statement}
#             |       |   `-- {Membrane}
#             |       |       |-- Token('number', '3')
#             |       |       |-- {Statement}
#             |       |       |   |-- Token('kw_exists', 'exists')
#             |       |       |   |-- Token('op_tilde', '~')
#             |       |       |   |-- Token('name', 'a')
#             |       |       |   `-- Token('name', 'c')
#             |       |       |-- {Statement}
#             |       |       |   |-- Token('kw_reaction', 'reaction')
#             |       |       |   |-- None
#             |       |       |   |-- Token('op_tilde', '~')
#             |       |       |   |-- Token('name', 'a')
#             |       |       |   |-- Token('op_production', '::')
#             |       |       |   |-- Token('name', 'a')
#             |       |       |   `-- Token('name', 'b')
#             |       |       |-- {Statement}
#             |       |       |   |-- Token('kw_reaction', 'reaction')
#             |       |       |   |-- None
#             |       |       |   |-- Token('op_tilde', '~')
#             |       |       |   |-- Token('name', 'a')
#             |       |       |   |-- Token('op_production', '::')
#             |       |       |   |-- Token('name', 'b')
#             |       |       |   |-- Token('op_dissolve', '$')
#             |       |       |   `-- None
#             |       |       `-- {Statement}
#             |       |           |-- Token('kw_reaction', 'reaction')
#             |       |           |-- None
#             |       |           |-- Token('op_tilde', '~')
#             |       |           |-- Token('name', 'c')
#             |       |           |-- Token('op_production', '::')
#             |       |           |-- Token('name', 'c')
#             |       |           `-- Token('name', 'c')
#             |       |-- {Statement}
#             |       |   |-- Token('kw_reaction', 'reaction')
#             |       |   |-- None
#             |       |   |-- Token('op_tilde', '~')
#             |       |   |-- Token('name', 'b')
#             |       |   |-- Token('op_production', '::')
#             |       |   `-- Token('name', 'd')
#             |       |-- {Statement}
#             |       |   |-- Token('kw_reaction', 'reaction')
#             |       |   |-- None
#             |       |   |-- Token('op_tilde', '~')
#             |       |   |-- Token('name', 'd')
#             |       |   |-- Token('op_production', '::')
#             |       |   |-- Token('name', 'd')
#             |       |   `-- Token('name', 'e')
#             |       |-- {Statement}
#             |       |   |-- Token('kw_reaction', 'reaction')
#             |       |   |-- Token('kw_as', 'as')
#             |       |   |-- Token('name', 'c1')
#             |       |   |-- Token('op_tilde', '~')
#             |       |   |-- Token('name', 'c')
#             |       |   |-- Token('name', 'c')
#             |       |   |-- Token('op_production', '::')
#             |       |   `-- Token('name', 'c')
#             |       |-- {Statement}
#             |       |   |-- Token('kw_reaction', 'reaction')
#             |       |   |-- Token('kw_as', 'as')
#             |       |   |-- Token('name', 'c2')
#             |       |   |-- Token('op_tilde', '~')
#             |       |   |-- Token('name', 'c')
#             |       |   |-- Token('op_production', '::')
#             |       |   |-- Token('op_dissolve', '$')
#             |       |   `-- None
#             |       `-- {Statement}
#             |           |-- Token('kw_priority', 'priority')
#             |           |-- Token('op_tilde', '~')
#             |           |-- Token('name', 'c1')
#             |           |-- Token('op_priority_maximal', '>>')
#             |           `-- Token('name', 'c2')
#             `-- {Statement}
#                 |-- Token('kw_reaction', 'reaction')
#                 |-- None
#                 |-- Token('op_tilde', '~')
#                 |-- Token('name', 'e')
#                 |-- Token('op_production', '::')
#                 |-- Token('op_osmose', '!')
#                 |-- Token('name', 'e')
#                 `-- None
