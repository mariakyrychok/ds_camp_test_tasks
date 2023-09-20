import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
from matplotlib import animation
from typing import Literal, Callable

CellState = Literal[0, 1]
GameRules = Callable[[CellState, int], CellState]


def default_rules(cell_value, num_alive_neighbours):
    if num_alive_neighbours == 3:
        return 1
    elif num_alive_neighbours == 2:
        return cell_value
    return 0


class Game:
    def __init__(self, board: np.array, rules: GameRules = default_rules):
        self.board = board
        self.rules = rules

    def next_state(self):
        new_board = np.copy(self.board)
        rows, columns = self.board.shape
        for row in range(rows):
            for col in range(columns):
                num_alive_neighbours = self.get_num_alive_neighbours(row, col)
                new_board[row][col] = self.rules(self.board[row][col], num_alive_neighbours)
        return new_board

    def advance(self):
        self.board = self.next_state()

    def get_num_alive_neighbours(self, row, col):
        num_alive_neighbours = 0
        neighbour_coordinates = (
            (row - 1, col - 1), (row - 1, col), (row - 1, col + 1), (row, col - 1),
            (row, col + 1), (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)
        )
        for row, col in neighbour_coordinates:
            num_alive_neighbours += self.value_at(row, col)
        return num_alive_neighbours

    def value_at(self, row, col):
        rows, columns = self.board.shape
        return self.board[row % rows][col % columns]


def generate_random_board(rows, columns):
    return np.random.randint(2, size=(rows, columns))


def request_board_shape():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    return rows, columns


def seventh_iteration():
    game = Game(np.array([
        [1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 1],
        [1, 0, 0, 1, 0, 0, 1],
        [0, 1, 1, 0, 1, 1, 0],
        [1, 1, 1, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 0, 1]
    ]))
    for i in range(7):
        game.advance()
    print('Task 2.0. The seventh iteration of the Game of Life:')
    print(game.board)


def infinite_random():
    rows, columns = request_board_shape()
    game = Game(generate_random_board(rows, columns))
    print('Task 2.1. The Infinite iteration of the Game of Life:')
    while True:
        print(game.board)
        game.advance()
        time.sleep(2)


def infinite_random_visualized():
    fig = plt.figure()
    plt.axis('off')
    plt.title('Task 2.2. The Infinite iteration of the Game of Life with visualization', fontsize=9, pad=10)
    rows, columns = request_board_shape()
    game = Game(generate_random_board(rows, columns))

    def animate(i):
        sns.heatmap(game.board, annot=False, cbar=False, cmap=['#d9edcb', '#38761d'], linewidths=1, square=True)
        game.advance()

    anim = animation.FuncAnimation(fig, animate, frames=None, repeat=False, cache_frame_data=False, interval=250)
    plt.show()


def main():
    # task 2.0
    #seventh_iteration()
    # task 2.1
    #infinite_random()
    # task 2.2
    infinite_random_visualized()


if __name__ == '__main__':
    main()
