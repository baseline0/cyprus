# An environment - a container object for rules and particles
class CyprusEnvironment(object):
  def __init__(self, name=None, parent=None, contents=[], membranes=[], rules=[]):
    global sim
    self.sim = sim

    self.name = name
    self.parent = parent
    self.contents = contents
    self.membranes = membranes
    self.staging_area = []
    self.rules = rules
    self.setparents()
    self.setpriorities()

  def printstatus(self, depth=0):
    spaces = " " * (depth * 2)
    print('%s[name: %s' % (spaces, self.name))
    print('%s symbols: %s' % (spaces, self.contents))
    print('%s rules: %s' % (spaces, self.rules))
    print('%s staging area: %s' % (spaces, self.staging_area))
    print('%s Membranes:' % spaces)
    for m in self.membranes:
      m.printstatus(depth + 1)
    print('%s]' % spaces)
  
  def tick(self):
    self.stage1()
    self.stage2()
    self.contents.extend(self.staging_area)
    self.staging_area = []
  
  def setpriorities(self):
    self.ruleranks = {}
    for rule in self.rules:
      r = self.ruleranks.get(rule.priority, [])
      r.append(rule)
      self.ruleranks[rule.priority] = r
  
  def setparents(self):
    for m in self.membranes: m.parent = self
  
  def dissolve(self):
    pass # environments cannot dissolve

  def rule_is_applicable(self, rule):
    counts = set([(s.__str__(), rule.requirements.count(s)) for s in rule.requirements])
    s_counts = dict([(s.__str__(), self.contents.count(s)) for s in self.contents])
    for (s, c) in counts:
      if s_counts.get(s, None) == None or s_counts[s] < c: return False
    return True
    
  def apply_rule(self, rule):
    global cyprus_state_rule_applied
    if self.rule_is_applicable(rule):
      cyprus_state_rule_applied = True
      for s in rule.requirements: self.contents.remove(s)
    self.staging_area.extend(rule.output)

  ## apply all rules maximally, non-deterministically
  def stage1(self):
    for m in self.membranes: 
      m.stage1()

    for p in sorted(self.ruleranks.keys(), reverse=True):
      rs = self.ruleranks[p]
      shuffle(rs)
      for rule in rs:
        while self.rule_is_applicable(rule):
          self.apply_rule(rule)
  
  ## apply changes from stage 1, including dissolutions and osmosis
  def stage2(self):
    global sim # cyprus_membrane_lookup_table

    for m in self.membranes: 
      m.stage2()

    self.contents.extend(self.staging_area)
    self.staging_area = []
    contentcopy = list(self.contents)

    for s in contentcopy:
      if isinstance(s, CyprusDissolveParticle):
        self.contents.remove(s)

        if s.target:
          if not sim.cyprus_membrane_lookup_table.get(s.target, None):
            msg = "ERROR: No containers defined with name '%s'" % s.target
            raise CyprusException(msg)
          sim.cyprus_membrane_lookup_table[s.target].dissolve()
        else:
          self.dissolve()
          break
      
      if isinstance(s, CyprusOsmoseParticle):
        self.contents.remove(s)
        if s.target:
          if not sim.cyprus_membrane_lookup_table.get(s.target, None):
            msg = "ERROR: No containers defined with name '%s'" % s.target
            raise CyprusException(msg)
          sim.cyprus_membrane_lookup_table[s.target].contents.append(
            Particle(s.payload))
        elif self.parent:
          self.parent.contents.append(Particle(s.payload))
        else: # environments cannot be osmosed through
          self.contents.append(s)