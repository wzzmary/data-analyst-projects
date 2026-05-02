import copy
from interfaces import Board, Token
from morpion_here import MorpionHereStrategy,has_winner  # ton IA et la fonction utilitaire
from random_strategy import RandomStrategy     # IA bête

def play_game(strategy1, strategy2):
    board = Board(height=6, width=7, to_win=4)
    current_token = Token.YELLOW
    players = {Token.YELLOW: strategy1, Token.RED: strategy2}

    turn = 0
    while True:
        current_strategy = players[current_token]
        try:
            move = current_strategy.play(copy.deepcopy(board), current_token)
            board.play(move, current_token)
        except Exception as e:
            print(f"Erreur de {current_strategy._class_._name_}: {e}")
            break

        print(f"\nTour {turn} - {current_token.name} joue colonne {move}")
        print(board)
        print("-" * 30)

        # Vérification de victoire après chaque coup
        if has_winner(board, current_token):
            print(f"\n{current_token.name} a gagné en {turn + 1} coups !")
            print(board)
            break

        turn += 1
        if turn >= 42:
            print("Égalité !")
            break

        current_token = Token.RED if current_token == Token.YELLOW else Token.YELLOW

if __name__ == "_main_":
    bot1 = MorpionHereStrategy(Token.YELLOW)
    bot2 = RandomStrategy()
    play_game(bot1, bot2)