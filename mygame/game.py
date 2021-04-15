# game.py
# import the draw module

# import draw

## We may also import the function draw_game directly into the main script's namespace, by using the from command.
## from draw import draw_game

### We may also use the import * command to import all objects from a specific module, like this:
from draw import *

# if you have two draw modules with slighty different names 
# if visual_mode:
#     import draw_visual as draw
# else:
#     import draw_textual as draw

def play_game():
    ...

def main():
    result = play_game()
#    draw.draw_game(result)
    draw_game(result)

# this means that if this script is executed, then
# main() will be executed
if __name__ == '__main__':
    main()