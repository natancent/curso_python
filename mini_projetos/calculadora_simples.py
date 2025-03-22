# Inicializa a variável de controle do loop
roda = True  

# Início do loop while, que continuará rodando enquanto 'roda' for True
while roda == True:  
    # Solicita ao usuário um número e converte para float
    numero = float(input("Digite um número: "))  
    
    # Solicita ao usuário a operação matemática desejada
    operacao = input("Escolha operação (+ , - , * , / , // , %): ")  
    
    # Solicita um segundo número e converte para float
    numero2 = float(input("Digite outro número:" ))  

    # Verifica qual operação foi escolhida e aplica a operação ao 'numero'
    if operacao == ("+"):
        numero += numero2  # Adição
    if operacao == ("-"):
        numero -= numero2  # Subtração
    if operacao == ("*"):
        numero *= numero2  # Multiplicação
    if operacao == ("/"):
        numero /= numero2  # Divisão
    if operacao == ("//"):
        numero //= numero2  # Divisão inteira (sem casas decimais)
    if operacao == ("%"):
        numero %= numero2  # Módulo (resto da divisão)

    # Exib
