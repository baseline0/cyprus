from cyprus.parser import Grouping, ProgramGroup, StatementGroup, EnvironmentGroup, MembraneGroup

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
    if isinstance(x, ProgramGroup):
      return '{Program}'
    elif isinstance(x, EnvironmentGroup):
      return '{Environment}'
    elif isinstance(x, MembraneGroup):
      return '{Membrane}'
    elif isinstance(x, StatementGroup):
      return '{Statement}'
    else:
      return repr(x)

  return pretty_tree(tree, kids, show)
