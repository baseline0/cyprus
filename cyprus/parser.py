def flatten(x):
  result = []

  for el in x:
    if hasattr(el, "__iter__") and not isinstance(el, str):
      result.extend(flatten(el))
    else:
      result.append(el)

  return result


class Grouping(object):
  
  def __init__(self, kids):
    try:
      self.kids = list(flatten([kids]))
    except TypeError:
      self.kids = [kids]

class Program(Grouping):
  pass
  
class Environment(Grouping):
  pass
  
class Membrane(Grouping):
  pass

class Statement(Grouping):
  pass
