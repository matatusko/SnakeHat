# SnakeHat

SnakeHat - Traditional snake game for Raspberry Pi's SenseHat.

Some extra features:
- include 3 kinds of food:
  - Standard (red) - gives 1 points
  - Disappearing (magenta) - gives 3 points but disappear after 4 seconds. 30% appearance rate
  - Speeding (cyan) - gives 7 points but speed up the movement by 20%. Appears among other kind of food. 10% appearance rate.
 - Movement speed increases by 10% every 5 eaten block;
 - Score shows up at the end of a game;
 - Middle button press to quickly finish the game;
  
I'll post same screenshots/gifs later (maybe...:))

# How to run

Simply run as a python package - throw everything in a single folder and run the command
```python
python -m folder_name.app
```
