from snake import *

from Settings import Settings
from Snake import Snake
from Food import Food, DisappearingFood, SpeedingFood

def listen_for_input(settings, snake):
   """
   Listens for joystic movement and sets the snake movement direction accordingly. 
   Snake cannot go in the oposite way to where it is heading already.
   If middle button has been pressed - stops the game
   """
   for event in sense.stick.get_events():
      if event.action == 'pressed' and event.direction == 'middle':
         settings.game_on = False
      elif event.action == 'pressed':
         if (event.direction == 'left' and snake.current_direction == 'right') or \
            (event.direction == 'right' and snake.current_direction == 'left') or \
            (event.direction == 'up' and snake.current_direction == 'down') or \
            (event.direction == 'down' and snake.current_direction == 'up'):
            return
         else:
            snake.current_direction = event.direction

def show_score(score):
   """Shows the obtained score for 3 seconds, if score is larger than 10, will display digit by digit with .1 second sleep time inbetween"""
   for _ in range(3):
      for character in str(score):
         sense.show_letter(character)
         sleep(.65)
         sense.clear()
         sleep(.1)

def initialize_food(snake):
   # 30% chance that the food will be disappearing
   if random.random() < .7:
      food = Food()
   else:
      food = DisappearingFood()

   # 15% chance that the speeding food will appear along the other kind
   speeding_food = None
   if random.random() < .15:
      speeding_food = SpeedingFood()

   return food, speeding_food

if __name__ == '__main__':
   # Initialize the main game modules
   settings = Settings()
   snake = Snake()

   # Start the game loop - once player dies or presses middle buttom the loop is broken
   while settings.game_on:
      # If there is not food yet - initialize it, create and show it to the player
      if not settings.food_in_game:
         food, speeding_food = initialize_food(snake)
         food.create_food(snake.snake)
         if speeding_food: speeding_food.create_food(snake.snake)
         settings.food_in_game = True
      food.show_food()
      if speeding_food: speeding_food.show_food()

      # Listen for movement and move the snake accordingly
      listen_for_input(settings, snake)
      snake.move_snake()

      # Check if the head of a snake entered its own body. If yes, show score and break the game loop
      if snake.check_death():
         sleep(3)
         show_score(settings.score)
         settings.game_on = False
         
      # Add body if the food was eaten on the previous round
      snake.add_body(settings)

      # Check if snake head is at the position of food - if yes, add score, delete food and set food_in_game flag to false
      # so that new food can be initialized on a new game loop
      food_eaten = snake.eat_food(food.pos)
      if food_eaten:
         settings.score += food.score
         del food
         if speeding_food: del speeding_food
         settings.food_in_game = False

      # Do the above for the speeding food. Increase speed by 20% if eaten
      if settings.food_in_game and speeding_food:
         food_eaten = snake.eat_food(speeding_food.pos)
         if food_eaten:
            settings.score += speeding_food.score
            settings.speed = settings.speed * 0.8
            del speeding_food
            del food
            settings.food_in_game = False
      
      # Check the disappearing food special case - if the time has elapsed, kill the food
      try: # If the food was killed before
         if food.special_action():
            del food
            if speeding_food: del speeding_food
            settings.food_in_game = False
      except NameError:
         pass

      # Sleep and clear the screen
      sleep(settings.speed)
      sense.clear()

   sense.clear()