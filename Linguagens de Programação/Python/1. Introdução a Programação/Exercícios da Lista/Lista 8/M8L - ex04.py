'''
4. Implemente um programa com uma função para calcular o número de combinações 
possíveis de m elementos em grupos de n elementos (n ≤ m), dado pela fórmula de 
combinação: m!/(m-n)!n!
'''

def receber_elementos():
    print("\tNúmero de combinações possíveis de m elementos em grupos de n elementos")
    print(f"\t{71*'-'}")
    print()
    print("Informe m e n, em que (m >= n) e (n >= 0)\n")

    while True:
        try:
            m = int(input("m: "))
            n = int(input("n: "))
            if m >= n and n >= 0:
                return m, n
            else:
                print(30*"=")
                print("Condições: (m >= n) e (n >= 0)")
                print(30*"=")
        except ValueError:
            print(53*"-")
            print("m e n devem ser inteiros, em que (m >= n) e (n >= 0)!")
            print(53*"-")

def fatorial(x):
    f = 1
    for c in range(2,x+1):
        f = f * c
    
    return f

def combinacao(M, N):

    x = fatorial(M)
    y = fatorial(N)
    z = fatorial((M - N))
  
    formula_combinacao = x / (z * y)

    return formula_combinacao

def main():

    m, n = receber_elementos()

    resultado = combinacao(m, n)

    print(f"\nResultado = {resultado}")

main()



