'''
 Um armazém trabalha com um determinado número de mercadorias diferentes (um
máximo de 100 itens). Faça um programa que leia e armazene em vetores os preços
de cada mercadoria e a quantidade vendida no mês e, além disso, calcule e imprima:
a. O faturamento mensal do armazém.
b. A mercadoria mais vendida e a menos vendida.
c. O preço da mercadoria menos vendida.
2
d. Quantas mercadorias têm seu preço mais alto que o preço da mercadoria
menos vendida.
'''

print("-"*80)
print("Status do armazém")
print("-"*80)

produtos = []
print("Atualmente o armazém conta com as suigntes mercadorias: ")
print(produtos)
q1 = str(input("Deseja adicionar alguma mercadoria? \n S ou N \n"))

while q1 != "S" and q1 != "s" and q1 != "N" and q1 != "n":
    print("Resposta inválida.")
    print("Tente novamente")
    q1 = str(input("Deseja adicionar alguma mercadoria? \n S ou N \n"))

if q1 == "S" or q1 == "s":
    q2 = int(input("Quantas mercadorias deseja adicionar? \n"))
    while q2 <= 0 or q2 > 100:
        print("Quantidade inválida para o seu estoque.")
        q2 = int(input("Quantas mercadorias deseja adicionar? \n"))
elif q1 =="N" or q1 == "n":
    print("Ok.")
    print("Seu estoque se encontra assim:")
    print(produtos)

p1 = 1
faturamentos = []
quantidade_vendas = []
nomes = []
precos = []


while q2 > 0:
    nome = str(input(f"Qual o nome do {p1}º produto? "))
    nomes.append(nome)
    #adiciona o nome dos produtos na lista de nomes

    #preço de compra do produto
    compra = float(input(f"Qual o valor de compra do {p1}º produto? "))
    while compra <= 0:
        print("Valor incorreto, tente novamente.")
        compra = float(input(f"Qual o valor de compra do {p1}º produto? "))

    #quantidade de produtos comprados
    quantidade1 = int(input(f"Quantas unidades do {p1}º produto foram compradas? "))
    while quantidade1 <= 0:
        print("Valor incorreto, tente novamente.")
        quantidade1 = int(input(f"Quantas unidades do {p1}º produto foram compradas? "))
    
    #preço de venda do produto
    venda = float(input(f"Qual o valor de venda do {p1}º produto? "))
    while venda <= 0:
        print("Valor incorreto, tente novamente.")
        venda = float(input(f"Qual o valor de venda do {p1}º produto? "))
    precos.append(venda)

    #quantidade de produtos vendidos
    quantidade2 = int(input(f"Quantas unidades do {p1}º produto foram vendidas? "))
    while quantidade2 > quantidade1:
        print("Valores incorretos, tente novamente.")
        quantidade2 = int(input(f"Quantas unidades do {p1}º produto foram vendidas? "))
    quantidade_vendas.append(quantidade2)
    #adiciona a quantidade de produtos que foram vendidos na lista

    faturamento = (venda*quantidade2) - (compra*quantidade1)
    faturamentos.append(faturamento)
    print(f"O faturamento relacionado a este produto é {faturamento}")
    #calculo e impressão do faturamento

    q2 = q2 - 1
    p1 = p1 + 1

print("-"*80)
print("Informações gerais")
print("-"*80)

totalfaturado = sum(faturamentos)
print(f"O balanço mensal do armazém fechou com o valor de {totalfaturado}")

print("-"*80)

produto1 = quantidade_vendas.index(max(quantidade_vendas))
popular = nomes[produto1]
produto2 = quantidade_vendas.index(min(quantidade_vendas))
inpopular = nomes[produto2]

print("O produto mais vendido do seu armazém foi o", popular, "com", max(quantidade_vendas), "unidades")
print("Porém...")
print("O produto menos vendido do seu armazém foi o", inpopular, "com", min(quantidade_vendas), "unidades")

print("-"*80)

preco_inpopular = precos[produto2]

print("A mercadoria menos vendida é", nomes[produto2], "que tem o preço de", preco_inpopular)

print("-"*80)

lista = []
for i in precos:
    if i < preco_inpopular:
        lista.append(i)

quantidade3 = len(lista)

print("Existem", quantidade3, "itens com um preço maior que o do produto menos vendido")
print("Fim da analise")
print("-"*80)
