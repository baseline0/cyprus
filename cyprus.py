#!/use/bin/python

import sys, getopt

from funcparserlib.parser import NoParseError
from cyprus.base import Base
from cyprus.program import CyprusProgram as Program


def usage():
  print("usage: python cyprus.py [-p | -V] <filename.cyp>")
  print("       python cyprus.py -v")
  print("       python cyprus.py -h")
  print("  -p: pretty-print(a parse tree and exit")
  print("  -V: display verbose output of the program's execution")
  print("  -v: display version info and exit")
  print("  -h: display this help text and exit")
  
def version():  
  cyprus_version = 20220113
  print("cyprus version %s" % cyprus_version)
  print("Jacob Peck (suspended-chord)")
  print("   http://github.com/gatesphere/cyprus")
  print("fork for python3:")
  print("   http://github.com/baseline0/cyprus")

# -----------------

if __name__ == '__main__':

  from cyprus.base import Base
  base = Base()

  args = sys.argv[1:]

  try:
    opts, args = getopt.getopt(args, 'pVvh')
  except:
    usage()
    sys.exit()

  ptree, pversion, phelp, pverbose = False, False, False, False
  for opt, a in opts:
    if   opt == '-p': 
      ptree = True
    elif opt == "-V": 
      pverbose = True
    elif opt == '-v': 
      pversion = True
    elif opt == '-h': 
      phelp = True

  if pversion:
    version()
    sys.exit()

  if len(args) != 1 or phelp:
    usage()
    sys.exit()
  
  filename = args[0]
  
  if ptree:
    Program.print_tree(filename)
    sys.exit()
  
  from cyprus.program import parse_and_run_tree
  
  parse_and_run_tree(filename, 
    pverbose=pverbose)
  
  sys.exit()
