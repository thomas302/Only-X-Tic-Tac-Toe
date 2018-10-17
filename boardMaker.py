class MakeBoards:
    def __init__(self):
        self.boardLength = 3
        self.separator = "+---"
        self.separatorEnd = "+"
        self.side = "|"
        self.boardSeparator = "   "
        self.boardAmount = 3
    def returnHorizontal(self):
        l = []
        for i in range(self.boardLength):
            l.append(self.separator)
        l.append(self.separatorEnd)
        s = ''.join(l)
        l = []
        for i in range(self.boardAmount):
            l.append(s)
            l.append(self.boardSeparator)
        l.append("\n")
        return ''.join(l)
    def returnSides(self, boards, row):
        list1 = []
        for x in range(self.boardAmount):
            l = []
            board = set(boards[x][1])
            for i in range(self.boardLength):
                s = {(i+1, row)}
                if s.issubset(board):
                    l.append(self.side + " x ")
                else:
                    l.append(self.side + "   ")
            l.append(self.side)
            l.append(self.boardSeparator)
            s = ''.join(l)
            list1.append(s)
        list1.append(str(row))
        list1.append("\n")
        return ''.join(list1)
    def returnBoards(self, boards):
        l = []
        row =1
        boardNumber = 0
        for i in range(self.boardLength):
            l.append(self.returnHorizontal() + self.returnSides( boards, i+1))
            boardNumber += 1
            row += 1
        l.append(self.returnHorizontal()+ "\n" + "  1   2   3       1   2   3       1   2   3" + "\n" + "      1               2               3    ")
        return ''.join(l)
        
        
        
        
    """
    +---+---+---+
    |   |   |   |
	+---+---+---+
    |   |   |   |
	+---+---+---+
    |   |   |   |
	+---+---+---+
      1   2   3
    """
if __name__ == '__main__':
    mb = MakeBoards()
    print(mb.returnBoards())
