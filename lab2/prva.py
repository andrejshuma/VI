from gogoClone.searching_framework import Problem, astar_search


class Table(Problem):
    def __init__(self, initial, allowed, size, goal=None):
        super().__init__(initial, goal)
        self.allowed = allowed
        self.size = size
        self.columns, self.rows = size  # 5,9

    def successor(self, state):
        successors = {}
        player = state[0]
        home_pos = state[1]
        home_dir = state[2]

        ways_to_go = [(0, 0), (0, 1), (0, 2), (-1, 1),
                      (-2, 2), (1, 1), (2, 2)]
        dirs_to_go = ["Stoj", "Gore 1", "Gore 2",
                      "Gore-levo 1", "Gore-levo 2",
                      "Gore-desno 1", "Gore-desno 2"]

        new_home_pos, new_home_dir = self.move_home((home_pos, home_dir))

        for way, dir in zip(ways_to_go, dirs_to_go):
            new_player_x = player[0] + way[0]
            new_player_y = player[1] + way[1]

            if self.in_bounds(new_player_x,new_player_y):
                new_player = (new_player_x, new_player_y)

                if new_player in self.allowed or new_player == new_home_pos:
                    new_state = (new_player, new_home_pos, new_home_dir)
                    successors[dir] = new_state

        return successors

    def in_bounds(self,a,b):
        return 0 <= a < self.columns and 0 <= b < self.rows

    def move_home(self, home):
        home_pos, home_dir = home
        home_x, home_y = home_pos

        if home_dir == "r":
            if home_x == self.columns - 1:
                new_dir = "l"
                home_x -= 1
                return (home_x, home_y), new_dir
            else:
                home_x += 1
                return (home_x, home_y), home_dir
        else:
            if home_x == 0:
                new_dir = "r"
                home_x += 1
                return (home_x, home_y), new_dir
            else:
                home_x -= 1
                return (home_x, home_y), home_dir

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] == state[1]

    def h(self, node):
        x, y = node.state[0]
        house_x, house_y = node.state[1]
        return (abs(x - house_x)+abs(y - house_y)) / 5


if __name__ == '__main__':
    allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4), (2, 4),
               (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]

    size = (5, 9)  # 5 columns, 9 rows
    person_coord = tuple(int(i) for i in input().split(","))
    house_coord = tuple(int(i) for i in input().split(","))
    house_dir = "r" if input() == "desno" else "l"

    initial_state = (person_coord, house_coord, house_dir)
    tabla = Table(initial_state, allowed, size)

    solution = astar_search(tabla)
    if solution:
        print(solution.solution())
    else:
        print([])