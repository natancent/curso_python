# Passo 1: Criar um menu 
bebidas = {
    "Cerveja": 8.00,
    "Caipirinha": 15.00,
    "Refrigerante": 5.00

}

comidas = {
    "Croquete":23.00,
    "Steak":35.00,
    "Fish":40.00
}

outros_gastos = {
    "Estacionamento":5.00,
    "Entrada":50.00,
    "Guarda - Volumes ": 20.00
}

# Passo 2: Receber pedidos do cliente
pedidos = ["Cerveja", "Caipirinha", "Cerveja" , "Croquete", "Fish", "Estacionamento",
           "Entrada","Entrada","Guarda - Volumes","Guarda - Volumes"]  # Exemplo de pedidos

# Passo 3: Calcular o total da conta
total_bebidas = sum(bebidas[bebida] for bebida in pedidos if bebida in bebidas)
total_comidas = sum(comidas[comida] for comida in pedidos if comida in comidas)
total_outros = sum(outros_gastos[outros] for outros in pedidos if outros in outros_gastos) 
sub_total = total_bebidas + total_comidas
gorjeta = sub_total * 0.10 
total = sub_total + gorjeta

#Sub total
print(f"Subtotal: R${sub_total:.2f}")

#Gorjeta
print(f"Gorjeta(10%): R${gorjeta:.2f}")

#Total

print(f"Total: R${total:.2f} ")

#Próximos passos: 
# 1 Descriminar itens no recibo com respectivos preços






