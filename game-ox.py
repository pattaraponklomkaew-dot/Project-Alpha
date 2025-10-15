import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("OX Game (Tic-Tac-Toe)")
        self.current_player = "X"
        self.board = [ [None]*3 for _ in range(3) ]
        self.buttons = [ [None]*3 for _ in range(3) ]
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.root, text="", font=("Arial", 32), width=4, height=2,
                                command=lambda row=i, col=j: self.on_click(row, col))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn

    def on_click(self, row, col):
        if self.buttons[row][col]["text"] == "" and not self.check_winner():
            self.buttons[row][col]["text"] = self.current_player
            self.board[row][col] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        b = self.board
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] != None:
                return True
            if b[0][i] == b[1][i] == b[2][i] != None:
                return True
        if b[0][0] == b[1][1] == b[2][2] != None:
            return True
        if b[0][2] == b[1][1] == b[2][0] != None:
            return True
        return False

    def is_draw(self):
        return all(self.board[i][j] is not None for i in range(3) for j in range(3))

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
                self.board[i][j] = None
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
