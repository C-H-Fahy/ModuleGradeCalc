#Copyright 2021 Ciaran Fahy
#MIT License

def main(grades, maxgrades, weights):
    """Input; 3 lists with weight as multiplier, Returns; grades explained(str)"""
    try:
        if len(grades) != len(weights) or len(weights) != len(maxgrades):
            return("Len of grades and weights not equal")

        high = weightedgrade(maxgrades, weights);
        grade = weightedgrade(grades, weights);
        percentage = grade / high * 100

        return('Your Weighted Grade is ' + str(grade) + ' which is ' + str(percentage) + '%')

    except ZeroDivisionError:
        return('Zero Division')
    

def weightedgrade(grades, weights):
    """Input; 2 lists, Returns; weighted grade(int)"""
    
    weightedgrade = 0
    for i in range (0, len(grades)):
        weightedgrade = weightedgrade + grades[i] * weights[i]

    return(weightedgrade)

#a = main([16.7, 40.41, 58.65], [20, 50, 80], [0.1, 0.4, 0.5]);
#print(a)
