import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from funcparserlib.lexer import Token

from cyprus.base import get_base
base = get_base()

from cyprus.clock import CyprusClock as Clock
from cyprus.environment import Environment
from cyprus.membrane import  Membrane
from cyprus.particle import Particle
from cyprus.dissolve_particle import DissolveParticle
from cyprus.osmose_particle import OsmoseParticle
from cyprus.rule import Rule

from cyprus.parser import Statement, Program, Environment, Membrane
from cyprus.parser import flatten, Grouping

# -----------------

from funcparserlib.parser import (some, maybe, many, finished, skip, 
  with_forward_decls, oneplus, NoParseError)
from funcparserlib.lexer import Token
from funcparserlib.util import pretty_tree

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
  
  statement = with_forward_decls(lambda: membrane | expr) >> Statement
  
  body = maybe(name) + many(statement)
  
  membrane = (skip(membrane_open) + body + skip(membrane_close)) >> Membrane
  env = (skip(env_open) + body + skip(env_close)) >> Environment
  
  program = many(env) + skip(finished) >> Program
  
  return program.parse(tokens)

# pretty print a parse tree
def ptree(tree):

  def get_kids(x):
    if isinstance(x, Grouping):
      return x.kids
    else:
      return []

  def show(x):
    #print("show(%r)" % x
    if isinstance(x, Program):
      return '{Program}'
    elif isinstance(x, Environment):
      return '{Environment}'
    elif isinstance(x, Membrane):
      return '{Membrane}'
    elif isinstance(x, Statement):
      return '{Statement}'
    else:
      return repr(x)
  return pretty_tree(tree, get_kids, show)

# -----------------

from funcparserlib.lexer import make_tokenizer, Token, LexerError

ENCODING = 'utf-8'

def tokenize(str):
  'str -> Sequence(Token)'
  specs = [
    ('comment',                 (r'//.*',)),
    ('newline',                 (r'[\r\n]+',)),
    ('space',                   (r'[ \t\r\n]+',)),
    ('name',                    (r'(?!(?:as|exists|priority|reaction)\b)[A-Za-z\200-\377_]([A-Za-z\200-\377_0-9])*',)),
    ('kw_exists',               (r'exists',)),
    ('kw_reaction',             (r'reaction',)),
    ('kw_as',                   (r'as',)),
    ('kw_priority',             (r'priority',)),
    ('op_priority_maximal',     (r'>>',)),
    ('op_tilde',                (r'~',)),
    ('op_production',           (r'::',)),
    ('op_dissolve',             (r'\$',)),
    ('op_osmose_location',      (r'!!',)),
    ('op_osmose',               (r'!',)),
    ('mod_catalyst',            (r'\*',)),
    ('mod_charge_positive',     (r'\+',)),
    ('mod_charge_negative',     (r'-',)),
    ('env_open',                (r'\[',)),
    ('env_close',               (r'\]',)),
    ('membrane_open',           (r'\(',)),
    ('membrane_close',          (r'\)',)),
    ('number',                  (r'-?(\.[0-9]+)|([0-9]+(\.[0-9]*)?)',))
  ]
  useless = ['comment', 'space', 'newline']
  t = make_tokenizer(specs)
  return [x for x in t(str) if x.type not in useless]

def tokenizefile(f):
  return tokenize(open(f, 'r').read())

# -----------------

