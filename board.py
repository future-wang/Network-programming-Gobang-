class Board(object):
    def __init__(self):
        self.locboard = [[0 for i in range(15)] for j in range(15)]
        self.direction = [[(0, -1), (0, 1)],  # UP Down
                          [(-1, 0), (1, 0)],  # Left Right
                          [(-1, -1), (1, 1)],  # leftUP to rightDOWN
                          [(1, -1), (-1, 1)]]  # rightUP to leftDOWN

    def draw(self, x, y, flag):
        self.locboard[x][y] = flag

    def getstate(self, x, y):
        if self.locboard[x][y] != 0:
            return False
        else:
            return True

    def isEnd(self, x, y, flag):
        tmpx = x
        tmpy = y
        for _ in self.direction:
            count = 1
            for dir in _:
                x = tmpx
                y = tmpy
                while True:
                    x = x + dir[0]
                    y = y + dir[1]
                    if 0 <= x < 15 and 0 <= y < 15 and self.locboard[x][y] == flag:
                        count = count + 1

                        if count >= 5:
                            print(f'Score:{count}')
                            return True
                    else:
                        print(f'Score:{count}')
                        break
        return False
