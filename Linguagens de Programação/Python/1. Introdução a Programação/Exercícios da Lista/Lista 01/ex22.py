'''
Calcule e mostre o imposto de renda de um grupo de contribuintes considerando que
os dados de cada contribuinte (número do CPF, número de dependentes e renda
mensal) são valores fornecidos pelo usuário. Para cada contribuinte será feito um
desconto no imposto de 5% do salário mínimo (R$136,00) para cada dependente (o
salário mínimo e o desconto são designados por constantes simbólicas). Os valores
da alíquota para cálculo do imposto são:

Renda Líquida (R$) Alíquota
até 900,00 isento
900,01 até 1500,00 5%
1500,01 até 1900,00 10%
1900,01 até 2200,00 15%
acima de 2200,01 20%

O último valor, que não será considerado, terá o número do CPF igual a zero. Ao final,
devem ser impressos:

a. Para cada contribuinte, o total a pagar.
b. O número de contribuintes.
c. O total de contribuintes isentos e não isentos.
d. O total de impostos que serão arrecadados desse grupo de contribuintes.
e. O número do CPF e o valor da contribuição daquele contribuinte que for pagar
o maior imposto.
'''

SM = 900 #isento

'''
900,01 até 1500,00 5%
1500,01 até 1900,00 10%
1900,01 até 2200,00 15%
acima de 2200,01 20%
'''


def dadosContribuinte():
    registros = []
    a = 0
    
    while a <2 :
        cpf = input('Qual o CPF: ')
        n_dependentes = input('Quantos dependentes: ')
        renda_mensal = float(input('Qual a renda mensal: '))

        registros.append({
            'cpf': cpf,
            'Dependentes': n_dependentes,
            'Renda mensal': renda_mensal,    
        })
        
        a +=1
        
    return registros

abc = dadosContribuinte()
total = 0

for item in abc:
    total += item['renda']

print(total)
print(abc)
    
# def calculoImposto():
    
# exercicio incompleto
