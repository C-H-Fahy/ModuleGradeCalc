import GradeCalc
def main():
    n = int(input("Enter Number of Assessements:\n"))
    grades = []
    maxgrades = []
    weights = []
    for i in range (0, n):
        grades.append(int(input("Enter Grade for Assessment " + str(n) + ":\n")))
        maxgrades.append(int(input("Enter MaxGrade for Assessment " + str(n) + ":\n")))
        weights.append(int(input("Enter Weight for Assessment " + str(n) + " as multiplier(eg. 0.1):\n")))
    return(GradeCalc.main(grades, maxgrades, weights))
print(main())
