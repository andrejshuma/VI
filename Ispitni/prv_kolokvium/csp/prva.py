from constraint import *
#       SEND
#      +MORE
#      --------
#      MONEY


def sumvariables(*vars):
    #["S0", "E1", "N2", "D3", "M4", "O"5, "R6", "Y7"]
    x = vars[0]*1000 + vars[1]*100 + vars[2]*10 + vars[3]
    y = vars[4]*1000 + vars[5]*100 + vars[6]*10 + vars[1]
    res = vars[4]*10000+vars[5]*1000 + vars[2]*100 + vars[1]*10 + vars[7]
    return x+y==res


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["S", "E", "N", "D", "M", "O", "R", "Y"]
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(10))))

    problem.addConstraint(AllDifferentConstraint(),variables)
    problem.addConstraint(sumvariables,variables)

    print(problem.getSolution())