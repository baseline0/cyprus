from funcparserlib.parser import (some, maybe, many, finished, skip, 
  with_forward_decls, oneplus, NoParseError)
from funcparserlib.lexer import Token


def flatten(x):
  result = []

  for el in x:
    if hasattr(el, "__iter__") and not isinstance(el, str):
      result.extend(flatten(el))
    else:
      result.append(el)

  return result


class Grouping(object):
  
  def __init__(self, kids):
    try:
      self.kids = list(flatten([kids]))
    except TypeError:
      self.kids = [kids]

class ProgramGroup(Grouping):
  pass
  
class EnvironmentGroup(Grouping):
  pass
  
class MembraneGroup(Grouping):
  pass

class StatementGroup(Grouping):
  pass


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

tokval = lambda tok: tok.value
toktype = lambda type: lambda tok: tok.type == type
make_number = lambda str: float(str)


def parse(tokens):
  ## building blocks
  kw_priority = some(toktype("kw_priority"))
  kw_probability = some(toktype("kw_probability"))
  kw_reaction = some(toktype("kw_reaction"))
  kw_exists = some(toktype("kw_exists"))
  kw_as = some(toktype("kw_as"))
  op_tilde = some(toktype("op_tilde"))
  op_priority_maximal = some(toktype("op_priority_maximal"))
  op_production = some(toktype("op_production"))
  atom = some(toktype("name"))
  number = some(toktype("number"))
  dissolve = some(toktype("op_dissolve"))
  osmose = some(toktype("op_osmose"))
  osmose_location = some(toktype("op_osmose_location"))
  env_open = some(toktype("env_open"))
  env_close = some(toktype("env_close"))
  membrane_open = some(toktype("membrane_open"))
  membrane_close = some(toktype("membrane_close"))
  
  ## grammar from the bottom up
  name = atom | number
  symbol = atom | (dissolve + maybe(name)) | (osmose + name + maybe(osmose_location + name))
  
  priority = kw_priority + op_tilde + name + op_priority_maximal + name
  
  reaction = (kw_reaction + maybe(kw_as + name) + op_tilde + 
             oneplus(name) + op_production + many(symbol))
  
  exists = kw_exists + op_tilde + oneplus(name)
  
  expr = (exists | reaction | priority)
  
  statement = with_forward_decls(lambda: membrane | expr) >> StatementGroup
  
  body = maybe(name) + many(statement)
  
  membrane = (skip(membrane_open) + body + skip(membrane_close)) >> MembraneGroup
  env = (skip(env_open) + body + skip(env_close)) >> EnvironmentGroup
  
  program = many(env) + skip(finished) >> ProgramGroup
  
  return program.parse(tokens)
