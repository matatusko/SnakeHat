from snake import *

class Food(object):
   def __init__(self, score=1, food_color=RED):
      self.food_color = food_color
      self.score = score
      self.pos = []

   def create_food(self, snake):
      """If the food doesn't exist yet, creates it at random position by also making sure that it doesn't spawn at any position that of a snake body"""
      while not self.pos:
         x = random.randint(0, 7)
         y = random.randint(0, 7)
         if [x, y] not in snake:
            self.pos = [x, y]

   def show_food(self):
      sense.set_pixel(self.pos[0], self.pos[1], self.food_color)

   def special_action(self):
      return False

class DisappearingFood(Food):
   def __init__(self, disappearance_time=4.0, score=3, food_color=MAGENTA):
      self.food_color = food_color
      self.pos = []
      self.score = score
      self.time_till_end = time() + disappearance_time

   def special_action(self): 
      return self.time_till_end < time()

class SpeedingFood(Food):
   def __init__(self, score=7, food_color=CYAN):
      self.food_color = food_color
      self.pos = []
      self.score = score