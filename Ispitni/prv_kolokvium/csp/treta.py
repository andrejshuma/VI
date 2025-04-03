from constraint import *
def constraint(*vars):
    marija = vars[0]
    petar = vars[2]
    sostanok = vars[3]

    marija_free_time = [14,15,18]
    simona_free_time = [13,14,16,19]
    petar_free_time = [12,13,16,17,18,19]

    if sostanok not in simona_free_time:
        return False

    if sostanok not in marija_free_time and marija == 1:
        return False

    if sostanok not in petar_free_time and petar==1:
        return False

    if petar==1 and marija ==1: return False;
    if petar==0 and marija ==0: return False;

    return True



if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Marija_prisustvo",[0,1] )
    problem.addVariable("Simona_prisustvo", [1])
    problem.addVariable("Petar_prisustvo", [0,1])
    problem.addVariable("vreme_sostanok", [13,14,16,19])
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(constraint, ("Marija_prisustvo", "Simona_prisustvo", "Petar_prisustvo", "vreme_sostanok"))
    # ----------------------------------------------------

    [print(solution) for solution in problem.getSolutions()]