import pandas as pd
import numpy as np
import keyboard


class Game:
    def __init__(self):
        self.matrix = [[0 for x in range(4)] for x in range(4)]
        self.current = 0
        self.best = 0
        self.game_start()

    def game_start(self):
        # start the game 2048, and add two number to the block
        for i in range(2):
            self.add_number()

        keyboard.on_press(press_key)
        while True:
            pass
            # print(pd.DataFrame(self.matrix))

    def add_number(self):
        # add 2 or 4 to an empty space
        new_number = np.random.choice([2, 4], p=[0.9, 0.1])

        # choose a random empty block
        while True:
            col = np.random.randint(0, 3)
            row = np.random.randint(0, 3)
            if self.matrix[row][col] == 0:
                self.matrix[row][col] = new_number
                return


def press_key(event):
    # create a listener
    if event.name == 'w' or event.name == 'up':
        print("move up")
    elif event.name == 'a' or event.name == 'left':
        print("move left")
    elif event.name == 'd' or event.name == 'right':
        print("move right")
    elif event.name == 's' or event.name == 'down':
        print("move down")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Game()


