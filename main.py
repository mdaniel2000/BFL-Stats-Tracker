from scoreboard import Scoreboard
from team import Team
import keyboard


def drive(offense, defense, scoreboard):
    if keyboard.is_pressed('3'):
        offense.front_cups -= 1
    elif keyboard.is_pressed('2'):
        offense.middle_cups -= 1
    elif keyboard.is_pressed('1'):
        offense.back_cups -= 1


if __name__ == '__main__':

    board = Scoreboard()
    home = Team()
    away = Team()

    if keyboard.is_pressed('1'):
        possession = home.get_possession()
    elif keyboard.is_pressed('2'):
        possession = away.get_possession()

    while board.half == 1:
        if home.possession:
            drive(home, away, board)
        else:
            drive(away, home, board)

        if keyboard.is_pressed('q'):
            board.end_half()

    while board.half == 2:
        if home.possession:
            drive(home, away, board)
        else:
            drive(away, home, board)

        if keyboard.is_pressed('q'):
            board.end_game()
