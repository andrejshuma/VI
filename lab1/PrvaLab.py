from imports.util import *
from imports.uninformed_search import *


def straight(state):
    snake = state[0]
    snake_dir = state[1]
    zeleni = state[2]

    dvizenja = {'left': (-1, 0), 'right': (1, 0), 'down': (0, -1), 'up': (0, 1)}
    nova_glava_coord = (snake[-1][0] + dvizenja[snake_dir][0],snake[-1][1]+dvizenja[snake_dir][1])

    if nova_glava_coord in zeleni:
        nova_zmija = list(snake)
        nova_zmija.append(nova_glava_coord)
        novi_zeleni = [z for z in zeleni if z != nova_glava_coord]
        novi_zeleni = tuple(novi_zeleni)
        nova_zmija = tuple(nova_zmija)
        nov_state=(nova_zmija,snake_dir,novi_zeleni)
        return nov_state
    else:
        nova_zmija = list(snake)
        nova_zmija.append(nova_glava_coord)
        nova_zmija.pop(0)
        nova_zmija = tuple(nova_zmija)
        nov_state = (nova_zmija, snake_dir, zeleni)
        return nov_state


def left(state):
    snake = state[0]
    snake_dir = state[1]
    zeleni = state[2]
    dvizenja = {'left': (0, -1), 'right': (0, 1), 'down': (1, 0), 'up': (-1, 0)}

    nova_glava_poz = {'left': 'down', 'right': 'up', 'down': 'right', 'up': 'left'}
    nova_glava_dir = nova_glava_poz[snake_dir]
    nova_glava = (snake[-1][0] + dvizenja[snake_dir][0], snake[-1][1] + dvizenja[snake_dir][1])

    if nova_glava in zeleni:
        nova_zmija = list(snake)
        nova_zmija.append(nova_glava)
        novi_zeleni = [jab for jab in zeleni if jab != nova_glava]
        novi_zeleni = tuple(novi_zeleni)
        nova_zmija = tuple(nova_zmija)
        nov_state = (nova_zmija, nova_glava_dir, novi_zeleni)
        return nov_state
    else:
        nova_zmija = list(snake)
        nova_zmija.append(nova_glava)
        nova_zmija.pop(0)
        nova_zmija = tuple(nova_zmija)
        nov_state = (nova_zmija, nova_glava_dir, zeleni)
        return nov_state

def right(state):
    snake = state[0]
    snake_dir = state[1]
    zeleni = state[2]
    dvizenja = {'left': (0, 1), 'right': (0, -1), 'down': (-1, 0), 'up': (1, 0)}
    nova_glava_poz = {'left': 'up', 'right': 'down', 'down': 'left', 'up': 'right'}

    nova_glava_dir = nova_glava_poz[snake_dir]
    nova_glava = (snake[-1][0] + dvizenja[snake_dir][0], snake[-1][1] + dvizenja[snake_dir][1])

    if nova_glava in zeleni:
        nova_zmija = list(snake)
        nova_zmija.append(nova_glava)
        novi_zeleni = [jab for jab in zeleni if jab != nova_glava]
        novi_zeleni = tuple(novi_zeleni)
        nova_zmija = tuple(nova_zmija)
        nov_state = (nova_zmija, nova_glava_dir, novi_zeleni)
        return nov_state
    else:
        nova_zmija = list(snake)
        nova_zmija.append(nova_glava)
        nova_zmija.pop(0)
        nova_zmija = tuple(nova_zmija)
        nov_state = (nova_zmija, nova_glava_dir, zeleni)
        return nov_state


def valid(snake, crveni):
    if len(snake) != len(set(snake)): return False
    for koord in snake:
        if koord in crveni: return False
    return 0 <= (snake[len(snake) - 1][0]) < 10 and 0 <= (snake[len(snake) - 1][1]) < 10


class Snake(Problem):
    def __init__(self, initial, crveni, goal=None):
        super().__init__(initial, goal)
        self.crveni = crveni

    def successor(self, state):
        successors = {}
        pravo_ = straight(state)
        levo_ = left(state)
        desno_ = right(state)
        if valid(pravo_[0], self.crveni):
            successors['ProdolzhiPravo'] = pravo_
        if valid(levo_[0], self.crveni):
            successors['SvrtiLevo'] = levo_
        if valid(desno_[0], self.crveni):
            successors['SvrtiDesno'] = desno_

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[-1]) == 0

if __name__ == '__main__':
    n = int(input())
    zeleni = []
    for i in range(n):
        coord = [int(num) for num in input().split(",")]
        zeleni.append(tuple(coord))
    m = int(input())
    crveni = []
    for i in range(m):
        coord = [int(num) for num in input().split(",")]
        crveni.append(tuple(coord))
    zmija = ((0, 9), (0, 8), (0, 7))
    state = (zmija, 'down', tuple(zeleni))
    s = Snake(state, crveni)
    solution = breadth_first_graph_search(s)
    if solution: print(solution.solution())
