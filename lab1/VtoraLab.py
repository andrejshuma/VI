from imports.util import *
from imports.uninformed_search import *


def danger(ball, players):
    for p in players:
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if ball[0] == p[0] + i and ball[1] == p[1] + j: return True


def validna(state,prepreki):
    if state[0] in prepreki or state[1] in prepreki: return  False
    if danger(state[1],prepreki): return False
    return 0<=state[0][0]<8 and 0<=state[0][1]<6 and 0<=state[1][0]<8 and 0<=state[1][1]<6

class Football(Problem):
    def __init__(self,initial,prepreki,gol,goal=None):
        super().__init__(initial,goal)
        self.gol = gol
        self.prepreki = prepreki

    def successor(self, state):
        successors = {}

        pos_player = state[0]
        pos_ball = state[1]
        moves = [(0,1),(0,-1),(1,0),(1,1),(1,-1)]
        move_names= ["gore","dolu","desno","gore-desno","dolu-desno"]

        l = len(moves)

        for move in range(l):
            next_to_ball = False
            new_pos_player = (pos_player[0] + moves[move][0], pos_player[1] + moves[move][1])
            if new_pos_player == pos_ball:
                next_to_ball = True
                new_pos_ball = (pos_ball[0] + moves[move][0], pos_ball[1] + moves[move][1])
                new_state = (new_pos_player,new_pos_ball)
            else: new_state = (new_pos_player,pos_ball)

            if validna(new_state,self.prepreki):
                text = "Turni topka " if next_to_ball else "Pomesti coveche "
                text+=move_names[move]
                successors[text] = new_state



        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[1] in self.gol



if __name__ == '__main__':
    player = [int(n) for n in input().split(",")]
    ball = [int(n) for n in input().split(",")]
    player= tuple(player)
    ball= tuple(ball)
    prepreki = ((3, 3), (5, 4))
    gol = ((7, 2), (7, 3))
    state = (player,ball)
    f = Football(state,prepreki,gol)
    solution = breadth_first_graph_search(f)
    if solution: print(solution.solution())
    else: print("No Solution!")