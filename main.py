import pyautogui as pag
#   from ChessVision import ChessVision
from stockfish import Stockfish

robot = Stockfish(path="stockfish", depth=20)
white_a1_position = (82, 865)
black_a1_position = (687, 270)
step = 90
menu = "1-opponent move : 2-Best move"
# for computer vision find yellow pixel
# should be two seperate squares in
# image find center pixel and check
# color if yellow that is starting
# x if color is end position


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
        pag.leftClick()
        pag.moveTo(a1_position[0] + (x2 * step), a1_position[1] - (y2 * step))
        pag.leftClick()
        robot.make_moves_from_current_position([move])
    else:
        a1_position = black_a1_position
        pag.moveTo(a1_position[0] - (x1 * step), a1_position[1] + (y1 * step))
        pag.leftClick()
        pag.leftClick()
        pag.moveTo(a1_position[0] - (x2 * step), a1_position[1] + (y2 * step))
        pag.leftClick()
        robot.make_moves_from_current_position([move])

    pag.leftClick(1416, 695)


def main():
    color = input("color: ")
    if color == "white":
        my_turn = True
    else:
        my_turn = False
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



        # if menuChoice == 1:
        #     oppmove = input('Input opponent move:')
        #     opponent_move(oppmove)
        #     print(robot.get_board_visual())
        #     menuChoice = int(input(menu))
        # elif menuChoice == 2:
        #     move = get_best_move()
        #     print(move)
        #     robot.make_moves_from_current_position([move])
        #     menuChoice = int(input(menu))
        # elif menuChoice == 3:
        #     do_best_move(color)
        #     menuChoice = int(input(menu))
        # else:
        #     break

    pass


if __name__ == "__main__":
    main()

