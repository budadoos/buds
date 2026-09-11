import pygame
import random  # Implemented to handle random AI moves

class TicTacToe:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((300, 300))
        pygame.display.set_caption("Tic Tac Toe")
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'  # Player is always 'X'
        self.font = pygame.font.Font(None, 74)
        self.running = True

    def draw_board(self):
        self.screen.fill((255, 255, 255))
        for i in range(1, 3):
            pygame.draw.line(self.screen, (0, 0, 0), (i * 100, 0), (i * 100, 300), 5)
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * 100), (300, i * 100), 5)

        for i in range(9):
            if self.board[i] != ' ':
                text = self.font.render(self.board[i], True, (0, 0, 0))
                self.screen.blit(text, ((i % 3) * 100 + 25, (i // 3) * 100 + 10))

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return True
        return False

    def reset_game(self):
        pygame.time.wait(1500) # Short delay so you can see the final board state
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def ai_move(self):
        # Find all current empty indices on the board
        empty_positions = [i for i, spot in enumerate(self.board) if spot == ' ']
        
        if empty_positions:
            # AI randomly picks one open index
            chosen_index = random.choice(empty_positions)
            self.board[chosen_index] = 'O'
            
            # Check if AI won or tied
            if self.check_winner():
                self.draw_board()
                pygame.display.flip()
                print("Player O (AI) wins!")
                self.reset_game()
            elif ' ' not in self.board:
                self.draw_board()
                pygame.display.flip()
                print("It's a tie!")
                self.reset_game()
            else:
                # Hand turn back to the Human Player
                self.current_player = 'X'

    def run(self):
        while self.running:
            self.draw_board()
            pygame.display.flip()

            # Handle the AI's move automatically when it is 'O's turn
            if self.current_player == 'O' and self.running:
                pygame.time.wait(500)  # Brief delay so the AI move doesn't feel instant
                self.ai_move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                # Human Player Move Strategy (Only acts when current_player is 'X')
                elif event.type == pygame.MOUSEBUTTONDOWN and self.current_player == 'X':
                    x, y = event.pos
                    row = y // 100
                    col = x // 100
                    index = row * 3 + col
                    
                    if self.board[index] == ' ':
                        self.board[index] = 'X'
                        
                        if self.check_winner():
                            self.draw_board()
                            pygame.display.flip()
                            print("Player X wins!")
                            self.reset_game()
                        elif ' ' not in self.board:
                            self.draw_board()
                            pygame.display.flip()
                            print("It's a tie!")
                            self.reset_game()
                        else:
                            # Switch turn over to the AI engine
                            self.current_player = 'O'

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
    pygame.quit()
