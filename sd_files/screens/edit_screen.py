import adafruit_display_text.label
import terminalio
import displayio
import board
import framebufferio
import rgbmatrix


def build_classic_edit_screen(edit_select, best_of, home_score, away_score, high_score=10): # noqa
    g = displayio.Group()
    if edit_select == 1:
        line1_message = 'Away Score'
        line2_message = str(away_score)
    elif edit_select == 2:
        line1_message = 'Best Of'
        line2_message = str(best_of)
    elif edit_select == 3:
        line1_message = 'First to'
        line2_message = str(high_score)
    else:
        line1_message = 'Home Score'
        line2_message = str(home_score)
    line1 = adafruit_display_text.label.Label(
        terminalio.FONT,
        color=0xff0011,
        text=line1_message
    )
    pixels = (len(line1_message) * 5) + (len(line1_message) - 1)
    line1.x = (64 - pixels) // 2
    line1.y = 8
    line2 = adafruit_display_text.label.Label(
        terminalio.FONT,
        color=0xff0011,
        text=line2_message
    )
    pixels = (len(line2_message) * 5) + (len(line2_message) - 1)
    line2.x = (64 - pixels) // 2
    line2.y = 24
    g.append(line1)
    g.append(line2)
    return g


def build_timed_edit_screen(edit_select, player_one_score, player_two_score, half_time, with_legs, player_one_ratio=1, player_two_ratio=1): # noqa
    g = displayio.Group()
    if edit_select == 1:
        line1_message = 'Player 2'
        line2_message = str(player_two_score)
    elif edit_select == 2:
        line1_message = 'Half Times'
        line2_message = str(half_time)
    elif edit_select == 3:
        line1_message = 'Legs'
        if with_legs:
            line2_message = "On"
        else:
            line2_message = "Off"
    elif edit_select == 4:
        line1_message = 'P1 Ratio'
        line2_message = str(player_one_ratio) + ":1"
    elif edit_select == 5:
        line1_message = 'P2 Ratio'
        line2_message = str(player_two_ratio) + ":1"
    else:
        line1_message = 'Player 1'
        line2_message = str(player_one_score)
    line1 = adafruit_display_text.label.Label(
        terminalio.FONT,
        color=0xff0011,
        text=line1_message
    )
    pixels = (len(line1_message) * 5) + (len(line1_message) - 1)
    line1.x = (64 - pixels) // 2
    line1.y = 8
    line2 = adafruit_display_text.label.Label(
        terminalio.FONT,
        color=0xff0011,
        text=line2_message
    )
    pixels = (len(line2_message) * 5) + (len(line2_message) - 1)
    line2.x = (64 - pixels) // 2
    line2.y = 24
    g.append(line1)
    g.append(line2)
    return g
