class Board:
  #b represents a boardthrought the script
  # the boards list is used as a reference for which board an x is placed on
  boards = [(1,[]), (2,[]), (3,[])]
  #Dead boards contains the reference number of all boards which have been eliminated
  deadBoards = []
  #appends value to the correct board 
  def placeX(self, b, x, y):
    coordinate = (x , y)
    boardN = self.boards[b-1][1]
    if b in self.deadBoards:
        print("Board "+str(b)+" is dead")
        return False
    elif coordinate in boardN:
      print("X is already there")
      return False
    else:
      boardN.append(coordinate)
      print("appended")
      return True
  #main issue, always returns None
  #desinged to search list for dead boards, and add them to the dead board list
  def isBoardDead(self, b):
    boardN = self.boards[b-1][1]
    row1 = [((1,1),(2,1),(3,1))]
    row2 = [((1,2),(2,2),(3,2))]
    row3 = [((1,3),(2,3),(3,3))]
    col1 = [((1,1),(1,2),(1,3))]
    col2 = [((2,1),(2,2),(2,3))]
    col3 = [((3,1),(3,2),(3,3))]
    rDiagonal = [((1,3),(2,2),(3,1))]
    lDiagonal = [((3,3),(2,2),(1,1))]
    deadList = []
    deadList.extend((row1, row2, row3, col1, col2, col3, rDiagonal, lDiagonal))
    for i in range(0,7):
      if set(tuple(deadList[0][i])).issubset(tuple(boardN)):
        self.deadBoards.append(b)
        x = "Board "+str(b)+" is dead"
        return x
      else:
        return None
class Game:
  def gameTextBased(self):
    turnNumber = 0
    b = Board()
    while len(b.deadBoards) < 3:
      b1 = input("Choose Board")
      x1 = input("Choose Column")
      y1 = input("Choose Row")
      b.placeX(int(b1), int(x1), int(y1))
      print(b.isBoardDead(int(b1)))
      turnNumber += 1
    return turnNumber
      
    
t = Game()
if __name__ == '__main__':
  print("Play? Y or N")
  play = input()
  if play == "Y" or play == "y":
    while True:
      if t.gameTextBased() % 2 == 0:
        print("Player 2 Won") 
      else:
        print("player 1 Won")
      print("Play Again? Y or N")
      play1 = input()
      if play1 == "Y" or play1 == "y":
        pass
      else:
        break
  else:
    exit()
  exit()
