import os
import random
from tabnanny import check

os.environ["OPENBLAS_NUM_THREADS"] = "1"
random.seed(0)


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Game:
    def __init__(self, matrix, n, m):
        self.matrix = matrix
        self.n = n
        self.m = m
        self.tocki = self.countTocki()
        self.izedeni = 0

    def countTocki(self):
        return sum(row.count('.') for row in self.matrix)

    def incrementIzedeni(self):
        self.izedeni += 1

    def check(self):
        return self.izedeni == self.tocki


class Pacman:
    def __init__(self, matrix, n, m):
        self.player = Player(0, 0)
        self.game = Game(matrix, n, m)
        self.n = n
        self.m = m
        self.visited = set()
        self.visited.add((0, 0))

    def playGame(self):
        nothing = False
        while True:
            if nothing: break

            i = self.player.y
            j = self.player.x
            posakuvani = []
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for di, dj in directions:
                new_i = i + di
                new_j = j + dj
                if 0 <= new_i < self.n and 0 <= new_j < self.m and matrix[new_i][new_j] == '.': posakuvani.append(
                    (new_i, new_j))

            s = len(posakuvani)
            if s != 0:
                if s > 1:
                    new_i, new_j = random.choice(posakuvani)
                else:
                    new_i, new_j = posakuvani[0]

                self.player.x, self.player.y = new_j, new_i
                self.game.matrix[new_i][new_j] = '#'

                print(f"{new_i},{new_j}")
                self.game.incrementIzedeni()

                if self.game.check(): break
            else:
                izbor = random.choice(directions)
                ctr = 0
                while True:
                    new_i = i + izbor[0]
                    new_j = j + izbor[1]
                    ctr += 1
                    if ctr >= 16:
                        print("Nothing to do here")
                        nothing = True
                        break
                    if 0 <= new_i < self.n and 0 <= new_j < self.m:
                        # Check if the new position is not visited and can move to a dot
                        if (new_i, new_j) not in self.visited:
                            self.player.x, self.player.y = new_j, new_i
                            print(f"{new_i},{new_j}")
                            self.visited.add((new_i, new_j))
                            break
                    izbor = random.choice(directions)


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    matrix = []
    for _ in range(n):
        line = list(input())
        matrix.append(line)

    p = Pacman(matrix, n, m)
    p.playGame()