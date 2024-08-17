# os comandos conddicionais farão com que o programa só realize sua função caso seja verdadeiro. Agora iremos a prender o comando: if.
a = int(input("valor de a: "))


if a <= 50:
    print("o valor de a está abaixo de 50!")
else:
    print("o valor de a está acima de 50!")


# verificar se o número é par ou ímpar.
print()
b=int(input("Digite um número: "))
print("Verificar se o número épar ou ímpar:")


if b % 2 == 1:
    print("O número é ímpar (Odd number).")
else:
    print("O número é par (Even number).")

print("end of program.")
