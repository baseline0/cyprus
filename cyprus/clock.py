# the clock, governs the system's operation
class CyprusClock(object):
  def __init__(self, envs):
    self._tick = 0
    self.envs = envs
  
  def printstatus(self):
    print("Clock tick: %s" % self._tick)
    for e in self.envs: e.printstatus()
  
  def printfinalcontents(self):
    for e in self.envs:
      if e.name:
        print("%s: %s" % (e.name, e.contents))
      else:
        print("Unnamed env %d: %s" % (self.envs.index(e), e.contents))
  
  def tick(self):
    self._tick += 1
    for e in self.envs:
      e.tick()