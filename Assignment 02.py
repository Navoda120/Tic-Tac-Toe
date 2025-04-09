                                                                                    # Assignment 02
#Registration Number :- 323586266
#Name :- D.M.T.Navoda Dissanayake

import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root  # Initialize the main window
        self.root.title("Tic-Tac-Toe")  # Set the title of the window

        # Set the current player to "X"
        self.current_player = "X"
        # Create a 3x3 board represented as a list of lists
        self.board = [[None for _ in range(3)] for _ in range(3)]

        # Create a 2D list to hold button references for the game grid
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()  # Call method to create the game board

    def create_board(self):
        # Create buttons for the Tic-Tac-Toe board
        for i in range(3):
            for j in range(3):
                # Create a button for each cell in the grid
                self.buttons[i][j] = tk.Button(
                    self.root,
                    text="",  # Initial text for the button
                    font=("Berlin Sans FB Demi", 24),  # Font size and style
                    height=2,
                    width=5,
                    bg="#4BC3E1",  # Set the background color of the buttons
                    command=lambda row=i, col=j: self.on_click(row, col)  # Button click action
                )
                self.buttons[i][j].grid(row=i, column=j)  # Place button in the grid layout

    def on_click(self, row, col):
        # Handle button click events
        try:
            if self.buttons[row][col]["text"] == "":  # Check if the cell is empty
                # Set the button text to the current player
                self.buttons[row][col]["text"] = self.current_player
                self.board[row][col] = self.current_player  # Update the board state

                # Check for a winner or draw
                if self.check_winner():
                    messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")  # Show winner message
                    self.reset_board()  # Reset the board for a new game
                    return
                elif self.check_draw():
                    messagebox.showinfo("Game Over", "It's a Draw!")  # Show draw message
                    self.reset_board()  # Reset the board for a new game
                    return

                # Switch to the next player
                self.current_player = "O" if self.current_player == "X" else "X"
            else:
                # Warn if the cell is already taken
                messagebox.showwarning("Invalid Move", "Cell already taken! Choose another cell.")
        except Exception as e:
            # Handle any unexpected errors
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

    def check_winner(self):
        # Check all possible winning combinations
        for i in range(3):
            # Check rows for a win
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] is not None:
                return True
            # Check columns for a win
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] is not None:
                return True

        # Check diagonals for a win
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            return True

        return False  # No winner found

    def check_draw(self):
        # Check if the board is full without a winner
        for row in self.board:
            if None in row:  # If there's an empty cell, it's not a draw
                return False
        return True  # All cells are filled and no winner, so it's a draw

    def reset_board(self):
        # Reset the game board for a new game
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""  # Clear button text
                self.board[i][j] = None  # Reset board state
        self.current_player = "X"  # Reset to the first player

if __name__ == "__main__":
    root = tk.Tk()  # Create the main application window
    game = TicTacToe(root)  # Create an instance of the game
    root.mainloop()  # Start the Tkinter main loop
