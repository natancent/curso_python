renda = float(input("Qual é a renda mensal?: "))
divida = False
fiador = True

if renda > 3000 and not divida:
    print("Empréstimo aprovado.")
elif 2000 <= renda <= 3000 and not divida and fiador:
    print("Empréstimo aprovado com fiador.")
else:
    print("Empréstimo não aprovado.")


