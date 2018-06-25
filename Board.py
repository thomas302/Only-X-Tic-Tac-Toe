class Board(self):
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
class Turn(self):
  def turn(self):
    b1 = eval(input("Choose Board"))
    x1 = eval(input("Choose Column"))
    y1 = eval(input("Choose Row"))
    Board.placeX(self, b1, x1, y1)
    
def main():
  if __name__ == '__main__':
    
