def f1(a, b):
    c = a - b
    return (a + b + c)

def f2(a, b):
    c = f1(b, a)
    return(b + c - a)

def main():
    x = f2(2, 3)
    return print(x)

main()