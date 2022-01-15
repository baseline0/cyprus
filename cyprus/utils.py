from cyprus.parser import Grouping, SimulationProgram, Statement, Environment, Membrane

from funcparserlib.util import pretty_tree

# pretty print a parse tree
def get_pretty_tree(tree):

  def kids(x):
    if isinstance(x, Grouping):
      return x.kids
    else:
      return []

  def show(x):
    #print("show(%r)" % x
    if isinstance(x, SimulationProgram):
      return '{Program}'
    elif isinstance(x, Environment):
      return '{Environment}'
    elif isinstance(x, Membrane):
      return '{Membrane}'
    elif isinstance(x, Statement):
      return '{Statement}'
    else:
      return repr(x)

  return pretty_tree(tree, kids, show)
