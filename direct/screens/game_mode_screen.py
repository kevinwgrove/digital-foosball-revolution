import adafruit_display_text.label
import terminalio
import displayio
import board
import framebufferio
import rgbmatrix


def build_game_mode_screen(g, game_mode):
    g.pop()
    if game_mode == 1:
        message = 'Classic'
        line2 = adafruit_display_text.label.Label(
            terminalio.FONT,
            color=0x0000FF,
            text=message)
        pixels = (len(message) * 5) + (len(message) - 1)
        line2.x = (64 - pixels) // 2
        line2.y = 22
        g.append(line2)
    elif game_mode == 2:
        message = 'Timed 1/2s'
        line2 = adafruit_display_text.label.Label(
            terminalio.FONT,
            color=0x0000FF,
            text=message)
        pixels = (len(message) * 5) + (len(message) - 1)
        line2.x = (64 - pixels) // 2
        line2.y = 22
        g.append(line2)
    return g
