#uso da função format, usada para formatar strings, permitindo que você insira valores de variáveis em uma string de forma controlada e personalizada. Essa função é poderosa e flexível, oferecendo muitas opções para formatar a saída da string.

# formatando inteiros:
print(format(10,"d"))
print(format(13, "+d"))
print(format(-7, "+d"))

#formatando reais:
print(format(3.141459265359, "f"))
print(format(3.141459265359, "+f"))
print(format(3.141459265359, "+.10f"))

#mais uma forma de formatação:

#string:
fruits = 'fruits:{0}, {1}, e {2}'
print(fruits.format("pineapple", "banana", "khaki"))
pets = "who is smarter: {1} or {0}?"
print(pets.format("cat", "dog"))

#inteiros:
sum = "{0} + {1} = {2}"
print(sum.format(3,4,3 + 4))
values = "min/avg/max value: {0}/{1}/{2}"
print(values.format(10,35,100))

#reais:
pi ="o valor de pi é: {0:.4f}"
print(pi.format(3.14149265359))
grades = "the average grade for the class was {0:.2f} ."
print(grades.format(8.7525))

#formatação com dados diferentes:
header = "{0}, {2}, {1}, {3}"
print(header.format("jacareí", 1, "april", 2024))
temperature = "{1:02d}/{0:02d}/{2}:{3:.1f}C"
print(temperature.format(1,4,2024,28.765))

