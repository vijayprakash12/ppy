from collections import defaultdict
class Solution:
   def __init__(self, head_name):
      self.family = defaultdict(list)
      self.head = head_name
      self.dead = set()

   def birth(self, p_name, c_name):
      self.family[p_name].append(c_name)
      #print(self.family)

   def death(self, name):
      self.dead.add(name)
      #print(self.dead)

   def inheritance(self):
      self.ans = []
      self.depth_search(self.head)
      return self.ans

   def depth_search(self, current):
      if current not in self.dead:
         self.ans.append(current)
      for child in self.family[current]:
         self.depth_search(child)

ob = Solution('Jack')
ob.birth('Jack', 'Mack')
ob.birth('Jack', 'Rok')
ob.birth('Rok', 'Bolt')
ob.birth('Rok', 'Nike')
ob.birth('Mack', 'John')
ob.birth('John', 'Sad')
print(ob.inheritance())
ob.death('Mack')
print(ob.inheritance())
ob.death('Rok')
print(ob.inheritance())
'''['Jack', 'Mack', 'John', 'Sad', 'Rok', 'Bolt', 'Nike']
['Jack', 'John', 'Sad', 'Rok', 'Bolt', 'Nike']
['Jack', 'John', 'Sad', 'Bolt', 'Nike']'''
