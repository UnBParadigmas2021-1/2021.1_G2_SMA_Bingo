import random

class Card():
  def __init__(self):
    self.numbers = [[0 for x in range(5)] for y in range(5)]
    self.count = 0
    self.fill_matriz()
  
  
  def fill_matriz(self):
    matriz = random.sample(range(1, 75), 25)
    k = 0
    matriz.sort()

    for i in range(5):
      for j in range(5):
        self.numbers[i][j] = matriz[k]
        k+=1
  
  def check_number(self, number):
    for i in range(5):
      for j in range(5):
        if self.numbers[i][j] == number:
          self.numbers[i][j] = 0
          self.count += 1
    print(self.numbers)

  def check_bingo(self):
    print(self.count)
    return self.count == 25