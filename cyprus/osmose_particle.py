from cyprus.particle import CyprusParticle as Particle


class CyprusOsmoseParticle(Particle):

  def __init__(self, payload, target=None):
    self.payload = payload
    self.target = target
    
  def __str__(self):
    if self.target:
      return "!%s!!%s" % (self.payload, self.target)
    else:
      return "!%s" % self.payload
  
  def __eq__(self, other):
    if isinstance(other, CyprusOsmoseParticle):
      return (self.target, self.payload) == (other.target, other.payload)
    else:
      return False
