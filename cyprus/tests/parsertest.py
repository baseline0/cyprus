import sys
sys.path.append('..')

from cyprus.program import parse, ptree
from cyprus.program import tokenizefile
from funcparserlib.parser import NoParseError

import unittest

class ParseTest(unittest.TestCase):

  def test1(self):

    try:
      tree = parse(tokenizefile('test.cyp'))  
      print(ptree(tree))
    except NoParseError as e:
      print(e)
