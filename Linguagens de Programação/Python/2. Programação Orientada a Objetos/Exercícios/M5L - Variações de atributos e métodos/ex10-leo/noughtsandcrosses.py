import os

class Noughtsandcrosses:
    # Private class attributes
    __playAgain = "s"
    __moves = 1
    __whoPlay = 2  # 1=Player1, 2=Player2
    __maxMoves = 10
    __victory = False
    __board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    
    @classmethod
    def screen(cls):
        os.system("cls")  # Clear the console
        print("    0   1   2")
        print("0:  " + cls.__board[0][0] + " | " + cls.__board[0][1] + " | " + cls.__board[0][2] )
        print("   -----------")
        print("1:  " + cls.__board[1][0] + " | " + cls.__board[1][1] + " | " + cls.__board[1][2])
        print("   -----------")
        print("2:  " + cls.__board[2][0] + " | " + cls.__board[2][1] + " | " + cls.__board[2][2])
        print("Moves: " + str(cls.__moves))

    @classmethod
    def player_1_Play(cls):
        if cls.__whoPlay == 2 and cls.__moves < cls.__maxMoves:
            try:
                l = int(input("Player 1 - Choose a Line: "))
                c = int(input("Player 1 - Choose a Column: "))
                if cls.__board[l][c] == " ":
                    cls.__board[l][c] = "X"
                    cls.__moves += 1
                    cls.__whoPlay = 1
                else:
                    print("Cell already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid Line or Column. Try again.")

    @classmethod
    def player_2_Play(cls):
        if cls.__whoPlay == 1 and cls.__moves < cls.__maxMoves:
            try:
                l = int(input("Player 2 - Choose a Line: "))
                c = int(input("Player 2 - Choose a Column: "))
                if cls.__board[l][c] == " ":
                    cls.__board[l][c] = "O"  # Player 2 uses "O"
                    cls.__moves += 1
                    cls.__whoPlay = 2
                else:
                    print("Cell already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid Line or Column. Try again.")

    @classmethod
    def verifyVictory(cls):
        victory = "n"
        symbols = ["X", "O"]

        for s in symbols:
            # Check Rows
            if cls.checkRows(s):
                victory = s
                break
            
            # Check Columns
            if cls.checkColumns(s):
                victory = s
                break
            
            # Check Diagonal
            if cls.checkDiagonal(s):
                victory = s
                break
            
            # Check Anti-Diagonal
            if cls.checkAntiDiagonal(s):
                victory = s
                break

        return victory

    @classmethod
    def checkRows(cls, s):
        for indexL in range(3):
            soma = 0
            for indexC in range(3):
                if cls.__board[indexL][indexC] == s:
                    soma += 1
            if soma == 3:
                return True
        return False

    @classmethod
    def checkColumns(cls, s):
        for indexC in range(3):
            soma = 0
            for indexL in range(3):
                if cls.__board[indexL][indexC] == s:
                    soma += 1
            if soma == 3:
                return True
        return False

    @classmethod
    def checkDiagonal(cls, s):
        soma = 0
        for i in range(3):
            if cls.__board[i][i] == s:
                soma += 1
        return soma == 3

    @classmethod
    def checkAntiDiagonal(cls, s):
        soma = 0
        for i in range(3):
            if cls.__board[i][2 - i] == s:
                soma += 1
        return soma == 3
    
    @classmethod
    def redefine(cls):
        cls.__playAgain = "s"
        cls.__moves = 0
        cls.__whoPlay = 2  # 1=Player1, 2=Player2
        cls.__maxMoves = 9
        cls.__victory = False
        cls.__board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
    
    @classmethod
    def play_game(cls):
        while True:
            cls.screen()
            cls.player_1_Play()
            cls.__victory = cls.verifyVictory()
            if cls.__moves >= cls.__maxMoves and cls.__victory == "n":
                cls.screen()
                print("Deu velha")
                break
            elif cls.__victory != "n":
                cls.screen()
                print("Player 1 won!!!")
                break
            cls.screen()
            cls.player_2_Play()
            cls.__victory = cls.verifyVictory()
            if cls.__moves >= cls.__maxMoves and cls.__victory == "n":
                cls.screen()
                print("Deu velha")
                break
            elif cls.__victory != "n":
                cls.screen()
                print("Player 2 won!!!!")
                break
