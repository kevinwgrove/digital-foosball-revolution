from helpers.increment import inc
from helpers.decrement import dec
import time
import board
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn


print("This is the Digital Foosball Revolution")

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# Home goal sensor
home = DigitalInOut(board.D2)
home.direction = Direction.INPUT
home.pull = Pull.UP

# Away goal sensor
away = DigitalInOut(board.D3)
away.direction = Direction.INPUT
away.pull = Pull.UP

reset_button = DigitalInOut(board.D8)
reset_button.direction = Direction.INPUT
reset_button.pull = Pull.UP

mode_button = DigitalInOut(board.D9)
mode_button.direction = Direction.INPUT
mode_button.pull = Pull.UP

edit_button = DigitalInOut(board.D10)
edit_button.direction = Direction.INPUT
edit_button.pull = Pull.UP

# Increment button
increment = DigitalInOut(board.D6)
increment.direction = Direction.INPUT
increment.pull = Pull.UP

# Decrement button
decrement = DigitalInOut(board.D7)
decrement.direction = Direction.INPUT
decrement.pull = Pull.UP

home_score = 0
away_score = 0

game_mode = 0

high_score = 10

edit = False

edit_mode = 0
team_edit = 0

start_time = 0
time_edit = 5
half_time = int(60 * time_edit)

start_stop_home = DigitalInOut(board.D11)
start_stop_home.direction = Direction.INPUT
start_stop_home.pull = Pull.UP

start_stop_away = DigitalInOut(board.D12)
start_stop_away.direction = Direction.INPUT
start_stop_away.pull = Pull.UP

home_led = DigitalInOut(board.D4)
home_led.direction = Direction.OUTPUT

away_led = DigitalInOut(board.D5)
away_led.direction = Direction.OUTPUT


home_ratio = 1
away_ratio = 1
ratios_on = False

"""
Game Modes:
    0 = 1st to 10 goals
    1 = 1st to high_score
    2 = Timed halves
    3 = Timed halves w/ handicaps

Button Pinouts:
    D2 = Home Goal
    D3 = Away Goal
    D4 = Home LED
    D5 = Away LED
    D6 = Increment
    D7 = Decrement
    D8 = Reset
    D9 = Mode
    D10 = Edit
    D11 = Start/Stop Home
    D12 = Start/Stop Away

Display Pinouts:
    27 = CLK
    32 = R1
    33 = G1
    34 = B1
    35 = R2
    36 = G2
    37 = B2
"""

