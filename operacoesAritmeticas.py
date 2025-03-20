#numero1 = 10
#numero2 = 2
#
#
#
#
## 1️⃣ Crie um programa que peça dois números ao usuário e mostre a soma, subtração, multiplicação, divisão normal e divisão inteira entre eles.
#
##Adição
#print(int(numero1 + numero2))
#
##subtração
#print(int(numero1 - numero2))
#
##Multiplicação
#print(int(numero1 * numero2))
#
##Divisão
#print(int(numero1 / numero2))
#
##Mod
#print(int(numero1 % numero2))
#
##Resto
#print(int(numero1 // numero2))
#
##Exponenciação
#print(int(numero1 ** numero2))
#
## 2️⃣ Peça ao usuário um número e exiba o quadrado e o cubo desse número.
#num = input("Favor Digite um número:")
#num = int(num)
#
#quadrado = num ** 2
#cubo = num ** 3
#
#print(quadrado)
#print(cubo)
#
#
## 3️⃣ Solicite um número ao usuário e mostre se ele é par ou ímpar usando o operador de módulo (%).
#if num % 2 == 0:
#    print("Número par")
#else:
#    print("Número impar")
#
## 4️⃣ Peça ao usuário a quantidade de dias e converta para horas, minutos e segundos.
#dias = input("Digite a quantidade de dias a serem convertidos:")
#dias = int(dias)
#horas = dias * 24
#minutos = horas * 60
#segundos = minutos * 60
#
#print(f"{dias} dias equivalem á {horas} horas , {minutos} minutos e {segundos} segundos " )
#print(f"{dias} dias equivalem á {horas} horas , {minutos} minutos e {segundos} segundos " )

# 5️⃣ Faça um programa que receba o salário de uma pessoa e um percentual de aumento, 
#     depois calcule e mostre o novo salário dela.
#salario = input("Salário:")
#percent = input("Percentual de aumento (só número):")
#
#salario = float(salario)
#percent = float(percent)
#
#porcentagem = (salario * percent) / 100
#novo_salario = salario + porcentagem
#print(f"Seu novo salário com aumento de {percent:.0f}%, é de  R${novo_salario:.2f}")
#
#
###Desafio 6: Peça ao usuário um valor em Celsius e converta para Fahrenheit.
#celsius = input("Digite o valor em Celsius:")
#celsius = int(celsius)
#fahrenheit = (celsius * 9/5) + 32
#print(fahrenheit) 
#
##Desafio 7 : O usuário digita o valor da compra e o valor pago. O programa calcula o troco.
#valor_compra = float(input("favor digite o valor da compra: "))
#valor_pago = float(input("Favor,digite o valor pago: "))
#troco = valor_pago - valor_compra
#falta = troco * -1
#
#if troco > 0:
#    print(f"Seu troco é de R${troco:.2f}.") 
#elif troco == 0:
#    print("Você não tem troco.")
#else:
#    print(f"Dinheiro insuficiente, falta R${falta:.2f}! ")

#Desafio: O usuário digita o raio, e o programa calcula a área do círculo.
#raio = float(input("Favor digite a medida do raio:"))
#area = 3.14 * raio ** 2
#print(f"A área do circulo é {area:.1f}")

#Desafio: O usuário digita peso e altura, e o programa calcula o IMC.

peso = float(input("Digite seu peso: "))
altura = float( input("Digite a sua altura: "))
imc = peso / (altura * altura) 
print(f"Seu IMc é de {imc:.1f} ")