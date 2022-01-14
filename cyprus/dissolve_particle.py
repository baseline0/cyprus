from cyprus.particle import CyprusParticle as Particle


class CyprusDissolveParticle(Particle):

  def __init__(self, target=None):
    self.target = target
    
  def __str__(self):
    if self.target:
     return "$%s" % self.target
    else:
      return "$"
  
  def __eq__(self, other):
    if isinstance(other, CyprusDissolveParticle):
      return other.target == self.target
    else:
      return False
