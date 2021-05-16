from screens.display_message import build_display_message, display_flash_message # noqa
from helpers.increment import inc
from helpers.decrement import dec
from screens.classic_screen import build_classic_score_screen, initialize_classic_screen # noqa
from screens.edit_screen import build_classic_edit_screen
import board
import displayio
import framebufferio
import rgbmatrix
import time
import random
from audiocore import WaveFile


def classic_mode(increment, decrement, reset, enter, edit, home, away, home_led, away_led, start_stop_home, start_stop_away, h_bu, a_bu, fart_button, analog_out): # noqa
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

    home_score = away_score = player_one_wins = player_two_wins = edit_select = games_played = 0 # noqa

    home_goal = away_goal = home_ready = away_ready = edit_mode = game_start = False # noqa

    home_led.value = away_led.value = True

    best_of = 1

    single_whistle_file = open("audio_files/single_whistle.wav", "rb")
    single_whistle = WaveFile(single_whistle_file)

    three_whistles_file = open("audio_files/three_whistles.wav", "rb")
    three_whistles = WaveFile(three_whistles_file)

    goal_long_file = open("audio_files/goal_long.wav", "rb")
    goal_long = WaveFile(goal_long_file)

    goal_short_file = open("audio_files/goal_short.wav", "rb")
    goal_short = WaveFile(goal_short_file)

    classic_group = initialize_classic_screen(home_score, away_score, player_one_wins, player_two_wins) # noqa

    while True:
        if not fart_button.value:
            fart_file = open(f'audio_files/farts/fart_{str(random.randint(1, 35))}.wav', "rb") # noqa
            fart = WaveFile(fart_file)
            analog_out.play(fart)
        display.show(classic_group)
        display.refresh(minimum_frames_per_second=0)
        while not edit.value:
            edit_select = 0
            edit_mode = True
            build_display_message('Edit Mode')
            time.sleep(2)
            classic_group = build_classic_edit_screen(edit_select, best_of, home_score, away_score, 10) # noqa

        while edit_mode:  # edit before game start
            display.show(classic_group)
            display.refresh(minimum_frames_per_second=0)
            while not edit.value:
                if edit_select == 2:
                    edit_select = 0
                    classic_group = build_classic_edit_screen(edit_select, best_of, home_score, away_score, 10) # noqa
                    time.sleep(0.5)
                else:
                    edit_select = inc(edit_select)
                    if edit_select == 2:
                        classic_group = build_classic_edit_screen(edit_select, best_of, home_score, away_score, 10) # noqa
                    else:
                        classic_group = build_classic_edit_screen(edit_select, best_of, home_score, away_score, 10) # noqa
                    time.sleep(0.5)
            while not enter.value:
                edit_mode = False
                classic_group = initialize_classic_screen(home_score, away_score, player_one_wins, player_two_wins) # noqa
                time.sleep(0.5)

            if edit_select == 1:
                while not increment.value:
                    if away_score == 9:
                        break
                    else:
                        away_score = inc(away_score)
                        classic_group = build_classic_edit_screen(edit_select, best_of, home_score, away_score, 10) # noqa
                        time.sleep(0.5)
                while not decrement.value:
                    if away_score == 0:
                        break
                    else:
                        away_score = dec(away_score)
                        classic_group = build_classic_edit_screen(edit_select, best_of, home_score, away_score, 10) # noqa
                        time.sleep(0.5)
            elif edit_select == 2:
                while not increment.value:
                    best_of = inc(best_of, 2)
                    classic_group = build_classic_edit_screen(edit_select, best_of, home_score, away_score, 10) # noqa
                    time.sleep(0.5)
                while not decrement.value:
                    if best_of == 1:
                        break
                    else:
                        best_of = dec(best_of, 2)
                        classic_group = build_classic_edit_screen(edit_select, best_of, home_score, away_score, 10) # noqa
                        time.sleep(0.5)
            else:
                while not increment.value:
                    if home_score == 9:
                        break
                    else:
                        home_score = inc(home_score)
                        classic_group = build_classic_edit_screen(edit_select, best_of, home_score, away_score, 10) # noqa
                        time.sleep(0.5)
                while not decrement.value:
                    if home_score == 0:
                        break
                    else:
                        home_score = dec(home_score)
                        classic_group = build_classic_edit_screen(edit_select, best_of, home_score, away_score, 10) # noqa
                        time.sleep(0.5)

        if not start_stop_home.value:
            home_led.value = False
            home_ready = True

        if not start_stop_away.value:
            away_led.value = False
            away_ready = True

        if home_ready and away_ready:
            game_start = True
            build_display_message('Kick Off')
            time.sleep(1.5)
            analog_out.play(single_whistle)
            classic_group = initialize_classic_screen(home_score, away_score, player_one_wins, player_two_wins) # noqa

        if not reset.value:
            home_led.value = away_led.value = False
            return

        while game_start:  # In game play
            if not fart_button.value:
                fart_file = open(f'audio_files/farts/fart_{str(random.randint(1, 35))}.wav', "rb") # noqa
                fart = WaveFile(fart_file)
                analog_out.play(fart)
            while not edit.value:
                edit_mode = True
                build_display_message('Edit Mode')
                time.sleep(2)

            while edit_mode:
                while not edit.value:
                    if edit_select == 0:
                        edit_select = 1
                        classic_group = build_classic_edit_screen(edit_select, best_of, home_score, away_score, 10) # noqa
                        time.sleep(0.5)
                    else:
                        edit_select = 0
                        classic_group = build_classic_edit_screen(edit_select, best_of, home_score, away_score, 10) # noqa
                        time.sleep(0.5)
                while not enter.value:
                    edit_mode = False
                    classic_group = initialize_classic_screen(home_score, away_score, player_one_wins, player_two_wins) # noqa
                    display.show(classic_group)
                    display.refresh(minimum_frames_per_second=0)
                    time.sleep(0.5)
                if edit_select:
                    while not increment.value:
                        if away_score == 9:
                            break
                        else:
                            away_score = inc(away_score)
                            classic_group = build_classic_edit_screen(edit_select, best_of, home_score, away_score, 10) # noqa
                            time.sleep(0.5)
                    while not decrement.value:
                        if away_score == 0:
                            break
                        else:
                            away_score = dec(away_score)
                            classic_group = build_classic_edit_screen(edit_select, best_of, home_score, away_score, 10) # noqa
                            time.sleep(0.5)
                else:
                    while not increment.value:
                        if home_score == 9:
                            break
                        else:
                            home_score = inc(home_score)
                            classic_group = build_classic_edit_screen(edit_select, best_of, home_score, away_score, 10) # noqa
                            time.sleep(0.5)
                    while not decrement.value:
                        if home_score == 0:
                            break
                        else:
                            home_score = dec(home_score)
                            classic_group = build_classic_edit_screen(edit_select, best_of, home_score, away_score, 10) # noqa
                            time.sleep(0.5)
            if not home.value:
                home_score = inc(home_score)
                if away_score - home_score >= 5:
                    analog_out.play(goal_long)
                else:
                    analog_out.play(goal_short)
                classic_group = build_classic_score_screen(classic_group, home_score, away_score, player_one_wins, player_two_wins) # noqa
                home_goal = away_led.value = True
            elif not away.value:
                away_score = inc(away_score)
                if home_score - away_score >= 5:
                    analog_out.play(goal_long)
                else:
                    analog_out.play(goal_short)
                classic_group = build_classic_score_screen(classic_group, home_score, away_score, player_one_wins, player_two_wins) # noqa
                away_goal = home_led.value = True

            if home_score == 10 or away_score == 10:
                analog_out.play(three_whistles)
                winner = "Home Team" if home_score == 10 else "Away Team" # noqa
                home_goal = away_goal = home_ready = away_ready = game_start = home_led.value = away_led.value = False # noqa
                home_score = away_score = 0
                if games_played & 1:
                    if home_score == 10:
                        player_one_wins = inc(player_one_wins)
                        home_led.value = away_led.value = True
                    else:
                        player_two_wins = inc(player_two_wins)
                        home_led.value = away_led.value = True
                else:
                    if home_score == 10:
                        player_two_wins = inc(player_two_wins)
                        home_led.value = away_led.value = True
                    else:
                        player_one_wins = inc(player_one_wins)
                        home_led.value = away_led.value = True
                classic_group = build_classic_score_screen(classic_group, home_score, away_score, player_one_wins, player_two_wins) # noqa
                games_played = inc(games_played)
                if best_of == 1:
                    display_flash_message(winner, 'WINS!!!')
                    time.sleep(0.5)
                    player_one_wins = player_two_wins = 0
                    game_start = False
                    classic_group = build_classic_score_screen(classic_group, home_score, away_score, player_one_wins, player_two_wins) # noqa
                    break
                display_flash_message(winner, 'WINS!!!', 'Switch', 'Sides')
                time.sleep(0.5)

            if player_one_wins == best_of or player_one_wins > best_of / 2:
                display_flash_message('Player 1', 'WINS!!!')
                player_one_wins = player_two_wins = 0
                time.sleep(3)
                game_start = False
                break

            if player_two_wins == best_of or player_two_wins > best_of / 2:
                display_flash_message('Player 2', 'WINS!!!')
                player_one_wins = player_two_wins = 0
                time.sleep(3)
                game_start = False
                break

            if not reset.value:
                game_start = home_ready = away_ready = False
                home_led.value = away_led.value = True
                home_score = away_score = 0
                classic_group = initialize_classic_screen(home_score, away_score, player_one_wins, player_two_wins) # noqa
                time.sleep(0.5)
                break

            while home_goal:
                display.show(classic_group)
                display.refresh(minimum_frames_per_second=0)
                if not start_stop_away.value or not a_bu.value:
                    while not start_stop_away.value or not a_bu.value:
                        home_goal = False
                    away_led.value = False
                    break
                elif not reset.value:
                    while not reset.value:
                        game_start, home_ready, away_ready = False
                        home_led.value = away_led.value = True
                        home_score = away_score = 0
                        classic_group = initialize_classic_screen(home_score, away_score, player_one_wins, player_two_wins) # noqa
                        time.sleep(0.5)
                    break

            while away_goal:
                display.show(classic_group)
                display.refresh(minimum_frames_per_second=0)
                if not start_stop_home.value or not h_bu.value:
                    while not start_stop_home.value or not h_bu.value:
                        away_goal = False
                    home_led.value = False
                    break
                elif not reset.value:
                    while not reset.value:
                        game_start, home_ready, away_ready = False
                        home_led.value = away_led.value = True
                        home_score = away_score = 0
                        classic_group = initialize_classic_screen(home_score, away_score, player_one_wins, player_two_wins) # noqa
                        time.sleep(0.5)
                    break
