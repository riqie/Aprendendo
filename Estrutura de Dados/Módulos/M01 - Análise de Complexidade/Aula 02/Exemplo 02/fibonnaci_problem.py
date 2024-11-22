
counter = 0 

def fib(n):
    global counter
    counter += 1

    if n < 3:
        return 1
    else:
        return fib(n -1) + fib(n - 2)
    

problemSize = 2
print("\n%12s%15s" % ("Problem Size", "Calls"))


for count in range(5):
    fib(problemSize)
    print("%12s%15s" % (problemSize, counter))
    problemSize *= 2

print()
