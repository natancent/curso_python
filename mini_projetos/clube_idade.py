nome = input("Digite seu nome: ").upper()
idade = int(input("Digite a sua idade: "))
vip = {"PEDRO","CICERO","MATHEUS","JACK"}


if nome in vip:
    print("Nome na lista VIP ,pode entrar")
elif idade < 18:
    print("Nome não consta na lista VIP  e é menor de idade ,não pode entrar")
else:
    print("Você é maior de idade, pode entrar.")
