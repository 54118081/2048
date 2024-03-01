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
        # start the game 2048, and add two number to the grid
        for i in range(2):
            self.add_number()

        keyboard.on_press(self.press_key)
        while True:
            pass

    def add_number(self):
        # add 2 or 4 to an empty grid
        new_number = np.random.choice([2, 4], p=[0.9, 0.1])

        # choose a random empty grid
        while True:
            col = np.random.randint(0, 3)
            row = np.random.randint(0, 3)
            if self.matrix[row][col] == 0:
                self.matrix[row][col] = new_number
                return

    def display(self):
        print("------------------")
        print(pd.DataFrame(self.matrix))

    def press_key(self, event):
        # create a listener
        if event.name == 'w' or event.name == 'up':
            self.transpose()
            self.move_left()
            self.combine()
            self.transpose()
            self.display()
        elif event.name == 'a' or event.name == 'left':
            self.move_left()
            self.combine()
            self.display()
        elif event.name == 'd' or event.name == 'right':
            # reverse the element in each row
            # then combine them and reverse it back
            self.reverse()
            self.move_left()
            self.combine()
            self.reverse()
            self.display()
        elif event.name == 's' or event.name == 'down':
            self.transpose()
            self.reverse()
            self.move_left()
            self.combine()
            self.reverse()
            self.transpose()
            self.display()

    def combine(self):
        # add two same grid into one grid
        for row_i in range(4):
            col_i = 0

            # loop through each row
            # if current element is equal to next one
            # set 1st to 2 x current, 2nd to 0
            while col_i < 3:
                cur_row = self.matrix[row_i]
                if cur_row[col_i] == cur_row[col_i+1]:
                    self.matrix[row_i][col_i] *= 2
                    self.matrix[row_i][col_i+1] = 0
                    col_i += 2
                else:
                    col_i += 1
        self.move_left()

    def reverse(self):
        # reverse each row in the matrix
        for i in range(4):
            rev_lst = []
            for element in self.matrix[i]:
                rev_lst = [element] + rev_lst
            self.matrix[i] = rev_lst

    def transpose(self):
        # transpose the matrix
        self.matrix = list(map(list, zip(*self.matrix)))

    def move_left(self):
        # move all grid to the left
        for row_index in range(4):
            new_row = []
            for col_index in range(4):
                element = self.matrix[row_index][col_index]
                if element != 0:
                    new_row.append(element)
            while len(new_row) < 4:
                new_row.append(0)
            self.matrix[row_index] = new_row


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Game()


