from constraint import *

def max4(*vars):
    counter = dict()
    for t in vars:
        if counter.__contains__(t):counter[t] = counter[t]+1
        else: counter[t] =1

    return len([i for i in counter.values() if i > 4]) < 1

def all_in_one(*vars):
    if len(vars)<=4:
        termin = vars[0]
        for var in vars:
            if var !=termin:
                return False

    return True


if __name__ == '__main__':
    num = int(input()) # 3 ili 4
    papers = dict()
    paper_info = input()

    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()

    # Tuka definirajte gi promenlivite
    variables = [ f"{key} ({value})" for key,value in papers.items()]
    ai_variables = [ f"{key} ({value})" for key,value in papers.items() if value =="AI"]
    ml_variables = [ f"{key} ({value})" for key,value in papers.items() if value =="ML"]
    nlp_variables = [ f"{key} ({value})" for key,value in papers.items() if value =="NLP"]
    domain = [f'T{i + 1}' for i in range(num)]

    problem = Problem(BacktrackingSolver())
    problem.addVariables(variables, domain)

    # Tuka dodadete gi ogranichuvanjata
    problem.addConstraint(max4, variables)
    problem.addConstraint(all_in_one, ai_variables)
    problem.addConstraint(all_in_one, ml_variables)
    problem.addConstraint(all_in_one, nlp_variables)

    result = problem.getSolution()

    # Tuka dodadete go kodot za pechatenje
    for var in variables:
        print(f"{var}: {result[var]}")
