"""
6. Escreva uma função recursiva que, dado um número inteiro positivo n, retorne a
representação binária de n; e outra função recursiva que, dado um número binário,
retorne a sua representação em decimal.
"""

def binario(n):
    if n == 0:
        return "0"
    #é possivel tirar esse if, só que o número fica com 1 bit a mais 
    if n == 1:  
        return "1"
    return str(binario(n // 2)) + str(n % 2)

#n[-3] = n[2], n[-2] = n[1], n[-1] = n[0]...
def decimal(n):    
    i = len(n) - 1
    if i == 0:
        return int(n[-i-1]) * 2**i
    if n[-i-1] == 0:
        return 0
    #n = '111', i = 2, a fatia percorre a string a partir de n[-2], que equivale a n[1], n[-i:] = '11'
    return int(n[-i-1]) * 2**i + decimal(n[-i:])

def main():
    print('\nO programa fará a conversão de decimal para binário e a conversão de binário para decimal:')

    dec = 7
    print('\nDecimal para binário:\nExemplo:', dec)
    print(binario(dec))

    bin = '111' # OBS: O número em binário deve ser lido como string para que seja fatiado e cada dígito seja convertido na função
    print('\nBinário para decimal:\nExemplo:', bin)
    print(decimal(bin))

    print('\nFim do programa')

main()

