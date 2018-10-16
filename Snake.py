from snake import *

class Snake(object):
   def __init__(self, initial_position=[3, 3], snake_color=WHITE, snake_head_color=GREEN):
      self.current_direction = 'right'
      self.snake_head_color = snake_head_color
      self.snake_color = snake_color
      self.snake = [initial_position]
      self.move_direction = {
         'up': -1,
         'right': 1,
         'down': 1,
         'left': -1
      }
      self.eaten_food_pos = []
   
   def clamp_movement(self, value):
      """Ensures that the position of snake doesn't go above 7 or below 0. Returns the opposite values to allow the wall movement"""
      if value < 0: return 7
      elif value > 7: return 0
      return value
    
   def move_snake(self):
      for i in reversed(range(len(self.snake))):
         x, y = self.snake[i]
         if i == 0:
            if self.current_direction == 'right' or self.current_direction == 'left':
               x = self.clamp_movement(x + self.move_direction[self.current_direction])
            if self.current_direction == 'up' or self.current_direction == 'down':
               y = self.clamp_movement(y + self.move_direction[self.current_direction])
         else:
            x, y = self.snake[i-1]

         self.snake[i] = [x, y]
         if i == 0:
            sense.set_pixel(x, y, self.snake_head_color)
         else:
            sense.set_pixel(x, y, self.snake_color)

   def add_body(self, settings):
      """Adds body at the same position as the previously eaten food and resets the eaten food position back to none"""
      if self.eaten_food_pos:
         self.snake.append(self.eaten_food_pos)
         sense.set_pixel(self.eaten_food_pos[0], self.eaten_food_pos[1], self.snake_color)
         self.eaten_food_pos = []
         
         if len(self.snake) % 5 == 0:
            settings.speed *= 0.9

   def eat_food(self, pos):
      """
      If the snake head position is the same as food position, return True as the food as been eaten.
      Store the eaten food position for adding the body part later in the next movement
      """
      if pos == self.snake[0]:
         self.eaten_food_pos = pos
         return True

      return False

   def check_death(self):
      """Checks if head of the snake is at the same position as one of its body parts"""
      return self.snake[0] in self.snake[1:]