import pyautogui as pag
from stockfish import Stockfish

robot = Stockfish(path="stockfish", depth=20)
white_a1_position = (82, 865)
black_a1_position = (687, 270)
step = 90
menu = "1-opponent move : 2-Best move"
def opponent_move(oppmove):
    if robot.is_move_correct(oppmove):
        robot.make_moves_from_current_position([oppmove])


def get_best_move():
    return robot.get_best_move()


def do_best_move(color):
    move = robot.get_best_move()
    x1 = int(ord(move[0])) - 97
    y1 = int(move[1]) - 1
    x2 = int(ord(move[2])) - 97
    y2 = int(move[3]) - 1
    if color == "white":
        a1_position = white_a1_position
        pag.moveTo(a1_position[0] + (x1 * step), a1_position[1] - (y1 * step))
        pag.leftClick()
        pag.moveTo(a1_position[0] + (x2 * step), a1_position[1] - (y2 * step))
        pag.leftClick()
        robot.make_moves_from_current_position([move])
    else:
        a1_position = black_a1_position
        pag.moveTo(a1_position[0] - (x1 * step), a1_position[1] + (y1 * step))
        pag.leftClick()
        pag.moveTo(a1_position[0] - (x2 * step), a1_position[1] + (y2 * step))
        pag.leftClick()
        robot.make_moves_from_current_position([move])

    pag.leftClick(1416, 695)


def main():

    color = input("color: ")
    my_turn = True if color == "white" else False
    while True:
        if my_turn:
            do_best_move(color)
            my_turn = False
        else:
            opp_move = input('Input opponent move:')
            if opp_move == 'exit':
                break
            else:
                opponent_move(opp_move)
            my_turn = True



    pass


if __name__ == "__main__":
    main()

