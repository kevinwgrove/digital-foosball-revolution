import adafruit_display_text.label
import time
import board
import displayio
import framebufferio
import rgbmatrix
import terminalio
from digitalio import DigitalInOut, Direction, Pull
from screens.game_mode_screen import build_game_mode_screen
from game_modes.classic import classic_mode
from game_modes.timed_halves import timed_halves_mode
from helpers.increment import inc
from helpers.decrement import dec
import random
from audiocore import WaveFile
import adafruit_dotstar as dotstar


try:
    from audioio import AudioOut
except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut
    except ImportError:
        pass

displayio.release_displays()
matrix = rgbmatrix.RGBMatrix(
    width=64, height=32, bit_depth=1,
    rgb_pins=[
        board.D32,
        board.D33,
        board.D34,
        board.D35,
        board.D36,
        board.D37],
    addr_pins=[
        board.A12,
        board.A13,
        board.A14,
        board.A15],
    clock_pin=board.D27,
    latch_pin=board.D28,
    output_enable_pin=board.D26)
display = framebufferio.FramebufferDisplay(matrix, auto_refresh=False)

# Creates first line of text on RGB matrix
line1 = adafruit_display_text.label.Label(
    terminalio.FONT,
    color=0xff0011,
    text="Game Mode")
pixels = (len(line1.text) * 5) + (len(line1.text) - 1)
line1.x = (64 - pixels) // 2
line1.y = 8

# Creates second line of text on RGB matrix
line2 = adafruit_display_text.label.Label(
    terminalio.FONT,
    color=0x0000FF,
    text='Classic'
    )
pixels = (len(line2.text) * 5) + (len(line2.text) - 1)
line2.x = (64 - pixels) // 2
line2.y = 22

g = displayio.Group()
# Adds line1 and line2 to display group "g"
g.append(line1)
g.append(line2)


"""
Game Modes:
    1 = 1st to high_score
    2 = Timed halves w/ handicaps

Button Pinouts:
    D1 = Home Goal LEDs CI
    D2 = Home Goal LEDs DI
    D3 = Away Goal LEDs CI
    D4 = Away Goal LEDs DI
    D5 = Fart Button
    D6 = Increment (Black)
    D7 = Decrement (Black)
    D8 = Reset/Back (Red)
    D9 = Mode/Enter (Green)
    D10 = Edit (Yellow)
    D11 = Home Goal Backup
    D12 = Away Goal Backup
    D38 = Home Goal
    D39 = Away Goal
    D40 = Home LED
    D41 = Away LED
    D42 = Start/Stop Home (Red LED Button)
    D43 = Start/Stop Away (Red LED Button)

Display Pinouts:
    A = A12
    B = A13
    C = A14
    D = A15
    26 = OE
    27 = CLK
    28 = LAT
    32 = R1
    33 = G1
    34 = B1
    35 = R2
    36 = G2
    37 = B2


"""

game_mode = 1
mode_selected = False

# Initializes reset button
reset = DigitalInOut(board.D8)
reset.direction = Direction.INPUT
reset.pull = Pull.UP

# Initializes enter button
enter = DigitalInOut(board.D9)
enter.direction = Direction.INPUT
enter.pull = Pull.UP

# Initializes edit button
edit = DigitalInOut(board.D10)
edit.direction = Direction.INPUT
edit.pull = Pull.UP

# Initializes increment button
increment = DigitalInOut(board.D6)
increment.direction = Direction.INPUT
increment.pull = Pull.UP

# Initializes decrement button
decrement = DigitalInOut(board.D7)
decrement.direction = Direction.INPUT
decrement.pull = Pull.UP

# Initializes LED in start_stop_h button
h_led = DigitalInOut(board.D40)
h_led.direction = Direction.OUTPUT

# Initializes LED in start_stop_a button
a_led = DigitalInOut(board.D41)
a_led.direction = Direction.OUTPUT

# Initializes home LED button
start_stop_h = DigitalInOut(board.D42)
start_stop_h.direction = Direction.INPUT
start_stop_h.pull = Pull.UP

# Initializes away LED button
start_stop_a = DigitalInOut(board.D43)
start_stop_a.direction = Direction.INPUT
start_stop_a.pull = Pull.UP

# h goal sensor
h = DigitalInOut(board.D38)
h.direction = Direction.INPUT
h.pull = Pull.UP

# a goal sensor
a = DigitalInOut(board.D39)
a.direction = Direction.INPUT
a.pull = Pull.UP
fart_button = DigitalInOut(board.D5)

# h goal backup sensor
h_bu = DigitalInOut(board.D11)
h_bu.direction = Direction.INPUT
h_bu.pull = Pull.UP

# a goal backup sensor
a_bu = DigitalInOut(board.D12)
a_bu.direction = Direction.INPUT
a_bu.pull = Pull.UP

light_brightness = 0.5

# home goal LEDs
h_g_dots = dotstar.DotStar(board.D2, board.D1, 10, brightness=light_brightness)

# away goal LEDs
a_g_dots = dotstar.DotStar(board.D4, board.D3, 10, brightness=light_brightness)

# Initializes audio
analog_out = AudioOut(board.A0)

# Initializes fart button
fart_button.direction = Direction.INPUT
fart_button.pull = Pull.UP

while True:
    # Initializes and fills LED color to white
    h_g_dots.fill((255, 255, 255))
    a_g_dots.fill((255, 255, 255))

    while not mode_selected:
        display.show(g)
        # Displays group "g" on RGB matrix
        display.refresh(minimum_frames_per_second=0)
        while not increment.value:
            # Increment button pressed
            if game_mode == 2:
                # Game mode is set to 1 if it reaches 2
                game_mode = 1
                build_game_mode_screen(g, game_mode)
                time.sleep(0.5)
            else:
                # increases game_mode by 1
                game_mode = inc(game_mode)
                build_game_mode_screen(g, game_mode)
                time.sleep(0.5)
        while not decrement.value:
            # Decrement button pressed
            if game_mode == 1:
                # Game mode is set to 2 if it reaches 1
                game_mode = 2
                build_game_mode_screen(g, game_mode)
                time.sleep(0.5)
            else:
                # decreases game_mode by 1
                game_mode = dec(game_mode)
                build_game_mode_screen(g, game_mode)
                time.sleep(0.5)
        while not enter.value:
            # Enter button pressed
            # Selects game mode
            mode_selected = True
            time.sleep(0.5)
        while not fart_button.value:
            # Fart button pressed
            # Selects random audio file from fart folder
            fart_file = open(f'audio_files/farts/fart_{str(random.randint(1, 35))}.wav', "rb") # noqa
            fart = WaveFile(fart_file)
            analog_out.play(fart)

    if game_mode == 1:
        # Enters classic game mode
        classic_mode(increment, decrement, reset, enter, edit, h, a, h_led, a_led, start_stop_h, start_stop_a, h_bu, a_bu, fart_button, analog_out, h_g_dots, a_g_dots) # noqa
        mode_selected = False
    elif game_mode == 2:
        # Enters timed halves game mode
        timed_halves_mode(increment, decrement, reset, enter, edit, h, a, h_led, a_led, start_stop_h, start_stop_a, h_bu, a_bu, fart_button, analog_out, h_g_dots, a_g_dots) # noqa
        mode_selected = False
