

def classic_goal(group, goal, led, button, bu, reset, display):
    goal = True
    led.value = True
    display.show(group)
    display.refresh(minimum_frames_per_second=0)
    while goal:
        if not button.value:
            # Away LED button pressed
            # Game play continued
            led.value = False
            while not button.value:
                goal = False
                return
        if not bu.value:
            print("BU")
            # Away LED button pressed
            # Game play continued
            led.value = False
            while not bu.value:
                goal = False
                print("Exit")
                return


def timed_goal():
    pass


def winner_helper():
    pass
