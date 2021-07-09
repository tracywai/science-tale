class WordHuntBoard:

    def __init__(self):
        self.board = ['_']* 16

    def print_board(self):
        for i in range(0,len(self.board),4):
            print (' '.join(self.board[i:i+4]))

    def shake(self):
        pass
    
b = WordHuntBoard()

b.print_board()
