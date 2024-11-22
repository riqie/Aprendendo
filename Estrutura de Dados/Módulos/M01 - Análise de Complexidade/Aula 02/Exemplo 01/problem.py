
import time

problemSize = 1000

print("\n%12s%15s" % ("Problem Size", "Iterations"))

for count in range(5):
    number = 0
    work = 1

    for j in range(problemSize):

        for k in range(problemSize):
            number += 1
            work +=1
            work -=1

    
    print("%12d%16.3f" % (problemSize, number))
    problemSize *= 2
print()
