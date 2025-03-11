import random
import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"
random.seed(0)

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Game:
    def __init__(self, matrix,n,m):
        self.matrix = matrix
        self.N = n
        self.M = m
        self.izedeni=0
        self.tocki = self.count_tocki()

    def count_tocki(self):
        return sum(row.count('.') for row in self.matrix)

    def increment_izedeni(self):
        self.izedeni+=1

    def is_game_over(self):
        return self.izedeni == self.tocki


class Pacman:
    def __init__(self, matrix, n,m):
        self.player = (0,0)
        self.game = Game(matrix,n,m)
        self.matrix = matrix
        self.N = n
        self.M = m
        self.visited = set()
        self.visited.add((0,0))

    def playgame(self):
        nothing = False
        while True:
            if nothing: break

            i,j = self.player
            posakuvani = []
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for di,dj in directions:
                newi,newj = i+di,j+dj
                if 0<= newi < self.N and 0<=newj<self.M and self.matrix[newi][newj] == ".":
                    posakuvani.append((newi,newj))

            s= len(posakuvani)
            if s!=0:
                if s>1:
                    newi,newj = random.choice(posakuvani)
                else:
                    newi,newj = posakuvani[0]

                self.player = (newi, newj)
                self.game.matrix[newi][newj] = '#'
                self.game.increment_izedeni()
                print(f"[{newi}, {newj}]")
                #print(self.game.count_tocki())
                if self.game.is_game_over(): break

            else:
                izbor = random.choice(directions)
                counter=0
                while True:
                    newi = i+izbor[0]
                    newj = j+izbor[1]
                    counter+=1
                    if counter>=16:
                        print("Nothing to do here")
                        nothing = True
                        break
                    if 0<=newi<self.N and 0<=newj<self.M :
                       if(newi,newj) not in self.visited:
                           self.player = (newi, newj)
                           self.visited.add((newi,newj))
                           print(f"[{newi}, {newj}]")
                           #print(self.game.count_tocki())
                           break
                    izbor = random.choice(directions)




if __name__ == "__main__":
    N = int(input())
    M = int(input())

    matrix = []
    for i in range(N):
        a = list(input().strip())
        matrix.append(a)

    pacman = Pacman(matrix,N,M)
    pacman.playgame()