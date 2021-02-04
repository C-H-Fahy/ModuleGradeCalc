import GradeCalc
def main():
    try:
        n = int(input("Enter Number of Assessements:\n"))
        grades = []
        maxgrades = []
        weights = []
        for i in range (0, n):
            grades.append(float(input("Enter Marks for Assessment " + str(i+1) + ":\n")))
            maxgrades.append(float(input("Enter Maximum Marks for Assessment " + str(i+1) + ":\n")))
            weights.append(float(input("Enter Weight for Assessment " + str(i+1) + 
            " as multiplier(eg. 0.1 for 10%):\n")))

        decimal, weightedgrade = GradeCalc.main(grades, maxgrades, weights)
        print('Your Weighted Grade is ' + str(weightedgrade) + ' which is ' + str(decimal*100) + '%')
        return(decimal, weightedgrade)
        
    except TypeError:
        print('invalid input')
        return()
main()
