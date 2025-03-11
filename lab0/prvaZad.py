import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"

class Student:
    def __init__(self,name,surname,index,subject,theory,practice,lab):
        self.name = name
        self.surname= surname
        self.index=index
        self.theory = theory
        self.practice= practice
        self.lab=lab
        self.subject=subject
        self.total_points = int(theory) + int(practice) + int(lab)


def calculate_grade(points):
    if points >= 90:
        return 10
    elif points >80:
        return 9
    elif points >70:
        return 8
    elif points >60:
        return 7
    return 6


if __name__ == "__main__":
    students = {}

    while True:
        line = input().strip()
        if line == "end":
            break

        name, surname, index, subject, theory, practice, lab = line.split(",")

        student = Student(name, surname, index, subject, theory, practice, lab)

        if index not in students:
            students[index] = {"name": name, "surname": surname, "subjects": {}}

        students[index]["subjects"][subject] = calculate_grade(student.total_points)

    for index, info in students.items():
        print(f"Student: {info['name']} {info['surname']}")
        for subject, grade in info["subjects"].items():
            print(f"----{subject}: {grade}")
        print()


