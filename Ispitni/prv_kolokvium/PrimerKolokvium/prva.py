from searching_framework import *

class Boxes(Problem):
    def __init__(self, initial,n,old_boxes, goal=None):
        super().__init__(initial, goal)
        self.size= n
        self.old_boxes = old_boxes

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[2] == 0

    def check_valid(self, player, boxes):
        x, y = player
        return 0 <= x < self.size and 0 <= y < self.size and (x, y) not in boxes

    def successor(self, state):
        successors = {}
        player_pos = state[0]
        boxes = list(state[1])
        counter = state[2]

        moves = ["Gore", "Desno"]
        moves_coords = [(0, 1), (1, 0)]
        okolni = [(+1, 0), (-1, 0), (0, +1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]

        for move, coord in zip(moves, moves_coords):
            new_player_pos = (player_pos[0] + coord[0], player_pos[1] + coord[1])

            if self.check_valid(new_player_pos, self.old_boxes):
                new_boxes = list(boxes)
                new_counter = counter

                if new_counter > 0:
                    for box in boxes:
                        if any((new_player_pos[0] + s[0], new_player_pos[1] + s[1]) == box for s in okolni):
                            new_boxes.remove(box)
                            new_counter -= 1

                new_state = (new_player_pos, tuple(new_boxes), new_counter)
                successors[move] = new_state

        return successors


if __name__ == '__main__':
    n = int(input())
    man_pos = (0, 0)

    num_boxes = int(input())
    boxes = list()
    for _ in range(num_boxes):
        boxes.append(tuple(map(int, input().split(','))))

    initial = (man_pos, tuple(boxes), num_boxes)
    b = Boxes(initial,n,boxes)
    solution = breadth_first_graph_search(b)
    if solution: print(solution.solution())
    else: print("No Solution!")