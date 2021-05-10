from screens.display_message import build_display_message, display_flash_message # noqa
from helpers.increment import inc
from helpers.decrement import dec
from screens.timed_halves_screen import build_timed_halves_score_screen, initialize_timed_halves_screen, build_timer_screen # noqa
from screens.edit_screen import build_timed_edit_screen
import board
import displayio
import framebufferio
import rgbmatrix
import time
import random
from audiocore import WaveFile


def ratio_halves_mode(increment, decrement, reset, enter, edit, home, away, home_led, away_led, start_stop_home, start_stop_away, h_bu, a_bu, fart_button, analog_out): # noqa
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
    """
    Button Pinouts:
        D2 = Home Goal
        D3 = Away Goal
        D4 = Home LED
        D5 = Away LED
        D6 = Increment (Black)
        D7 = Decrement (Black)
        D8 = Reset/Back (Red)
        D9 = Mode/Enter (Green)
        D10 = Edit (Yellow)
        D11 = Start/Stop Home (Red LED)
        D12 = Start/Stop Away (Red LED)
        D14 = Home Goal Backup
        D15 = Away Goal Backup
    """

    current_time = int(time.mktime(time.localtime()))
    half_time = int(60)
    home_goal = away_goal = edit_mode = home_ready = away_ready = extra_time = with_legs = game_start = winner = pause = False # noqa
    home_led.value = away_led.value = True
    start_time = edit_select = home_score = away_score = player_one_total = player_two_total = player_one_count = player_two_count = 0 # noqa
    half = leg = player_one_ratio = player_two_ratio = 1
    golden_goal_half = half_time // 2
    seconds = [half_time]
    mins, secs = divmod(seconds[-1], 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    half_time_mins, half_time_secs = divmod(half_time, 60)
    half_time_timer = '{:02d}:{:02d}'.format(half_time_mins, half_time_secs)
    golden_goal_mins, golden_goal_secs = divmod(golden_goal_half, 60)
    golden_goal_timer = '{:02d}:{:02d}'.format(golden_goal_mins, golden_goal_secs) # noqa

    timed_halves_group = initialize_timed_halves_screen(player_one_total, player_two_total, home_score, away_score, half_time_timer) # noqa

    single_whistle_file = open("audio_files/single_whistle.wav", "rb")
    single_whistle = WaveFile(single_whistle_file)

    three_whistles_file = open("audio_files/three_whistles.wav", "rb")
    three_whistles = WaveFile(three_whistles_file)

    goal_long_file = open("audio_files/goal_long.wav", "rb")
    goal_long = WaveFile(goal_long_file)

    goal_short_file = open("audio_files/goal_short.wav", "rb")
    goal_short = WaveFile(goal_short_file)

    while True:
        if not fart_button.value:
            fart_file = open(f'audio_files/farts/fart_{str(random.randint(1, 35))}.wav', "rb") # noqa
            fart = WaveFile(fart_file)
            analog_out.play(fart)
        display.show(timed_halves_group)
        display.refresh(minimum_frames_per_second=0)
        while not edit.value:
            edit_select = 0
            edit_mode = True
            build_display_message('Edit Mode')
            time.sleep(2)
            timed_halves_group = build_timed_edit_screen(edit_select, home_score, away_score, half_time_timer, with_legs, player_one_ratio, player_two_ratio) # noqa

        while edit_mode:
            display.show(timed_halves_group)
            display.refresh(minimum_frames_per_second=0)
            while not edit.value:
                if edit_select == 5:
                    edit_select = 0
                    timed_halves_group = build_timed_edit_screen(edit_select, home_score, away_score, half_time_timer, with_legs, player_one_ratio, player_two_ratio) # noqa
                    time.sleep(0.5)
                else:
                    edit_select = inc(edit_select)
                    if edit_select == 2:
                        timed_halves_group = build_timed_edit_screen(edit_select, home_score, away_score, half_time_timer, with_legs, player_one_ratio, player_two_ratio) # noqa
                    elif edit_select == 3:
                        timed_halves_group = build_timed_edit_screen(edit_select, home_score, away_score, half_time_timer, with_legs, player_one_ratio, player_two_ratio) # noqa
                    elif edit_select == 4:
                        timed_halves_group = build_timed_edit_screen(edit_select, home_score, away_score, half_time_timer, with_legs, player_one_ratio, player_two_ratio) # noqa
                    elif edit_select == 5:
                        timed_halves_group = build_timed_edit_screen(edit_select, home_score, away_score, half_time_timer, with_legs, player_one_ratio, player_two_ratio) # noqa
                    elif edit_select == 0:
                        timed_halves_group = build_timed_edit_screen(edit_select, home_score, away_score, half_time_timer, with_legs, player_one_ratio, player_two_ratio) # noqa
                    else:
                        timed_halves_group = build_timed_edit_screen(edit_select, home_score, away_score, half_time_timer, with_legs, player_one_ratio, player_two_ratio) # noqa
                    time.sleep(0.5)

            while not enter.value:
                edit_mode = False
                timed_halves_group = initialize_timed_halves_screen(player_one_total, player_two_total, home_score, away_score, half_time_timer) # noqa
                time.sleep(0.5)

            if edit_select == 1:
                while not increment.value:
                    away_score = inc(away_score)
                    player_two_total = inc(player_two_total)
                    timed_halves_group = build_timed_edit_screen(edit_select, home_score, away_score, half_time_timer, with_legs, player_one_ratio, player_two_ratio) # noqa
                    time.sleep(0.5)
                while not decrement.value:
                    if away_score == 0:
                        break
                    else:
                        away_score = dec(away_score)
                        player_two_total = dec(player_two_total)
                        timed_halves_group = build_timed_edit_screen(edit_select, home_score, away_score, half_time_timer, with_legs, player_one_ratio, player_two_ratio) # noqa
                        time.sleep(0.5)
            elif edit_select == 2:
                while not increment.value:
                    half_time = int(inc(half_time, 15))
                    half_time_mins, half_time_secs = divmod(half_time, 60)
                    half_time_timer = '{:02d}:{:02d}'.format(half_time_mins, half_time_secs) # noqa
                    golden_goal_half = half_time // 2
                    timed_halves_group = build_timed_edit_screen(edit_select, home_score, away_score, half_time_timer, with_legs, player_one_ratio, player_two_ratio) # noqa
                    time.sleep(0.25)
                while not decrement.value:
                    if half_time == 15:
                        break
                    else:
                        half_time = int(dec(half_time, 15))
                        half_time_mins, half_time_secs = divmod(half_time, 60)
                        half_time_timer = '{:02d}:{:02d}'.format(half_time_mins, half_time_secs) # noqa
                        golden_goal_half = half_time // 2
                        timed_halves_group = build_timed_edit_screen(edit_select, home_score, away_score, half_time_timer, with_legs, player_one_ratio, player_two_ratio) # noqa
                        time.sleep(0.25)
            elif edit_select == 3:
                while not increment.value or not decrement.value:
                    with_legs = not with_legs
                    timed_halves_group = build_timed_edit_screen(edit_select, home_score, away_score, half_time_timer, with_legs, player_one_ratio, player_two_ratio) # noqa
                    time.sleep(0.5)
            elif edit_select == 4:
                while not increment.value:
                    player_one_ratio = inc(player_one_ratio)
                    timed_halves_group = build_timed_edit_screen(edit_select, home_score, away_score, half_time_timer, with_legs, player_one_ratio, player_two_ratio) # noqa
                    time.sleep(0.5)
                while not decrement.value:
                    if player_one_ratio == 1:
                        break
                    else:
                        player_one_ratio = dec(player_one_ratio)
                        timed_halves_group = build_timed_edit_screen(edit_select, home_score, away_score, half_time_timer, with_legs, player_one_ratio, player_two_ratio) # noqa
                        time.sleep(0.5)
            elif edit_select == 5:
                while not increment.value:
                    player_two_ratio = inc(player_two_ratio)
                    timed_halves_group = build_timed_edit_screen(edit_select, home_score, away_score, half_time_timer, with_legs, player_one_ratio, player_two_ratio) # noqa
                    time.sleep(0.5)
                while not decrement.value:
                    if player_two_ratio == 1:
                        break
                    else:
                        player_two_ratio = dec(player_two_ratio)
                        timed_halves_group = build_timed_edit_screen(edit_select, home_score, away_score, half_time_timer, with_legs, player_one_ratio, player_two_ratio) # noqa
                        time.sleep(0.5)
            else:
                while not increment.value:
                    home_score = inc(home_score)
                    player_one_total = inc(player_one_total)
                    timed_halves_group = build_timed_edit_screen(edit_select, home_score, away_score, half_time_timer, with_legs, player_one_ratio, player_two_ratio) # noqa
                    time.sleep(0.5)
                while not decrement.value:
                    if home_score == 0:
                        break
                    else:
                        home_score = dec(home_score)
                        player_one_total = dec(player_one_total)
                        timed_halves_group = build_timed_edit_screen(edit_select, home_score, away_score, half_time_timer, with_legs, player_one_ratio, player_two_ratio) # noqa
                        time.sleep(0.5)

        if not start_stop_home.value:
            home_led.value = False
            home_ready = True

        if not start_stop_away.value:
            away_led.value = False
            away_ready = True

        if home_ready and away_ready:
            game_start = True
            analog_out.play(single_whistle)
            build_display_message('Kick Off')
            time.sleep(1.5)
            start_time = int(time.mktime(time.localtime()))
            golden_goal_half = half_time // 2
            golden_goal_mins, golden_goal_secs = divmod(golden_goal_half, 60)
            golden_goal_timer = '{:02d}:{:02d}'.format(golden_goal_mins, golden_goal_secs) # noqa
            end_time = start_time + half_time
            if extra_time:
                end_time = start_time + golden_goal_half
                seconds = [golden_goal_half]
                timed_halves_group = initialize_timed_halves_screen(player_one_total, player_two_total, home_score, away_score, golden_goal_timer) # noqa
            else:
                timed_halves_group = initialize_timed_halves_screen(player_one_total, player_two_total, home_score, away_score, half_time_timer) # noqa

        if not reset.value:
            home_led.value = away_led.value = False
            return

        while game_start:
            if not fart_button.value:
                fart_file = open(f'audio_files/farts/fart_{str(random.randint(1, 35))}.wav', "rb") # noqa
                fart = WaveFile(fart_file)
                analog_out.play(fart)
            display.show(timed_halves_group)
            display.refresh(minimum_frames_per_second=0)
            if not reset.value:
                game_start = home_goal = away_goal = home_ready = away_ready = False # noqa
                home_led.value = away_led.value = True
                seconds = [half_time]
                home_score = away_score = start_time = player_one_total = player_two_total = 0 # noqa
                timed_halves_group = initialize_timed_halves_screen(player_one_total, player_two_total, home_score, away_score, half_time_timer) # noqa
                time.sleep(1)
                break

            current_time = int(time.mktime(time.localtime()))
            count_down = end_time - current_time
            if count_down not in seconds and count_down > 0:
                seconds.pop(0)
                seconds.append(end_time - current_time)
                mins, secs = divmod(seconds[-1], 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                timed_halves_group = build_timer_screen(timed_halves_group, timer) # noqa

            if not start_stop_home.value or not start_stop_away.value:
                pause = home_led.value = away_led.value = True
                home_ready = away_ready = False
                current_time = int(time.mktime(time.localtime()))
                end_time = current_time + seconds[-1]
                time.sleep(1)

            while pause:
                current_time = int(time.mktime(time.localtime()))
                if home_ready and away_ready:
                    pause = away_ready = home_ready = False
                    time.sleep(1)
                    end_time = current_time + seconds[-1]
                    timed_halves_group = build_timer_screen(timed_halves_group, timer) # noqa
                    break
                if not start_stop_home.value:
                    home_led.value = False
                    home_ready = True
                if not start_stop_away.value:
                    away_led.value = False
                    away_ready = True

                while not edit.value:
                    edit_mode = True
                    edit_select = 0
                    time.sleep(0.5)

                while edit_mode:
                    while not edit.value:
                        if edit_select == 1:
                            edit_select = 0
                            timed_halves_group = build_timed_edit_screen(edit_select, home_score, away_score, half_time_timer, with_legs, player_one_ratio, player_two_ratio) # noqa
                            time.sleep(0.5)
                        else:
                            edit_select = 1
                            timed_halves_group = build_timed_edit_screen(edit_select, home_score, away_score, half_time_timer, with_legs, player_one_ratio, player_two_ratio) # noqa
                            time.sleep(0.5)

                    while not enter.value:
                        edit_mode = False
                        time.sleep(0.5)

                    if edit_select == 1:
                        while not increment.value:
                            away_score = inc(away_score)
                            player_two_total = inc(player_two_total)
                            timed_halves_group = build_timed_edit_screen(edit_select, home_score, away_score, half_time_timer, with_legs, player_one_ratio, player_two_ratio) # noqa
                            time.sleep(0.5)
                        while not decrement.value:
                            if away_score == 0:
                                break
                            else:
                                away_score = dec(away_score)
                                player_two_total = dec(player_two_total)
                                timed_halves_group = build_timed_edit_screen(edit_select, home_score, away_score, half_time_timer, with_legs, player_one_ratio, player_two_ratio) # noqa
                                time.sleep(0.5)
                    else:
                        while not increment.value:
                            home_score = inc(home_score)
                            player_one_total = inc(player_one_total)
                            timed_halves_group = build_timed_edit_screen(edit_select, home_score, away_score, half_time_timer, with_legs, player_one_ratio, player_two_ratio) # noqa
                            time.sleep(0.5)
                        while not decrement.value:
                            if home_score == 0:
                                break
                            else:
                                home_score = dec(home_score)
                                player_one_total = dec(player_one_total)
                                timed_halves_group = build_timed_edit_screen(edit_select, home_score, away_score, half_time_timer, with_legs, player_one_ratio, player_two_ratio) # noqa
                                time.sleep(0.5)

            if not home.value:
                if half & 1 and leg == 1:  # first half
                    if player_one_ratio > 1:
                        player_one_count = inc(player_one_count)
                        if player_one_count == player_one_ratio:
                            home_score = inc(home_score)
                            player_one_total = inc(player_one_total)
                            player_one_count = 0
                            timed_halves_group = build_timed_halves_score_screen(timed_halves_group, home_score, away_score, player_one_total, player_two_total) # noqa
                    else:
                        home_score = inc(home_score)
                        player_one_total = inc(player_one_total)
                    if away_score - home_score >= 5:
                        analog_out.play(goal_long)
                    else:
                        analog_out.play(goal_short)
                    home_goal = away_led.value = True
                    current_time = int(time.mktime(time.localtime()))
                    end_time = current_time + seconds[-1]
                    timed_halves_group = build_timed_halves_score_screen(timed_halves_group, home_score, away_score, player_one_total, player_two_total) # noqa
                elif half & 1 and leg == 2:
                    if player_two_ratio > 1:
                        player_two_count = inc(player_two_count)
                        if player_two_count == player_two_ratio:
                            home_score = inc(home_score)
                            player_two_total = inc(player_two_total)
                            player_two_count = 0
                            timed_halves_group = build_timed_halves_score_screen(timed_halves_group, home_score, away_score, player_one_total, player_two_total) # noqa
                    else:
                        home_score = inc(home_score)
                        player_two_total = inc(player_two_total)
                    if away_score - home_score >= 5:
                        analog_out.play(goal_long)
                    else:
                        analog_out.play(goal_short)
                    home_goal = away_led.value = True
                    current_time = int(time.mktime(time.localtime()))
                    end_time = current_time + seconds[-1]
                    timed_halves_group = build_timed_halves_score_screen(timed_halves_group, home_score, away_score, player_one_total, player_two_total) # noqa
                elif not half & 1 and leg == 2:
                    if player_one_ratio > 1:
                        player_one_count = inc(player_one_count)
                        if player_one_count == player_one_ratio:
                            away_score = inc(away_score)
                            player_one_total = inc(player_one_total)
                            player_one_count = 0
                            timed_halves_group = build_timed_halves_score_screen(timed_halves_group, home_score, away_score, player_one_total, player_two_total) # noqa
                    else:
                        away_score = inc(away_score)
                        player_one_total = inc(player_one_total)
                    if home_score - away_score >= 5:
                        analog_out.play(goal_long)
                    else:
                        analog_out.play(goal_short)
                    home_goal = away_led.value = True
                    current_time = int(time.mktime(time.localtime()))
                    end_time = current_time + seconds[-1]
                    timed_halves_group = build_timed_halves_score_screen(timed_halves_group, home_score, away_score, player_one_total, player_two_total) # noqa
                else:  # second half
                    if player_two_ratio > 1:
                        player_two_count = inc(player_two_count)
                        if player_two_count == player_two_ratio:
                            away_score = inc(away_score)
                            player_two_total = inc(player_two_total)
                            player_two_count = 0
                            timed_halves_group = build_timed_halves_score_screen(timed_halves_group, home_score, away_score, player_one_total, player_two_total) # noqa
                    else:
                        away_score = inc(away_score)
                        player_two_total = inc(player_two_total)
                    if home_score - away_score >= 5:
                        analog_out.play(goal_long)
                    else:
                        analog_out.play(goal_short)
                    home_goal = away_led.value = True
                    current_time = int(time.mktime(time.localtime()))
                    end_time = current_time + seconds[-1]
                    timed_halves_group = build_timed_halves_score_screen(timed_halves_group, home_score, away_score, player_one_total, player_two_total) # noqa
            elif not away.value:
                if half & 1 and leg == 1:  # first half
                    if player_two_ratio > 1:
                        player_two_count = inc(player_two_count)
                        if player_two_count == player_two_ratio:
                            away_score = inc(away_score)
                            player_two_total = inc(player_two_total)
                            player_two_count = 0
                            timed_halves_group = build_timed_halves_score_screen(timed_halves_group, home_score, away_score, player_one_total, player_two_total) # noqa
                    else:
                        away_score = inc(away_score)
                        player_two_total = inc(player_two_total)
                    if home_score - away_score >= 5:
                        analog_out.play(goal_long)
                    else:
                        analog_out.play(goal_short)
                    away_goal = home_led.value = True
                    current_time = int(time.mktime(time.localtime()))
                    end_time = current_time + seconds[-1]
                    timed_halves_group = build_timed_halves_score_screen(timed_halves_group, home_score, away_score, player_one_total, player_two_total) # noqa
                elif half & 1 and leg == 2:
                    if player_one_ratio > 1:
                        player_one_count = inc(player_one_count)
                        if player_one_count == player_one_ratio:
                            away_score = inc(away_score)
                            player_one_total = inc(player_one_total)
                            player_one_count = 0
                            timed_halves_group = build_timed_halves_score_screen(timed_halves_group, home_score, away_score, player_one_total, player_two_total) # noqa
                    else:
                        away_score = inc(away_score)
                        player_one_total = inc(player_one_total)
                    if home_score - away_score >= 5:
                        analog_out.play(goal_long)
                    else:
                        analog_out.play(goal_short)
                    away_goal = home_led.value = True
                    current_time = int(time.mktime(time.localtime()))
                    end_time = current_time + seconds[-1]
                    timed_halves_group = build_timed_halves_score_screen(timed_halves_group, home_score, away_score, player_one_total, player_two_total) # noqa
                elif not half & 1 and leg == 2:
                    if player_two_ratio > 1:
                        player_two_count = inc(player_two_count)
                        if player_two_count == player_two_ratio:
                            home_score = inc(home_score)
                            player_two_total = inc(player_two_total)
                            player_two_count = 0
                            timed_halves_group = build_timed_halves_score_screen(timed_halves_group, home_score, away_score, player_one_total, player_two_total) # noqa
                    else:
                        home_score = inc(home_score)
                        player_two_total = inc(player_two_total)
                    if away_score - home_score >= 5:
                        analog_out.play(goal_long)
                    else:
                        analog_out.play(goal_short)
                    away_goal = home_led.value = True
                    current_time = int(time.mktime(time.localtime()))
                    end_time = current_time + seconds[-1]
                    timed_halves_group = build_timed_halves_score_screen(timed_halves_group, home_score, away_score, player_one_total, player_two_total) # noqa
                else:  # second half
                    if player_one_ratio > 1:
                        player_one_count = inc(player_one_count)
                        if player_one_count == player_one_ratio:
                            home_score = inc(home_score)
                            player_one_total = inc(player_one_total)
                            player_one_count = 0
                    else:
                        home_score = inc(home_score)
                        player_one_total = inc(player_one_total)
                    if away_score - home_score >= 5:
                        analog_out.play(goal_long)
                    else:
                        analog_out.play(goal_short)
                    away_goal = home_led.value = True
                    current_time = int(time.mktime(time.localtime()))
                    end_time = current_time + seconds[-1]
                    timed_halves_group = build_timed_halves_score_screen(timed_halves_group, home_score, away_score, player_one_total, player_two_total) # noqa

            while home_goal:
                if not fart_button.value:
                    fart_file = open(f'audio_files/farts/fart_{str(random.randint(1, 35))}.wav', "rb") # noqa
                    fart = WaveFile(fart_file)
                    analog_out.play(fart)
                display.show(timed_halves_group)
                display.refresh(minimum_frames_per_second=0)
                if extra_time:
                    if player_one_total > player_two_total or player_two_total > player_one_total: # noqa
                        analog_out.play(three_whistles)
                        home_led.value = away_led.value = True
                        if half == 1:
                            if with_legs:
                                display_winner = "Player 1" if player_one_total > player_two_total else "Player 2" # noqa
                                display_flash_message(' ', ' ', display_winner, 'Wins!!!') # noqa
                                time.sleep(3)
                            else:
                                display_flash_message('Home Team', 'Wins!!!', ' ', ' ') # noqa
                                time.sleep(0.5)
                        else:
                            if with_legs:
                                display_winner = "Player 1" if player_one_total > player_two_total else "Player 2" # noqa
                                display_flash_message(' ', ' ', display_winner, 'Wins!!!') # noqa
                                time.sleep(3)
                            else:
                                display_flash_message('Away Team', 'Wins!!!', ' ', ' ') # noqa
                                time.sleep(0.5)
                        winner = True
                        break
                    else:
                        if not start_stop_away.value or not a_bu.value:
                            while not start_stop_away.value or not a_bu.value:
                                home_goal = False
                                current_time = int(time.mktime(time.localtime())) # noqa
                            end_time = current_time + seconds[-1]
                            away_led.value = False
                            time.sleep(1)
                            break
                if not start_stop_away.value or not a_bu.value:
                    while not start_stop_away.value or not a_bu.value:
                        home_goal = False
                        current_time = int(time.mktime(time.localtime()))
                    end_time = current_time + seconds[-1]
                    away_led.value = False
                    time.sleep(1)
                    break

            while away_goal:
                if not fart_button.value:
                    fart_file = open(f'audio_files/farts/fart_{str(random.randint(1, 35))}.wav', "rb") # noqa
                    fart = WaveFile(fart_file)
                    analog_out.play(fart)
                display.show(timed_halves_group)
                display.refresh(minimum_frames_per_second=0)
                if extra_time:
                    if player_one_total > player_two_total or player_two_total > player_one_total: # noqa
                        home_led.value = away_led.value = True
                        analog_out.play(three_whistles)
                        if half == 1:
                            if with_legs:
                                display_winner = "Player 1" if player_one_total > player_two_total else "Player 2" # noqa
                                display_flash_message(' ', ' ', display_winner, 'Wins!!!') # noqa
                                time.sleep(3)
                            else:
                                display_flash_message('Away Team', 'Wins!!!', ' ', ' ') # noqa
                                time.sleep(0.5)
                        else:
                            if with_legs:
                                display_winner = "Player 1" if player_one_total > player_two_total else "Player 2" # noqa
                                display_flash_message(' ', ' ', display_winner, 'Wins!!!') # noqa
                                time.sleep(3)
                            else:
                                display_flash_message('Home Team', 'Wins!!!', ' ', ' ') # noqa
                                time.sleep(0.5)
                        winner = True
                        break
                    else:
                        if not start_stop_home.value or not h_bu.value:
                            while not start_stop_home.value or not h_bu.value:
                                away_goal = False
                                current_time = int(time.mktime(time.localtime())) # noqa
                            end_time = current_time + seconds[-1]
                            home_led.value = False
                            time.sleep(1)
                            break
                if not start_stop_home.value or not h_bu.value:
                    while not start_stop_home.value or not h_bu.value:
                        away_goal = False
                        current_time = int(time.mktime(time.localtime()))
                    end_time = current_time + seconds[-1]
                    home_led.value = False
                    time.sleep(1)
                    break

            if winner:
                away_goal = home_goal = home_ready = away_ready = extra_time = game_start = False # noqa
                home_led.value = away_led.value = True
                home_score = away_score = player_two_total = player_one_total = start_time = player_one_count = player_two_count = 0 # noqa
                half = leg = 1
                seconds = [half_time]
                timed_halves_group = initialize_timed_halves_screen(player_one_total, player_two_total, home_score, away_score, half_time_timer) # noqa
                winner = False
                break

            if int(time.mktime(time.localtime())) == end_time:
                analog_out.play(three_whistles)
                if half == 1:
                    if extra_time:
                        display_flash_message('Golden', 'Goal', 'Switch', 'Sides') # noqa
                        time.sleep(0.5)
                        extra_time = home_led.value = away_led.value = True
                        end_time = start_time + golden_goal_half
                        start_time = 0
                        home_goal = away_goal = home_ready = away_ready = game_start = False # noqa
                        seconds = [half_time]
                        half = 2
                        time.sleep(3)
                        timed_halves_group = initialize_timed_halves_screen(player_one_total, player_two_total, home_score, away_score, golden_goal_timer) # noqa
                        break
                    else:
                        build_display_message('Switch', 'Sides')
                        away_goal = home_goal = home_ready = away_ready = game_start = False # noqa
                        home_led.value = away_led.value = True
                        start_time = 0
                        seconds = [half_time]
                        half = 2
                        time.sleep(3)
                        timed_halves_group = initialize_timed_halves_screen(player_one_total, player_two_total, home_score, away_score, half_time_timer) # noqa
                        break
                elif half == 2 and leg == 1:
                    if with_legs:
                        if player_one_total == player_two_total:
                            build_display_message('First leg', 'Tie')
                            start_time = home_score = away_score = player_one_count = player_two_count = 0 # noqa
                            seconds = [half_time]
                            half = 1
                            leg = 2
                            home_goal = away_goal = home_ready = away_ready = game_start = False # noqa
                            home_led.value = away_led.value = True
                            time.sleep(3)
                            timed_halves_group = initialize_timed_halves_screen(player_one_total, player_two_total, home_score, away_score, half_time_timer) # noqa
                            break
                        else:
                            display_winner = "Player 1" if home_score > away_score else "Player 2" # noqa
                            build_display_message(display_winner,  '1st Leg')
                            leg = 2
                            half = 1
                            start_time = home_score = away_score = player_one_count = player_two_count = 0 # noqa
                            home_goal = away_goal = home_ready = away_ready = game_start = False # noqa
                            home_led.value = away_led.value = True
                            seconds = [half_time]
                            time.sleep(3)
                            timed_halves_group = initialize_timed_halves_screen(player_one_total, player_two_total, home_score, away_score, half_time_timer) # noqa
                            break
                    else:
                        if player_one_total == player_two_total:
                            display_flash_message('Golden', 'Goal', 'Switch', 'Sides') # noqa
                            time.sleep(0.5)
                            extra_time = home_led.value = away_led.value = True
                            end_time = start_time + golden_goal_half
                            start_time = 0
                            home_goal = away_goal = home_ready = away_ready = game_start = False # noqa
                            seconds = [half_time]
                            half = 1
                            time.sleep(3)
                            timed_halves_group = initialize_timed_halves_screen(player_one_total, player_two_total, home_score, away_score, golden_goal_timer) # noqa
                            break
                        else:
                            display_winner = "Home Team" if home_score > away_score else "Away Team" # noqa
                            display_flash_message(' ', ' ', display_winner, 'Wins!!!') # noqa
                            half = 1
                            start_time = home_score = away_score = player_one_count = player_two_count = player_two_total = player_one_total = 0 # noqa
                            home_goal = away_goal = home_ready = away_ready = game_start = False # noqa
                            home_led.value = away_led.value = True
                            seconds = [half_time]
                            time.sleep(3)
                            timed_halves_group = initialize_timed_halves_screen(player_one_total, player_two_total, home_score, away_score, half_time_timer) # noqa
                            break
                elif half == 2 and leg == 2:
                    if player_one_total == player_two_total:
                        display_flash_message('Golden', 'Goal', 'Switch', 'Sides') # noqa
                        time.sleep(0.5)
                        extra_time = home_led.value = away_led.value = True
                        end_time = start_time + golden_goal_half
                        start_time = 0
                        seconds = [half_time]
                        half = 1
                        home_goal = away_goal = home_ready = away_ready = game_start = False # noqa
                        time.sleep(3)
                        timed_halves_group = initialize_timed_halves_screen(player_one_total, player_two_total, home_score, away_score, golden_goal_timer) # noqa
                        break
                    else:
                        display_winner = "Player 1" if player_one_total > player_two_total else "Player 2" # noqa
                        display_flash_message(' ', ' ', display_winner, 'Wins!!!') # noqa
                        half = leg = 1
                        start_time = home_score = away_score = player_one_count = player_two_count = player_two_total = player_one_total = 0 # noqa
                        home_goal = away_goal = home_ready = away_ready = game_start = False # noqa
                        home_led.value = away_led.value = True
                        seconds = [half_time]
                        time.sleep(3)
                        timed_halves_group = initialize_timed_halves_screen(player_one_total, player_two_total, home_score, away_score, half_time_timer) # noqa
                        break
