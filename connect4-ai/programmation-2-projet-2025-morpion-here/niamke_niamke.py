import copy
from interfaces import Strategy, Board, Token
import random


"""
Cette fonction has_winner a pour but de trouver les alignements gagnants en verifiant les colonnes les lignes et es diagonales par lot de 4 aussi appelé 
fenêtre au morpion cette fonction nous sera tres utile pour pour notre fonction d'evaluation du plateau 
"""
def has_winner(board: Board, token: Token) -> bool:
    height = board.height
    width = board.width
    to_win = board.to_win

    # Vérification des lignes (horizontales)
    for row in range(height):
        line = board.line(row)


        for col in range(width - to_win + 1):
            gagnant = True
            for i in range(to_win):
                if line[col + i] != token:
                    gagnant = False
                    break
            if gagnant:
                return True

    # Vérification des colonnes
    for col in range(width):
        column = board.column(col)

        for row in range(height - to_win + 1):
            gagnant = True
            for i in range(to_win):
                if column[row + i] != token:
                    gagnant = False
                    break
            if gagnant:
                return True

    # Vérification des diagonales descendantes (\)
    for row in range(height - to_win + 1):
        for col in range(width - to_win + 1):
            gagnant = True
            for i in range(to_win):
                if board.box(row + i, col + i) != token:
                    gagnant = False
                    break
            if gagnant:
                return True

    # Vérification des diagonales montantes (/)
    for row in range(to_win - 1, height):
        for col in range(width - to_win + 1):
            gagnant = True
            for i in range(to_win):
                if board.box(row - i, col + i) != token:
                    gagnant = False
                    break
            if gagnant:
                return True

    return False





class MorpionHereStrategy(Strategy):
    """
        Intelligence Artificielle pour Puissance 4 - MiniMax.
        """

    def _init_(self, color: Token):
        self.color = color
        self.name = "MorpionHereStrategy"
        self.depth = 5


    def authors(self) -> str:
        return "Marie Esther NIAMKE, Sephora Emmanuela NIAMKE"

    """
    Notre fonction d'evaluation commence avec la premiere fonction qu'on a implemente hors de 
    la sous-classe Morpionherestrategy ,elle sera utilisé ici por directement determiner qui est le gagnant si on a un alignement
    de 4 pions identiques a ce stade du jeu 
    """

    def evaluate_board(self, board: Board, your_token: Token) -> int:
        if has_winner(board, your_token):
            return 1000000
        if your_token == Token.YELLOW:
            opponent = Token.RED
        else:
            opponent = Token.YELLOW
        if has_winner(board, opponent):
            return -1000000

        """
        Cette fonction d'evaluation va calculer le score du plateau du point de vu de notre IA,your_token plus
         le score est eleve plus le pion et en bonne position pour prendre par la suite la meilleur décision
        Cette fonction utilise des heuristiques basées sur les alignements, la centralité et la menace de victoire. 
        """

        score = 0

        def count_token(lst, token)-> int :
            count = 0
            for i in range(len(lst) - 3):
                window = lst[i:i + 4]
                if window.count(token) == 4:
                    count += 200
                elif window.count(token) == 3 and window.count(Token.EMPTY) == 1:
                    count += 5
                elif window.count(token) == 2 and window.count(Token.EMPTY) == 2:
                    count += 2
            return count

        for i in range(board.height):
            score += count_token(board.line(i), your_token)
            score -= count_token(board.line(i), opponent)

        for i in range(board.width):
            score += count_token(board.column(i), your_token)
            score -= count_token(board.column(i), opponent)

        for diag in board.diagonals():
            score += count_token(diag, your_token)
            score -= count_token(diag, opponent)


        center_column = board.column(board.width // 2)
        center_count = center_column.count(your_token)
        score += center_count * 3

        return score



    def minimax(self, board: Board, depth: int, maximizing: bool, token: Token,alpha:int,beta:int) -> tuple[int, int]:
        """
        Cette fonction minimax vue en cours va Implémente l’algorithme MiniMax avec élagage Alpha-Beta pour simuler les coups à venir avec une plus grande profondeur
        Notre elagage alpha beta va nous permettra d'explorer plusieurs branches prometteuses plus rapidement in coupant les branches ou l'adversaire nous a deja bloqeur et
        ou ils nous sera impossible dd'avoir plus que ce quon a deja
         cette fonction Minimax nous renvoi un tuple (score, colonne) le meilleur score(high_score) trouvé et la colonne associée.(col_best)
         """



        valid_moves = []
        for col in range(board.width):
            if Token.EMPTY in board.column(col):
                valid_moves.append(col)

        if depth == 0 or not valid_moves:
            return self.evaluate_board(board, token), -1


        col_best = random.choice(valid_moves)

        if maximizing == True:
            high_score = -1000000

            for col in valid_moves:
                simulation_board = copy.deepcopy(board)
                simulation_board.play(col, token)
                score_evalue,_ = self.minimax(simulation_board, depth - 1, False, token,alpha, beta)


                if score_evalue > high_score:
                    high_score = score_evalue
                    col_best = col

                alpha = max (alpha, high_score)
                if beta <= alpha:
                    break


            return high_score, col_best


        else:
            low_score = 1000000
            opponent = Token.RED if token == Token.YELLOW else Token.YELLOW

            for col in valid_moves:
                simulation_board = copy.deepcopy(board)
                simulation_board.play(col, opponent)
                score_evalue, _ = self.minimax(simulation_board, depth - 1, True, token,alpha, beta)

                if score_evalue < low_score:
                    low_score = score_evalue
                    col_best = col

                beta = min(beta, low_score)

                if beta <= alpha:
                    break


            return low_score, col_best



        """
        Cette fonction play va choisir et retourner la colonne à jouer pour l’IA sur le plateau 'current_board' avec le jeton 'your_token'.
        elle utilise l’algorithme MiniMax pour déterminer le meilleur coup de plus elle gère toute exception pour éviter le forfait."""


    def play(self, current_board: Board, your_token: Token) -> int:

       try:
          _, best_move = self.minimax(current_board, depth=self.depth, maximizing=True, token=your_token,alpha=-1000000,beta=1000000)
          return best_move

       except Exception as e:
             # En cas de bug, on joue un coup valide au hasard pour éviter le forfait
            valid_moves = [col for col in range(current_board.width) if Token.EMPTY in current_board.column(col)]
            if valid_moves:
               return random.choice(valid_moves)
            else:
                # Plateau plein, pas de coup possible
               return 0