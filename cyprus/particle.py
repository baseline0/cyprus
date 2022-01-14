class CyprusParticle(object):

  def __init__(self, name, charge=''):
    self.name = name
    self.charge = charge
    
  def __str__(self):
    return "%s%s" % (self.name, self.charge)
  
  def __repr__(self):
    return self.__str__()
  
  def __eq__(self, other):
    return (self.name, self.charge) == (other.name, other.charge)
