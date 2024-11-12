'''
Uma companhia aérea mantém uma lista de voos previstos, identificados pelo 
número de voo e outra para a quantidade de lugares ainda disponíveis em cada voo. 
Cada avião leva um total de até 345 passageiros. Faça um programa que:
a. Inicialize a lista de voos para os valores 727, 442, 331, 447, 221, 291, inicialize a 
lista de lugares disponíveis para o valor máximo,
b. Mostre um menu com as seguintes opções: listar voos previstos, fazer 
reserva, cancelar reserva e sair do programa. 
c. Faça reservas, indicando se ainda existem lugares disponíveis no voo citado. 
Se houver, o programa deve perguntar se o usuário quer confirmar a reserva. 
Se quiser, o número de lugares disponíveis para aquele voo deve ser 
decrementado.
d. Desfaça reservas, incrementado o número de lugares disponíveis no voo
correspondente.
'''

print('\n','='*30)
print(' Seja Bem-Vindo ao FlyCode, o que deseja?')

lista_voos = ['727°', '442°', '331°', '447°', '221°', '291°']
lugares = []
reservas = 0

for voo in lista_voos:
    lugares.append(345)

for i in range(len(lista_voos)):
    voo = lista_voos[i]

while True:
    print('\n','='*30)
    print('\n A) Listar voos. \n B) Reservar voos. \n C) Cancelar reserva. \n D) Sair.')
    opcao = input('\n Selecione uma opção: ')

    if opcao.upper() == 'A':
        print('\n','='*30)
        print('\n Listagem de voos selecionado.')
        print('\n','='*30)

        for i in lista_voos:
            print(f" Voo: {i} | Lugares disponíveis: {lugares[lista_voos.index(i)]}")

        print('\n','='*30)
        print('\n O que deseja agora?')

    elif opcao.upper() == 'B':
        print('\n','='*30)
        aviao = input('\n Qual voo deseja selecionar? ')
        
        if (f'{aviao}°') in lista_voos:
            print('\n','='*30)
            print(f'\n Avião {aviao}° selecionado.')
            print(f' Lugares disponíveis para reserva: {lugares[lista_voos.index(f'{aviao}°')]}')
            print('\n','='*30)
        
            quantidade_lugares = int(input('\n Quantos lugares deseja? '))
            print('\n','='*30)

            if quantidade_lugares > lugares[lista_voos.index(f'{aviao}°')] or quantidade_lugares < 0:
                print('\n','='*30)
                print('\n Não é possivel reservar esta quantidade.\n Tente novamente.')

                continue

            else:
                lugares[lista_voos.index(f'{aviao}°')] -= quantidade_lugares
                print(f'\n {quantidade_lugares} lugares reservados.')
                print(f' {lugares[lista_voos.index(f'{aviao}°')]} lugares restantes.')
                reservas += 1
                print('\n O que deseja agora?')
                
        else: 
            print('\n','='*30)
            print('\n Este voo não existe, tente novamente.')

            continue

            
    elif opcao.upper() == 'C':
        print('\n','='*30)

        if reservas <= 0:
            print('\n Você não possui reservas feitas, tente novamente.')

            continue

        cancelar_voo = input('\n Deseja cancelar as reservas de qual voo? ')
        print('\n','='*30)

        if (f'{cancelar_voo}°') in lista_voos:
            print(f'\n Avião {cancelar_voo}° selecionado.')
            print(f' Lugares disponíveis para cancelar: {lugares[lista_voos.index(f'{cancelar_voo}°')]}')
            print('\n','='*30)
            cancelar_lugares = int(input('\n Deseja cancelar quantos lugares? '))

            if cancelar_lugares > lugares[lista_voos.index(f'{cancelar_voo}°')]:
                print('\n','='*30)
                print(' Você não reservou tantos lugares.')
                
                continue
            
            else:
                print('\n','='*30)
                lugares[lista_voos.index(f'{cancelar_voo}°')] += cancelar_lugares
                reservas -= 1
                print(' Reservas canceladas')
                print('\n O que deseja agora?')
                print('\n','='*30)

    
    elif opcao.upper() == 'D':
        print('\n','='*30)
        print('\n Deseja sair do programa?')
        print('\n','='*30)
        sair = input('\n S/N:')

        if sair.upper() == 'N':
            print('\n','='*30)
            print('\n A) Listar voos. \n B) Reservar voos. \n C) Cancelar reserva. \n D) Sair.')
            opcao = input('\n Muito bem, o que deseja agora?')

        else:
            print('\n','='*30)
            print('\n Saindo.')
            break
    
    



    

























  









