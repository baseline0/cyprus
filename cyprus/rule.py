class CyprusRule(object):

  def __init__(self, name, req, out, pri=1):
    self.name = name
    self.requirements = req
    self.output = out
    self.priority = pri
  
  def __str__(self):
    if self.name != None:
      return "%s -> %s (%s)[%s])" % (self.requirements, self.output, self.priority, self.name)
    else:
      return "%s -> %s (%s)" % (self.requirements, self.output, self.priority)
  
  def __repr__(self):
    return self.__str__()
