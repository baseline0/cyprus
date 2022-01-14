from cyprus.environment import Environment

from cyprus.base import get_base
base = get_base()

class Membrane(Environment):
  
  def dissolve(self):
    self.parent.contents.extend(self.contents)
    self.parent.membranes.remove(self)
    self.parent.membranes.extend(self.membranes)
    self.contents = []
    self.staging_area = []
    self.rules = []
  
    if self.name:
      del(base.cyprus_membrane_lookup_table[self.name])
  
  def printstatus(self, depth=0):
    indent = " " * (depth * 4)

    print(f'{indent} (name: {self.name}')
    print(f'{indent} symbols: {self.contents}')
    print(f'{indent} rules: {self.rules}')
    print(f'{indent} staging area: {self.staging_area}')

    print(f'{indent} Membranes:')
    for m in self.membranes:
      m.printstatus(depth + 1)
    print(f'{indent}')
