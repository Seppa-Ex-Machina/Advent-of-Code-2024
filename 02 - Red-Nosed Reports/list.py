import math

result = 0
report = []
strikes = 0

def evaluate_report(report):
    sign = 0
    strikes = 0
    for i in range(len(report)-1): 
        diff = int(report[i]) - int(report[i+1])
        if( i == 0):
            sign = int(diff / abs(diff)) if diff != 0 else 0
        if(abs(diff) > 3): # Too large
            strikes += 1
            return False, strikes
        if(math.copysign(1, diff) != sign):
            strikes += 1
            return False, strikes
        if(diff == 0):
            strikes += 1
            return False, strikes
    return True, strikes



with open("input\input01.txt", "r") as file:
    for line in file:
        sign = 0
        strikes = 0
        report = line.split()
        result += 1 # Assume that report is good
        # print(report)
        eval, strikes = evaluate_report(report)

        if(not eval):
            result -= 1
            if(strikes > 0):
                # print("Report is bad (Strikes)")
                # print(strikes)
                # print("Trying permutations")
                length = len(report)
                for i in range(length):
                    permuted_report = report[:i] + report[i+1:]
                    eval, _ = evaluate_report(permuted_report)
                    if(eval):
                        # print("Found a good permutation")
                        result += 1
                        # print(permuted_report)
                        break
                



print(result)

