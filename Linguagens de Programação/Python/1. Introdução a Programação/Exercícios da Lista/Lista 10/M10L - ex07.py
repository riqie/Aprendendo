'''
Escreva uma função recursiva que, dada uma string s e um caractere c, conte o 
número de ocorrências do caractere c na string s.
'''

def contador(s, c):
    if s == "": #Caso-base = string vazia
        return 0
    
    if s[0] == c: #Caso recursivo
        return 1 + contador(s[1:], c) #Manda o resto da string pra ser analisado. Por ex, no caso da string "banana", manda "anana", depois "nana", e assim por diante.
    
    return contador(s[1:], c)
    
def main():
    
    print("\tCONTADOR DE CARACTER NA STRING\n")
    string_entrada = "abacaxi"
    caractere = "a"

    resultado = contador(string_entrada.lower(), caractere.lower())
    
    print(f"Número de caracteres '{caractere.lower()}' na string '{string_entrada.lower()}': {resultado}")

main()
