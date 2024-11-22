
import time

problemSize = 5000

print("\n%12s%16s" % ("Problem Size", "Seconds"))

for count in range(5):
    start = time.time()
    work = 1

    for j in range(problemSize):

        for k in range(problemSize):
            work +=1
            work -=1

    elapsed = time.time() - start

    print("%12d%16.3f" % (problemSize, elapsed))
    problemSize *= 2
print()
