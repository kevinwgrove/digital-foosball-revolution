import adafruit_display_text.label
import terminalio
import displayio
import board
import framebufferio
import rgbmatrix
from adafruit_bitmap_font import bitmap_font


def build_timed_halves_score_screen(group, h_score, a_score, p1_total, p2_total): # noqa
    g0 = group[0]
    g1 = group[1]
    g2 = group[2]
    group.pop(0)
    group.pop(0)
    group.pop(0)
    g = displayio.Group(max_size=11)
    g.append(g0)
    g.append(g1)
    g.append(g2)
    font_file = 'foosball_fonts/Play-Regular-8-8.pcf'
    font = bitmap_font.load_font(font_file)

    if h_score > 9:
        home_score = adafruit_display_text.label.Label(
            terminalio.FONT,
            color=0xff0011,
            text=str(h_score))
        home_score.x = 10
        home_score.y = 26
    else:
        home_score = adafruit_display_text.label.Label(
            terminalio.FONT,
            color=0xff0011,
            text=str(h_score))
        home_score.x = 14
        home_score.y = 26

    if a_score > 9:
        away_score = adafruit_display_text.label.Label(
            terminalio.FONT,
            color=0xff0011,
            text=str(a_score))
        away_score.x = 42
        away_score.y = 26
    else:
        away_score = adafruit_display_text.label.Label(
            terminalio.FONT,
            color=0xff0011,
            text=str(a_score))
        away_score.x = 46
        away_score.y = 26

    if p1_total > 9:
        p1 = str(p1_total)
        p1_1 = adafruit_display_text.label.Label(
                font,
                color=0x0000FF,
                text=p1[0]
            )
        p1_1.x = 0
        p1_1.y = 4
        g.append(p1_1)
        p1_2 = adafruit_display_text.label.Label(
                font,
                color=0x0000FF,
                text=p1[1]
            )
        p1_2.x = 3
        p1_2.y = 4
        g.append(p1_2)
    else:
        p1 = adafruit_display_text.label.Label(
                font,
                color=0x0000FF,
                text=str(p1_total)
            )
        p1.x = 0
        p1.y = 4
        g.append(p1)

    if p2_total > 9:
        p2 = str(p2_total)
        p2_1 = adafruit_display_text.label.Label(
            font,
            color=0x0000FF,
            text=p2[0]
        )
        p2_1.x = 56
        p2_1.y = 4
        g.append(p2_1)
        p2_2 = adafruit_display_text.label.Label(
            font,
            color=0x0000FF,
            text=p2[1]
        )
        p2_2.x = 59
        p2_2.y = 4
        g.append(p2_2)
    else:
        p2 = adafruit_display_text.label.Label(
            font,
            color=0x0000FF,
            text=str(p2_total)
        )
        p2.x = 59
        p2.y = 4
        g.append(p2)

    g.append(home_score)
    g.append(away_score)
    return g


def build_timer_screen(g, time):
    g.pop(0)
    t = adafruit_display_text.label.Label(
        terminalio.FONT,
        color=0xff0011,
        text=str(time))
    t.x = 18
    t.y = 4
    g.insert(0, t)
    return g


def initialize_timed_halves_screen(p1_total, p2_total, h_score, a_score, timer): # noqa
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

    font_file = 'foosball_fonts/Play-Regular-8-8.pcf'
    font = bitmap_font.load_font(font_file)

    timed_halves_group = displayio.Group(max_size=11)

    t = adafruit_display_text.label.Label(
        terminalio.FONT,
        color=0xff0011,
        text=str(timer))
    t.x = 18
    t.y = 4

    timed_halves_group.append(t)

    home_label = adafruit_display_text.label.Label(
        terminalio.FONT,
        color=0xff0011,
        text="Home")
    home_label.x = 4
    home_label.y = 15

    away_label = adafruit_display_text.label.Label(
        terminalio.FONT,
        color=0xff0011,
        text='Away')
    away_label.x = 37
    away_label.y = 15

    timed_halves_group.append(home_label)
    timed_halves_group.append(away_label)

    if p1_total > 9:
        p1 = str(p1_total)
        p1_1 = adafruit_display_text.label.Label(
                font,
                color=0x0000FF,
                text=p1[0]
            )
        p1_1.x = 0
        p1_1.y = 4
        timed_halves_group.append(p1_1)
        p1_2 = adafruit_display_text.label.Label(
                font,
                color=0x0000FF,
                text=p1[1]
            )
        p1_2.x = 3
        p1_2.y = 4
        timed_halves_group.append(p1_2)
    else:
        p1 = adafruit_display_text.label.Label(
                font,
                color=0x0000FF,
                text=str(p1_total)
            )
        p1.x = 0
        p1.y = 4
        timed_halves_group.append(p1)

    if p2_total > 9:
        p2 = str(p2_total)
        p2_1 = adafruit_display_text.label.Label(
            font,
            color=0x0000FF,
            text=p2[0]
        )
        p2_1.x = 56
        p2_1.y = 4
        timed_halves_group.append(p2_1)
        p2_2 = adafruit_display_text.label.Label(
            font,
            color=0x0000FF,
            text=p2[1]
        )
        p2_2.x = 59
        p2_2.y = 4
        timed_halves_group.append(p2_2)
    else:
        p2 = adafruit_display_text.label.Label(
            font,
            color=0x0000FF,
            text=str(p2_total)
        )
        p2.x = 59
        p2.y = 4
        timed_halves_group.append(p2)

    if h_score > 9:
        home_score = adafruit_display_text.label.Label(
            terminalio.FONT,
            color=0xff0011,
            text=str(h_score))
        home_score.x = 10
        home_score.y = 26
    else:
        home_score = adafruit_display_text.label.Label(
            terminalio.FONT,
            color=0xff0011,
            text=str(h_score))
        home_score.x = 14
        home_score.y = 26

    if a_score > 9:
        away_score = adafruit_display_text.label.Label(
            terminalio.FONT,
            color=0xff0011,
            text=str(a_score))
        away_score.x = 42
        away_score.y = 26
    else:
        away_score = adafruit_display_text.label.Label(
            terminalio.FONT,
            color=0xff0011,
            text=str(a_score))
        away_score.x = 46
        away_score.y = 26

    timed_halves_group.append(home_score)
    timed_halves_group.append(away_score)

    display.show(timed_halves_group)
    display.refresh(minimum_frames_per_second=0)
    return timed_halves_group
