# the clock, governs the system's operation
class CyprusClock(object):

  def __init__(self, envs):
    # list of envs
    self._tick = 0
    self.envs = envs
  
  def print_status(self):
    print(f"Clock tick: {self._tick}")

    for e in self.envs: 
      e.print_status()
  
  def print_final_contents(self):
    for e in self.envs:
      if e.name:
        print(f"{e.name}: {e.contents}")
      else:
        print(f"Unnamed env {self.envs.index(e)}: {e.contents}")
  
  def tick(self):
    self._tick += 1

    for e in self.envs:
      e.tick()
