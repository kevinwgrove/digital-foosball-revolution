import time
import board
from digitalio import DigitalInOut, Direction, Pull


reset_button = DigitalInOut(board.D8)
reset_button.direction = Direction.INPUT
reset_button.pull = Pull.UP


while not reset_button.value:
        time.sleep(0.1)
        if reset_button.value:
            away_score = 0
            home_score = 0
            half_time = half_time
            print("Home Score: ", home_score)
            print("Away Score: ", away_score)
            break
