#Copyright 2021 Ciaran Fahy
#MIT License

def main(grades, maxgrades, weights):
    """Input; 3 lists with weight as multiplier, Returns; decimal(float) and weightedgrade(float)"""
    try:
        if len(grades) != len(weights) or len(weights) != len(maxgrades):
            return("Len of grades and weights not equal")

        high = weightgrade(maxgrades, weights);
        weightedgrade = weightgrade(grades, weights);
        decimal = weightedgrade / high
        return(decimal, weightedgrade)

    except ZeroDivisionError:
        print('Zero Division')
        return()
    except TypeError:
        print('Type Error')
        return()
    

def weightgrade(grades, weights):
    """Input; 2 lists, Returns; weighted grade(int)"""
    
    weightedgrade = 0
    for i in range (0, len(grades)):
        weightedgrade = weightedgrade + grades[i] * weights[i]

    return(weightedgrade)

#a = main([16.7, 40.41, 58.65], [20, 50, 80], [0.1, 0.4, 0.5]);
#print(a)
