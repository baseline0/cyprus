import sys
sys.path.append('..')

import unittest

from cyprus.program import tokenizefile

class LexerTest(unittest.TestCase):

  def test_unicode(self):  

    ts = tokenizefile('test.cyp')
    for t in ts:
      print(t.__unicode__())
