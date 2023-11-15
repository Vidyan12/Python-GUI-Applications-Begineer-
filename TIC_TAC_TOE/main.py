from tkinter import *
import numpy as np

# Constants for the game UI
size_of_board = 600
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 50
symbol_X_color = '#EE4035'
symbol_O_color = '#0492CF'
Green_color = '#7BC043'

class TicTacToeGame():
    def __init__(self):
        # Initialize the game window
        self.window = Tk()
        self.window.title('Tic-Tac-Toe')
        self.canvas = Canvas(self.window, width=size_of_board, height=size_of_board)
        self.canvas.pack()
        # Bind mouse click event
        self.window.bind('<Button-1>', self.click)

        # Initialize game state variables
        self.initialize_board()
        self.player_X_turns = True
        self.board_status = np.zeros(shape=(3, 3))

        # Scores
        self.player_X_score = 0
        self.player_O_score = 0
        self.tie_score = 0

        # Flags for game state
        self.player_X_starts = True
        self.reset_board = False
        self.game_over = False
        self.tie = False
        self.X_wins = False
        self.O_wins = False

    def mainloop(self):
        self.window.mainloop()

    def initialize_board(self):
        # Draw the initial tic-tac-toe board
        for i in range(2):
            self.canvas.create_line((i + 1) * size_of_board / 3, 0, (i + 1) * size_of_board / 3, size_of_board)
            self.canvas.create_line(0, (i + 1) * size_of_board / 3, size_of_board, (i + 1) * size_of_board / 3)

    def play_again(self):
        # Reset the board for a new game
        self.initialize_board()
        self.player_X_starts = not self.player_X_starts
        self.player_X_turns = self.player_X_starts
        self.board_status = np.zeros(shape=(3, 3))

    def draw_O(self, logical_position):
        # Draw O symbol on the canvas
        grid_position = self.convert_logical_to_grid_position(logical_position)
        self.canvas.create_oval(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
                                grid_position[0] + symbol_size, grid_position[1] + symbol_size,
                                width=symbol_thickness, outline=symbol_O_color)

    def draw_X(self, logical_position):
        # Draw X symbol on the canvas
        grid_position = self.convert_logical_to_grid_position(logical_position)
        self.canvas.create_line(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
                                grid_position[0] + symbol_size, grid_position[1] + symbol_size,
                                width=symbol_thickness, fill=symbol_X_color)
        self.canvas.create_line(grid_position[0] - symbol_size, grid_position[1] + symbol_size,
                                grid_position[0] + symbol_size, grid_position[1] - symbol_size,
                                width=symbol_thickness, fill=symbol_X_color)

    def display_game_over(self):
        # Display game over information and scores
        if self.X_wins:
            winner_text = ' Winner: Player 1 (X)'
            winner_color = symbol_X_color
            self.player_X_score += 1
        elif self.O_wins:
            winner_text = ' Winner: Player 2 (O)'
            winner_color = symbol_O_color
            self.player_O_score += 1
        else:
            winner_text = 'It\'s a tie'
            winner_color = 'gray'
            self.tie_score += 1

        self.canvas.delete("all")
        self.canvas.create_text(size_of_board / 2, size_of_board / 3, font="cmr 60 bold", fill=winner_color,
                                text=winner_text)

        # Display scores
        score_text = 'Scores \n'
        self.canvas.create_text(size_of_board / 2, 5 * size_of_board / 8, font="cmr 40 bold", fill=Green_color,
                                text=score_text)

        score_text = f'Player 1 (X): {self.player_X_score}\n'
        score_text += f'Player 2 (O): {self.player_O_score}\n'
        score_text += f'Tie                    : {self.tie_score}'
        self.canvas.create_text(size_of_board / 2, 3 * size_of_board / 4, font="cmr 30 bold", fill=Green_color,
                                text=score_text)

        # Display play again message
        play_again_text = 'Click to play again \n'
        self.canvas.create_text(size_of_board / 2, 15 * size_of_board / 16, font="cmr 20 bold", fill="gray",
                                text=play_again_text)

        self.reset_board = True

    def convert_logical_to_grid_position(self, logical_position):
        # Convert logical position to pixel position on the canvas
        logical_position = np.array(logical_position, dtype=int)
        return (size_of_board / 3) * logical_position + size_of_board / 6

    def convert_grid_to_logical_position(self, grid_position):
        # Convert pixel position to logical position on the board
        grid_position = np.array(grid_position)
        return np.array(grid_position // (size_of_board / 3), dtype=int)

    def is_grid_occupied(self, logical_position):
        # Check if a grid is already occupied
        return self.board_status[logical_position[0]][logical_position[1]] != 0

    def is_winner(self, player):
        # Check if a player has won
        player_value = -1 if player == 'X' else 1

        # Check rows and columns
        for i in range(3):
            if (self.board_status[i][0] == self.board_status[i][1] == self.board_status[i][2] == player_value) or \
                    (self.board_status[0][i] == self.board_status[1][i] == self.board_status[2][i] == player_value):
                return True

        # Check diagonals
        if (self.board_status[0][0] == self.board_status[1][1] == self.board_status[2][2] == player_value) or \
                (self.board_status[0][2] == self.board_status[1][1] == self.board_status[2][0] == player_value):
            return True

        return False

    def is_tie(self):
        # Check if the game is a tie (all grids are occupied)
        return not any(0 in row for row in self.board_status)

    def is_game_over(self):
        # Check if the game is over (either someone wins or all grids occupied)
        self.X_wins = self.is_winner('X')
        if not self.X_wins:
            self.O_wins = self.is_winner('O')

        if not self.O_wins:
            self.tie = self.is_tie()

        game_over = self.X_wins or self.O_wins or self.tie

        if game_over:
            if self.X_wins:
                print('Player 1 (X) wins!')
            elif self.O_wins:
                print('Player 2 (O) wins!')
            elif self.tie:
                print('It\'s a tie!')

        return game_over

    def click(self, event):
        # Handle mouse click event
        grid_position = [event.x, event.y]
        logical_position = self.convert_grid_to_logical_position(grid_position)

        if not self.reset_board:
            if self.player_X_turns:
                if not self.is_grid_occupied(logical_position):
                    self.draw_X(logical_position)
                    self.board_status[logical_position[0]][logical_position[1]] = -1
                    self.player_X_turns = not self.player_X_turns
            else:
                if not self.is_grid_occupied(logical_position):
                    self.draw_O(logical_position)
                    self.board_status[logical_position[0]][logical_position[1]] = 1
                    self.player_X_turns = not self.player_X_turns

            # Check if game is concluded
            if self.is_game_over():
                self.display_game_over()
        else:  # Play Again
            self.canvas.delete("all")
            self.play_again()
            self.reset_board = False

# Create an instance of the game and start the main loop
game_instance = TicTacToeGame()
game_instance.mainloop()
