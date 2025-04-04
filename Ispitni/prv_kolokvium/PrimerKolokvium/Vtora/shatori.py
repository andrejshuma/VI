from constraint import *

def same_position_constraint(*tents):
    for tent in tents:
        if tent in trees:
            return False
    return True

def tent_constraint(*tents):
    for tent1 in tents:
        for tent2 in tents:
            if tent1 == tent2:
                continue
            if abs(tent1[0] - tent2[0]) <= 1 and abs(tent1[1] - tent2[1]) <= 1:
                return False
    return True

def column_constraint(*tents):
    counter =[0 for _ in range(size)]

    for i in range(size):
        for tent in tents:
            if tent[0] == i:
                counter[i] = counter[i]+1

    for index,count in enumerate(count_columns):
        if count != counter[index]:
            return False
    return True



if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    size = 6
    # ----------------------------------------------------
    # ---Prochitajte gi informaciite od vlezot
    num_trees = int(input())
    trees=[]

    for i in range(num_trees):
        trees.append(tuple([int(t) for t in input().split(" ")]))

    trees = tuple(trees)

    count_columns = [int(num) for num in input().split(" ")]


    # -----------------------------------------------------
    # ---Izberete promenlivi i domeni so koi bi sakale da rabotite-----

    variables = []

    for index,tree in enumerate(trees):
        tent_domain = []
        for i in [-1,1]:
            new_x = tree[0] + i
            new_y = tree[1] + i

            # if 0 <= new_x < size and 0 <= new_y < size:   za dijagonalni
            #     tent_domain.append((new_x, new_y))
            if 0 <= new_x < size:
                tent_domain.append((new_x,tree[1]))
            if 0 <= new_y < size:
                tent_domain.append((tree[0],new_y))

        variable = f"tree{index}"
        variables.append(variable)
        problem.addVariable(variable,tent_domain)

    # -----------------------------------------------------
    # ---Potoa dodadete ogranichuvanjata-------------------

    problem.addConstraint(AllDifferentConstraint(), variables)
    problem.addConstraint(same_position_constraint, variables)
    #problem.addConstraint(tent_constraint, variables) #prva varijanta
    problem.addConstraint(column_constraint, variables) #vtora varijanta

    # -----------------------------------------------------

    # ---Potoa pobarajte reshenie--------------------------
    solution = problem.getSolution()
    if solution is None:
        print("No solution found.")
        exit()
    # -----------------------------------------------------

    # ---Na kraj otpechatete gi poziciite na shatorite-----
    for i in range(num_trees):
        x,y = solution[f"tree{i}"]
        print(f"{x} {y}")

