import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **balls):
    contents = []
    self.contents = contents
    for x in balls:
      counter = 0
      while counter < balls[x]:
        contents.append(x)
        counter += 1
        
  def draw(self,number):
    counter = 0
    drawnBalls = []
    if number > len(self.contents):
      drawnBalls = self.contents
    else:
      while counter < number:
        drawnBall = random.choice(self.contents)
        drawnBalls.append(drawnBall)
        self.contents.remove(drawnBall)
        counter +=1
      if number > len(self.contents):
        drawnBalls = self.contents
    return drawnBalls 

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  counter = 0
  hits = 0
  expectedContents = []
  for x in expected_balls:
    xcounter = 0
    while xcounter < expected_balls[x]:
      expectedContents.append(x)
      xcounter += 1
  while counter < num_experiments:
    copyHat = copy.deepcopy(hat)
    copyDrawn = copyHat.draw(num_balls_drawn)
    reference = len(copyDrawn)
    for x in expectedContents:
      if x in copyDrawn:
        copyDrawn.remove(x)
      if len(copyDrawn) == (reference - len(expectedContents)):
        hits += 1
    counter += 1
  return hits/num_experiments
  

        
