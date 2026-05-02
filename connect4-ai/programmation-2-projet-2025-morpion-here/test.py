from interfaces import Board, Token
from niamke_niamke import MorpionHereStrategy  # Ton IA
import random

# Adversaire : IA qui joue aléatoirement
class RandomStrategy:
    def authors(self):
        return "Random Bot"

    def play(self, board: Board, token: Token) -> int:
        valid_moves = [
            col for col in range(board.width)
            if Token.EMPTY in board.column(col)
        ]
        return random.choice(valid_moves)

# Vérifie si un joueur a gagné
def check_winner(board: Board, token: Token) -> bool:
    def has_n_in_row(lst):
        count = 0
        for t in lst:
            count = count + 1 if t == token else 0
            if count >= board.to_win:
                return True
        return False

    for i in range(board.height):
        if has_n_in_row(board.line(i)):
            return True
    for i in range(board.width):
        if has_n_in_row(board.column(i)):
            return True
    for diag in board.diagonals():
        if has_n_in_row(diag):
            return True
    return False

# Simule une partie entre deux IA
def simulate_game():
    board = Board(6, 7, 4)
    red_player = MorpionHereStrategy( Token.RED)     # Ton IA
    yellow_player = RandomStrategy()       # Adversaire
    players = [(red_player, Token.RED), (yellow_player, Token.YELLOW)]
    turn = 0

    while True:
        player, token = players[turn % 2]
        try:
            move = player.play(board, token)
            board.play(move, token)
        except Exception as e:
            print(f"{token.value} a causé une erreur : {e}")
            print(f"{token.value} perd par forfait.")
            break

        print(f"\n{token.value} joue en colonne {move}")
        print(board)

        if check_winner(board, token):
            print(f"\n🎉 Le joueur {token.value} a gagné !")
            break

        if all(Token.EMPTY not in board.column(c) for c in range(board.width)):
            print("\n🤝 Match nul (plateau rempli)")
            break

        turn += 1

# Lancer le test
if __name__ == "__main__":
    simulate_game()