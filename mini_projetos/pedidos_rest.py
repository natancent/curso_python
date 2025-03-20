# 📌 Passo 1: Criar um menu de produtos com preços (Dicionários)
bebidas = {
    "Cerveja": 8.00,
    "Caipirinha": 15.00,
    "Refrigerante": 5.00
}

comidas = {
    "Croquete": 23.00,
    "Steak": 35.00,
    "Fish": 40.00
}

outros_gastos = {
    "Estacionamento": 5.00,
    "Entrada": 50.00,
    "Guarda - Volumes": 20.00
}

# 📌 Passo 2: Lista de pedidos feita pelo cliente
pedidos = [
    "Cerveja", "Caipirinha", "Cerveja", "Croquete", "Fish", 
    "Estacionamento", "Entrada", "Entrada", "Guarda - Volumes", "Guarda - Volumes"
]

# 📌 Passo 3: Cálculo do total de cada categoria

# ✅ Soma os preços das bebidas pedidas, verificando se existem no dicionário
total_bebidas = sum(bebidas[bebida] for bebida in pedidos if bebida in bebidas)

# ✅ Soma os preços das comidas pedidas, verificando se existem no dicionário
total_comidas = sum(comidas[comida] for comida in pedidos if comida in comidas)

# ✅ Soma os preços de outros gastos, verificando se existem no dicionário
total_outros = sum(outros_gastos[outros] for outros in pedidos if outros in outros_gastos) 

# ✅ Calcula o subtotal (antes da gorjeta)
sub_total = total_bebidas + total_comidas + total_outros

# ✅ Calcula a gorjeta (10% do subtotal)
gorjeta = sub_total * 0.10 

# ✅ Calcula o total final (subtotal + gorjeta)
total = sub_total + gorjeta

# 📌 Passo 4: Exibir os valores finais para o cliente
print(f"Subtotal: R${sub_total:.2f}")  # Mostra o valor sem gorjeta
print(f"Gorjeta (10%): R${gorjeta:.2f}")  # Mostra o valor da gorjeta
print(f"💰 Total a pagar: R${total:.2f}")  # Mostra o valor total com gorjeta

# 🚀 Próximos passos:
# 1️⃣ Mostrar cada item consumido com seu preço unitário e total por item
# 2️⃣ Organizar a saída para exibição mais clara e profissional (estilo recibo)
# 3️⃣ Permitir entrada dinâmica dos pedidos (exemplo: input do usuário)
