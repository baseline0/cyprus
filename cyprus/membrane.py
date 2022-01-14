from cyprus.environment import CyprusEnvironment as Environment


class CyprusMembrane(Environment):
  
  # def __init__(self, name, parent, contents, membranes, rules) -> None:
  #   global sim
  #   self.sim = sim

  def dissolve(self):
    self.parent.contents.extend(self.contents)
    self.parent.membranes.remove(self)
    self.parent.membranes.extend(self.membranes)
    self.contents = []
    self.staging_area = []
    self.rules = []
  
    if self.name:
      del(self.sim.cyprus_membrane_lookup_table[self.name])
  
  def printstatus(self, depth=0):
    spaces = " " * (depth * 4)
    print(f'{spaces} (name: {self.name}')
    print(f'{spaces} symbols: {self.contents}')
    print(f'{spaces} rules: {self.rules}')
    print(f'{spaces} staging area: {self.staging_area}')

    print(f'{spaces} Membranes:')
    for m in self.membranes:
      m.printstatus(depth + 1)
    print(f'{spaces}')