class CyprusProgram(object):

  # TODO
  # enum kw_exists

  def __init__(self, tree):
    
    self.tree = tree
    envs = self.objectify()
    self.clock = Clock(envs)
  
  def objectify(self):
    out = []
    for e in self.tree.kids:
      env = self.buildenvironment(e)
      out.append(env)
    return out
  
  def buildcontainer(self, e):

    name = None
    parent = None
    contents = []
    membranes = []
    rules = []
    stmts = []

    for x in e.kids:
      if isinstance(x, Token):
        name = x.value
      if isinstance(x, Statement):
        stmts.append(self.executestatement(x))

    stmts = flatten(stmts)
    for x in stmts:
      if isinstance(x, Membrane):
        membranes.append(x)

      if isinstance(x, Rule):
        rules.append(x)

      if isinstance(x, Particle):
        contents.append(x)

    return [name, parent, contents, membranes, rules]
  
  def buildenvironment(self, e):

    name, parent, contents, membranes, rules = self.buildcontainer(e)
    env = Environment(name, parent, contents, membranes, rules)
    
    if name:
      if base.membrane_table.get(name, None):
        msg = f"ERROR: Multiple containers defined with name: {name}"
        raise Exception(msg)
      base.membrane_table[name] = env
    return env
  
  def buildmembrane(self, e):

    name, parent, contents, membranes, rules = self.buildcontainer(e)
    mem = Membrane(name, parent, contents, membranes, rules)

    if name:
      if base.membrane_table.get(name, None):
        msg = f"ERROR: Multiple containers defined with name: {name}"
        raise Exception(msg)
      base.membrane_table[name] = mem

    return mem
  
  def executestatement(self, stmt):

    x = stmt.kids[0]

    if isinstance(x, Membrane):
      return self.buildmembrane(x)
    elif isinstance(x, Token):
      if x.type == 'kw_exists':
        return self.buildparticles(stmt)
      elif x.type == 'kw_reaction':
        return self.buildrule(stmt)
      elif x.type == 'kw_priority':
        self.setpriority(stmt)
        return None
      else:
        print(f"ERROR: {stmt}")
    else:
      print(f"ERROR: {stmt}")
  
  def buildparticles(self, stmt:Statement):

    particles = stmt.kids[2:]
    out = []

    for p in particles:
      out.append(Particle(p.value))
    return out
    
  def buildrule(self, stmt:Statement):

    name = None
    req = []
    out = []
    pri = 1

    particulars = stmt.kids[1:]
    if particulars[0] is None:
      particulars = particulars [2:]
    else:
      name = particulars[1].value
      particulars = particulars[3:]

    prod = False
    dissolve = False
    osmose = False
    osmosename = False
    osmoselocation = False

    for x in particulars:
      if x: ## error...
        if x.type == 'op_production':
          prod = True
          continue
        elif x.type == 'op_dissolve':
          dissolve = True
          continue
        elif x.type == 'op_osmose':
          osmose = True
          continue
      if dissolve:
        if not x:
          particle = DissolveParticle()
        else:
          particle = DissolveParticle(x.value)
        dissolve = False
      elif osmose:
        if not osmosename:
          osmosename = x.value
          continue
        if osmosename:
          if not x:
            particle = OsmoseParticle(osmosename)
            osmose, osmosename, osmoselocation = False, False, False
          elif x.type == 'op_osmose_location':
            continue
          else:
            osmoselocation = x.value
            particle = OsmoseParticle(osmosename, osmoselocation)
            osmose, osmosename, osmoselocation = False, False, False
      else:
        particle = Particle(x.value)
      if prod: 
          out.append(particle)
      else: 
          req.append(particle)

    rule = Rule(name, req, out, pri)

    if name:
      if base.rule_table.get(name, None):
        msg = "ERROR: Multiple reactions defined with name '%s'" % name
        raise Exception(msg)
      base.rule_table[name] = rule
    return rule
        
  def setpriority(self, stmt):
    # global cyprus_rule_lookup_table

    greatern, lessern = stmt.kids[2].value, stmt.kids[4].value
    greater = base.rule_table.get(greatern, None)
    lesser = base.rule_table.get(lessern, None)

    if not greater:
      msg = f"ERROR: No reactions defined with name {greatern}"
      raise Exception(msg)

    if not lesser:
      msg = f"ERROR: No reactions defined with name {lessern}"
      raise Exception(msg)

    if greater.priority <= lesser.priority:
      greater.priority += 1
  
  def run(self, verbose=False):
    # global cyprus_state_rule_applied

    if verbose: 
      self.clock.print_status()

    while cyprus_state_rule_applied:
      cyprus_state_rule_applied = False
      self.clock.tick()

      if verbose: 
        self.clock.print_status()

    self.clock.print_final_contents()

  @classmethod
  def print_tree(fname:str) -> None:      

    try:
      tokens = tokenizefile(fname)
      parsed = parse(tokens)
      tree = ptree(parsed) 
      print(tree)

    except NoParseError as e:
      print(f"Could not parse file: {e.msg}")
      
def parse_and_run_tree(fname:str, pverbose:bool) -> None:

  ## actual logic
  try:
    tokens = tokenizefile(fname)
    tree = parse(tokens)

  except NoParseError as e:
    print(f"Could not parse file: {e.args}")
    return

  try:
    p = CyprusProgram(tree)
    p.run(verbose=pverbose)

  except Exception as e:
    print(f'error running program: {e.args}')
