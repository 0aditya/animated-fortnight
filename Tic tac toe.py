
import tkinter as tk
from tkinter import messagebox

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def handle_click(row, col):
    global board, current_player, buttons

    if board[row][col] == " ":
        player = players[current_player]
        buttons[row][col].config(text=player)
        board[row][col] = player

        if check_win(board, player):
            messagebox.showinfo("Tic Tac Toe", f"Player {player} wins!")
            update_score(player)
            root.quit()
        elif is_board_full(board):
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            root.quit()
        else:
            current_player = (current_player + 1) % 2

def update_score(player):
    global scores
    scores[player] += 1
    score_label.config(text=f"Scores: X - {scores['X']}   O - {scores['O']}")

def reset_game():
    global board, current_player, buttons
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = 0

    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=" ")

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")

board = [[" " for _ in range(3)] for _ in range(3)]
players = ["X", "O"]
current_player = 0
scores = {"X": 0, "O": 0}

buttons = []

# Create the buttons for the Tic Tac Toe grid
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(root, text=" ", font=("Helvetica", 20), width=6, height=3,
                           command=lambda r=row, c=col: handle_click(r, c))
        button.grid(row=row, column=col)
        button_row.append(button)
    buttons.append(button_row)

# Create a Reset button
reset_button = tk.Button(root, text="Reset", font=("Helvetica", 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)

# Create a label to display the scoreboard
score_label = tk.Label(root, text="Scores: X - 0   O - 0", font=("Helvetica", 16))
score_label.grid(row=4, column=0, columnspan=3)

# Start the GUI event loop
root.mainloop()
#%%
import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.players = ["X", "O"]
        self.current_player = 0
        self.scores = {"X": 0, "O": 0}

        self.buttons = []
        self.create_board_buttons()
        self.create_reset_button()
        self.create_score_label()

    def create_board_buttons(self):
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(self.root, text=" ", font=("Helvetica", 20), width=6, height=3,
                                   command=lambda r=row, c=col: self.handle_click(r, c))
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

    def create_reset_button(self):
        reset_button = tk.Button(self.root, text="Reset", font=("Helvetica", 14), command=self.reset_game)
        reset_button.grid(row=3, column=0, columnspan=3)

    def create_score_label(self):
        self.score_label = tk.Label(self.root, text="Scores: X - 0   O - 0", font=("Helvetica", 16))
        self.score_label.grid(row=4, column=0, columnspan=3)

    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)

    def check_win(self, player):
        # Check rows, columns, and diagonals for a win
        for row in self.board:
            if all(cell == player for cell in row):
                return True

        for col in range(3):
            if all(row[col] == player for row in self.board):
                return True

        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False

    def is_board_full(self):
        return all(cell != " " for row in self.board for cell in row)

    def handle_click(self, row, col):
        if self.board[row][col] == " ":
            player = self.players[self.current_player]
            self.buttons[row][col].config(text=player)
            self.board[row][col] = player

            if self.check_win(player):
                messagebox.showinfo("Tic Tac Toe", f"Player {player} wins!")
                self.update_score(player)
                self.root.quit()
            elif self.is_board_full():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.root.quit()
            else:
                self.current_player = (self.current_player + 1) % 2

    '''def update_score(self, player):
        self.scores[player] += 1
        self.score_label.config(text=f"Scores: X - {self.scores['X']}   O - {self.scores['O']}")'''

    def reset_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = 0

        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=" ")

if __name__ == "__main__":
    root = tk.Tk()
    tictactoe_gui = TicTacToeGUI(root)
    root.mainloop()


