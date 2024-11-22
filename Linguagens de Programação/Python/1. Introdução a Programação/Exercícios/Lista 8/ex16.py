# Faça um programa que calcule o imposto de renda de um contribuinte de um país imaginário 
# onde as regras do imposto são as seguintes:
# • Todos pagam a mesma alíquota, de 20%.
# • São descontados da base de cálculo (proventos) as despesas com educação e despesas 
# médicas.
# • São descontados R$ 1000,00 por dependente.
# • O imposto devido ou a receber pode ser parcelado em até 6 vezes.
# • Valores de imposto (devido ou a receber) abaixo de R$100,00 não são cobrados nem 
# pagos

def interface():
    print('='*60)
    print('O programa vai calcular o imposto de renda do contribuinte de um país.\n\nRegras do imposto:\n\n-> Todos pagam alíquota de 20%;\n\n-> São descontados da base de cálculo (proventos) as despesas com educação e despesas médicas;\n\n-> São descontados R$1000,00 por dependente;\n\n-> A dívida ou o Recibo podem ser parcelados em até 6x;\n   -> Abaixo de R$100,00 não são cobrados nem pagos.')
    print('='*60)


def impostoDeRenda(proventos, despesas, dependentes):
    imposto = proventos - despesas - (1000 *dependentes)

    if imposto < 0:
        imposto = 0

    aliquota = 0.20
    divida = imposto * aliquota
    
    if divida < 100:
        divida = 0

    return divida


def parcelar(divida):
    if divida == 0:
        return [0]
    
    parcelas = 6
    valor_parcela = divida / parcelas
    lista_parcelas = [valor_parcela] * parcelas

    return lista_parcelas


def resultado(divida, divida_parcelada):
    print('='*60)

    if divida == 0:
        print("Você não deve pagar imposto de renda.")
        return

    else:
        print(f"Imposto devido: R$ {divida:.2f}")

        if divida_parcelada:
            print("O imposto pode ser parcelado em até 6 vezes:")

    i = 1
    print('='*60)

    for parcela in divida_parcelada:
        print('Parcela', i, ': R$', format(parcela, '.2f'))
        i += 1



def variaveis():
    while True:
        try:
            print('='*60)
            proventos = float(input("Digite o valor dos proventos(salário): "))
            despesas_educacao = float(input("Digite o valor das despesas com educação: "))
            despesas_medicas = float(input("Digite o valor das despesas médicas: "))
            dependentes = int(input("Digite o número de dependentes: "))
            break

        except ValueError:
            print('='*60)
            print('Entre com valores válidos.')

    despesas = despesas_educacao + despesas_medicas
    
    return proventos, despesas, dependentes

def validarVariaveis(proventos, despesas, dependentes):
    if proventos < 0 or despesas < 0 or dependentes < 0:
        print('='*60)
        print("Valores negativos não são válidos.")
        return True
    
    else:
        return False


def main():
    interface()
    proventos, despesas, dependentes = variaveis()

    if validarVariaveis(proventos, despesas, dependentes):
        return
    
    divida = impostoDeRenda(proventos, despesas, dependentes)
    lista_parcelas = parcelar(divida)
    resultado(divida, lista_parcelas)


main()
print('fim do programa, gg')