while True:

    while not reset_button.value:
        time.sleep(0.1)
        if reset_button.value:
            away_score = 0
            home_score = 0
            half_time = half_time
            print("Home Score: ", home_score)
            print("Away Score: ", away_score)
            break

    while not edit_button.value:
        time.sleep(0.1)
        if edit_button.value:
            edit = not edit
            print(edit)
            break

    if edit:
        led.value = True
        while not mode_button.value:
            time.sleep(0.1)
            if mode_button.value:
                if edit_mode == 6:
                    edit_mode = 0
                else:
                    edit_mode = inc(edit_mode)

        if edit_mode == 1:  # edits home score
            while not increment.value:
                time.sleep(0.1)
                if increment.value:
                    home_score = inc(home_score)
                    print("Home Score: ", home_score)
                    print("Away Score: ", away_score)
                    break
            while not decrement.value:
                time.sleep(0.1)
                if decrement.value:
                    if home_score == 0:
                        break
                    else:
                        home_score = dec(home_score)
                        print("Home Score: ", home_score)
                        print("Away Score: ", away_score)
                        break
        elif edit_mode == 2:  # edits away score
            while not increment.value:
                time.sleep(0.1)
                if increment.value:
                    away_score = inc(away_score)
                    print("Home Score: ", home_score)
                    print("Away Score: ", away_score)
                    break
            while not decrement.value:
                time.sleep(0.1)
                if decrement.value:
                    if away_score == 0:
                        break
                    else:
                        away_score = dec(away_score)
                        print("Home Score: ", home_score)
                        print("Away Score: ", away_score)
                        break
        elif edit_mode == 3:  # edits high_score
            while not increment.value:
                time.sleep(0.1)
                if increment.value:
                    high_score = inc(high_score)
                    break
            while not decrement.value:
                time.sleep(0.1)
                if decrement.value:
                    high_score = dec(high_score)
                    break
        elif edit_mode == 4:  # edits half time
            while not increment.value:
                time.sleep(0.1)
                if increment.value:
                    half_time = inc(half_time, 15)
                    break
            while not decrement.value:
                time.sleep(0.1)
                if decrement.value:
                    if half_time >= 15:
                        half_time = dec(half_time, 15)
                        break
                    else:
                        break
        elif edit_mode == 5:  # edits home ratio
            while not increment.value:
                time.sleep(0.1)
                if increment.value:
                    home_ratio = inc(home_ratio)
                    break
            while not decrement.value:
                time.sleep(0.1)
                if decrement.value:
                    if home_ratio == 0:
                        break
                    else:
                        home_ratio = dec(home_ratio)
                        break
        elif edit_mode == 6:
            while not increment.value:
                time.sleep(0.1)
                if increment.value:
                    away_ratio = inc(away_ratio)
                    break
            while not decrement.value:
                time.sleep(0.1)
                if decrement.value:
                    if away_ratio == 0:
                        break
                    else:
                        away_ratio = dec(away_ratio)
                        break

    if game_mode == 0:
        if not home.value:
            home_score = inc(home_score)
            print("Home Score: ", home_score)
            print('Away Score: ', away_score)
        elif not away.value:
            away_score = inc(away_score)
            print("Home Score: ", home_score)
            print('Away Score: ', away_score)

        if home_score == 10 or away_score == 10:
            winner = "Home Team WINS" if home_score == 10 else "Away Team WINS"
            print(winner)
            print("Home Score: ", home_score)
            print('Away Score: ', away_score)
    elif game_mode == 1:
        if not home.value:
            home_score = inc(home_score)
            print("Home Score: ", home_score)
            print('Away Score: ', away_score)
        elif not away.value:
            away_score = inc(away_score)
            print("Home Score: ", home_score)
            print('Away Score: ', away_score)

        if home_score == high_score or away_score == high_score:
            winner = "Home Team WINS" if home_score == high_score else "Away Team WINS" # noqa
            print(winner)
            print("Home Score: ", home_score)
            print('Away Score: ', away_score)
    elif game_mode == 2:
        current_time = int(time.mktime(time.localtime()))
        if start_stop_away.value and start_stop_home.value:
            home_led.value = True
            away_led.value = True
            time.sleep(0.5)
            away_led.value = False
            home_led.value = False
            time.sleep(0.5)
        if not start_stop_home.value and not start_stop_away.value:
            while not start_stop_home.value or not start_stop_away.value:
                home_led.value = True
                away_led.value = True
            home_led.value = False
            away_led.value = False
            time.sleep(1)
            start_time = int(time.mktime(time.localtime()))
        if start_time:
            away_led.value = False
            home_led.value = False
            seconds = []
            end_time = start_time + half_time
            pause = False
            home_goal = False
            away_goal = False
            home_ready = False
            away_ready = False
            while True:
                current_time = int(time.mktime(time.localtime()))
                count_down = end_time - current_time
                if count_down not in seconds and count_down > 0:
                    seconds.append(end_time - current_time)
                    mins, secs = divmod(seconds[-1], 60)
                    timer = '{:02d}:{:02d}'.format(mins, secs)
                    print(timer)

                if not start_stop_home.value or not start_stop_away.value:
                    while not start_stop_home.value or not start_stop_away.value: # noqa
                        pause = True
                        home_led.value = True
                        away_led.value = True
                        current_time = int(time.mktime(time.localtime()))
                    end_time = current_time + seconds[-1]
                    time.sleep(1)

                while pause:
                    current_time = int(time.mktime(time.localtime()))
                    if home_ready and away_ready:
                        pause = False
                        home_ready = False
                        away_ready = False
                        time.sleep(1)
                        end_time = current_time + seconds[-1]
                        break
                    if not start_stop_home.value:
                        home_led.value = False
                        home_ready = True
                    if not start_stop_away.value:
                        away_led.value = False
                        away_ready = True

                if not home.value:
                    home_score += 1
                    home_goal = True
                    away_led.value = True
                    if not home.value:
                        while not home.value:
                            current_time = int(time.mktime(time.localtime()))
                    end_time = current_time + seconds[-1]
                    print("Home Score: ", home_score)
                    print("Away Score: ", away_score)
                elif not away.value:
                    away_score += 1
                    away_goal = True
                    home_led.value = True
                    if not away.value:
                        while not away.value:
                            current_time = int(time.mktime(time.localtime()))
                    end_time = current_time + seconds[-1]
                    print("Home Score: ", home_score)
                    print("Away Score: ", away_score)
                    time.sleep(1)
                else:
                    led.value = False

                while home_goal:
                    if not start_stop_away.value:
                        while not start_stop_away.value:
                            home_goal = False
                            current_time = int(time.mktime(time.localtime()))
                        end_time = current_time + seconds[-1]
                        away_led.value = False
                        time.sleep(1)
                        break

                while away_goal:
                    if not start_stop_home.value:
                        while not start_stop_home.value:
                            away_goal = False
                            current_time = int(time.mktime(time.localtime()))
                        end_time = current_time + seconds[-1]
                        home_led.value = False
                        time.sleep(1)
                        break

                if int(time.mktime(time.localtime())) == end_time:
                    print('GAME OVER')
                    start_time = 0
                    home_score = 0
                    away_score = 0
                    seconds = []
                    break
