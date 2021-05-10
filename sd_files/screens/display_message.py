import adafruit_display_text.label
import terminalio
import displayio
import board
import framebufferio
import rgbmatrix
import time


def build_display_message(message, l_two=None):
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
    g = displayio.Group()
    m_list = message.split()
    if l_two:
        line1 = adafruit_display_text.label.Label(
            terminalio.FONT,
            color=0xff0011,
            text=message
        )
        pixels = (len(message) * 5) + (len(message) - 1)
        line1.x = (64 - pixels) // 2
        line1.y = 8
        line2 = adafruit_display_text.label.Label(
            terminalio.FONT,
            color=0xff0011,
            text=l_two
        )
        pixels = (len(l_two) * 5) + (len(l_two) - 1)
        line2.x = (64 - pixels) // 2
        line2.y = 24
        g.append(line1)
        g.append(line2)
    elif len(m_list) > 2:
        m_one = ' '.join(m_list[0:2])
        m_two = ' '.join(m_list[2:])
        line1 = adafruit_display_text.label.Label(
            terminalio.FONT,
            color=0xff0011,
            text=m_one
        )
        pixels = (len(m_one) * 5) + (len(m_one) - 1)
        line1.x = (64 - pixels) // 2
        line1.y = 8
        line2 = adafruit_display_text.label.Label(
            terminalio.FONT,
            color=0xff0011,
            text=m_two
        )
        pixels = (len(m_two) * 5) + (len(m_two) - 1)
        line2.x = (64 - pixels) // 2
        line2.y = 24
        g.append(line1)
        g.append(line2)
    else:
        edit_screen = adafruit_display_text.label.Label(
            terminalio.FONT,
            color=0xff0011,
            text=message
        )
        pixels = (len(message) * 5) + (len(message) - 1)
        edit_screen.x = (64 - pixels) // 2
        edit_screen.y = 16
        g.append(edit_screen)
    display.show(g)
    display.refresh(minimum_frames_per_second=0)
    return


def display_flash_message(m_one_l_one, m_one_l_two, m_two_l_one=None, m_two_l_two=None): # noqa
    if m_one_l_one == ' ' and m_one_l_two == ' ':
        build_display_message(m_two_l_one, m_two_l_two)
        time.sleep(0.75)
        build_display_message(m_one_l_one, m_one_l_two)
        time.sleep(0.75)
        build_display_message(m_two_l_one, m_two_l_two)
        time.sleep(0.75)
        build_display_message(m_one_l_one, m_one_l_two)
        time.sleep(0.75)
        build_display_message(m_two_l_one, m_two_l_two)
        time.sleep(0.75)
        build_display_message(m_one_l_one, m_one_l_two)
        time.sleep(0.75)
        build_display_message(m_two_l_one, m_two_l_two)
        time.sleep(0.75)
        build_display_message(m_one_l_one, m_one_l_two)
        time.sleep(0.75)
        build_display_message(m_two_l_one, m_two_l_two)
        time.sleep(0.75)
    elif m_two_l_one is None and m_two_l_two is None:
        if m_two_l_one is None:
            m_two_l_one = ' '
        if m_two_l_two is None:
            m_two_l_two = ' '
        build_display_message(m_one_l_one, m_one_l_two)
        time.sleep(0.75)
        build_display_message(m_two_l_one, m_two_l_two)
        time.sleep(0.75)
        build_display_message(m_one_l_one, m_one_l_two)
        time.sleep(0.75)
        build_display_message(m_two_l_one, m_two_l_two)
        time.sleep(0.75)
        build_display_message(m_one_l_one, m_one_l_two)
        time.sleep(0.75)
        build_display_message(m_two_l_one, m_two_l_two)
        time.sleep(0.75)
        build_display_message(m_one_l_one, m_one_l_two)
        time.sleep(0.75)
        build_display_message(m_two_l_one, m_two_l_two)
        time.sleep(0.75)
        build_display_message(m_one_l_one, m_one_l_two)
        time.sleep(0.75)
    else:
        build_display_message(m_one_l_one, m_one_l_two)
        time.sleep(0.75)
        build_display_message(m_two_l_one, m_two_l_two)
        time.sleep(0.75)
        build_display_message(m_one_l_one, m_one_l_two)
        time.sleep(0.75)
        build_display_message(m_two_l_one, m_two_l_two)
        time.sleep(0.75)
        build_display_message(m_one_l_one, m_one_l_two)
        time.sleep(0.75)
        build_display_message(m_two_l_one, m_two_l_two)
        time.sleep(0.75)
        build_display_message(m_one_l_one, m_one_l_two)
        time.sleep(0.75)
        build_display_message(m_two_l_one, m_two_l_two)
        time.sleep(0.75)
