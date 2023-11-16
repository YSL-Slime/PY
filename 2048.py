import random

class Table:
    def __init__(self):
        self.field = [[0 for i in range(4)] for i in range(4)]
        x = random.randint(0, 3)
        self.field[x][x] = 2
        if x == 0:
            self.field[3][3] = 2
        elif x == 3:
            self.field[0][0] = 2
        else:
            self.field[x-1][x] = 2
    
    def move(self, x, y, c):
        match c:
            case 'l':
                for i in range(y-1, -1, -1):
                    if self.field[x][i] == 0:
                        if i == 0:
                            self.field[x][i] = self.field[x][y]
                            self.field[x][y] = 0
                            break
                        continue
                    elif self.field[x][i] > self.field[x][y] or self.field[x][i] < self.field[x][y]:
                        print("U cant do that") 
                        break
                    elif self.field[x][i] == self.field[x][y]:
                        self.field[x][i] *= 2
                        self.field[x][y] = 0
                        break
            case 'r':
                for i in range(y+1, 4):
                    if self.field[x][i] == 0:
                        if i == 3:
                            self.field[x][i] = self.field[x][y]
                            self.field[x][y] = 0
                            break
                        continue
                    elif self.field[x][i] > self.field[x][y] or self.field[x][i] < self.field[x][y]:
                        print("U cant do that") 
                        break
                    elif self.field[x][i] == self.field[x][y]:
                        self.field[x][i] *= 2
                        self.field[x][y] = 0
                        break
            case 'u':
                for i in range(x-1, -1, -1):
                    if self.field[i][y] == 0:
                        if i == 0:
                            self.field[i][y] = self.field[x][y]
                            self.field[x][y] = 0
                            break
                        continue
                    elif self.field[i][y] > self.field[x][y] or self.field[i][y] > self.field[x][y]:
                        print("U cant do that") 
                        break
                    elif self.field[i][y] == self.field[x][y]:
                        self.field[i][y] *= 2
                        self.field[x][y] = 0
                        break
            case 'd':
                for i in range(x+1, 4):
                    if self.field[i][y] == 0:
                        if i == 3:
                            self.field[i][y] = self.field[x][y]
                            self.field[x][y] = 0
                            break
                        continue
                    elif self.field[i][y] > self.field[x][y] or self.field[i][y] > self.field[x][y]:
                        print("U cant do that") 
                        break
                    elif self.field[i][y] == self.field[x][y]:
                        self.field[i][y] *= 2
                        self.field[x][y] = 0
                        break
        
        x = random.randint(0, 3)
        xs = [x]
        ct = 1
        
        while True:
            if 0 in self.field[x]:
                while True:
                    z = random.randint(0, 3)
                    if self.field[x][z] == 0:
                        self.field[x][z] = 2
                        break
                    else:
                        z = random.randint(0, 3)
                break
            else:
                if ct == 4:
                    break
                while x in xs:
                    x = random.randint(0, 3)
                xs.append(x)
                ct += 1
                
polje = Table()

c = 'p'

while(c != 'q'):
    if c == 'p':
        print("Welcome to 2048! GL!")
    
    for i in polje.field:
        print(i)
        
    x, y, c = input("Type in the: x(0-3) y(0-3) direction(u, d, l, r): ").split()
    polje.move(int(x), int(y), c)