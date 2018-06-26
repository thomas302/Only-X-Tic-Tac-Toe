class Board:
  #b represents a boardthrought the script
  boards = [(1,[]), (2,[]), (3,[])]
  deadBoards = []
  def placeX(self, b, x, y):
    coordinate = (x , y)
    boardN = self.boards[b-1][1]
    if b in deadBoards:
      return False
    elif coordinate in boardN:
      return False
    else:
      boardN.append(coordinate)
      return True
  def isBoardDead(self, b):
    boardN = self.boards[b-1][1]
    row1 = [(1,1),(2,1),(3,1)]
    row2 = [(1,2),(2,2),(3,2)]
    row3 = [(1,3),(2,3),(3,3)]
    col1 = [(1,1),(1,2),(1,3)]
    col2 = [(2,1),(2,2),(2,3)]
    col3 = [(3,1),(3,2),(3,3)]
    rDiagonal = [(1,3)(2,2)(3,1)]
    lDiagonal = [(3,3)(2,2)(1,1)]
    deadList = [ row1, row2, row3, col1, col2, col3, rDiagonal, lDiagonal]
    for i in range(0,7):
      if set(deadList[i]).issubset(boardN):
        self.deadBoards.append(b)
      else:
        pass
class Turn:
  def turnTextBased(self):
    b1 = eval(input("Choose Board"))
    x1 = eval(input("Choose Column"))
    y1 = eval(input("Choose Row"))
    Board.placeX(self, b1, x1, y1)
    
    
def main():
  if __name__ == '__main__':
    
