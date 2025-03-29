# Lista inicial de frutas disponíveis com seus respectivos preços
frutas = {
    "banana":  2.99,
    "uva":     4.59,
    "morango": 5.00, 
    "laranja": 3.49,
    "abacate": 4.99
}

# Listas auxiliares para registrar pedidos e compras
pedidos_compra = []  # Lista para registrar frutas que não temos, mas o usuário deseja
carrinho = []  # Lista para armazenar frutas que o usuário quer comprar

# Loop principal do sistema de compras
while True:  # Utilizamos um loop infinito, pois o `break` controlará a saída
    # Solicita ao usuário que digite o nome da fruta e normaliza a entrada (remove espaços e converte para minúsculas)
    fruta_digitada = input("\nDigite uma fruta para procurar na lista: ").strip().lower()

    # Verifica se a fruta digitada está disponível na lista de frutas
    if fruta_digitada in frutas:
        print(f"✅ Temos {fruta_digitada.upper()} em nossa lista!")  # Exibe a fruta em maiúsculas para melhor visualização
        
        # Pergunta ao usuário se deseja adicionar a fruta ao carrinho
        ad_carrinho = input("Deseja adicionar ao carrinho? (S / N): ").strip().upper()
        if ad_carrinho == "S":  # Se o usuário escolher "S"
            # Adiciona a fruta e seu preço ao carrinho como uma tupla (fruta, preço)
            carrinho.append((fruta_digitada.upper(), frutas[fruta_digitada]))
            print(f"🛒 {fruta_digitada.upper()} adicionada ao carrinho!")

        # Pergunta ao usuário se deseja continuar as compras
        if input("Deseja continuar as compras? (S / N): ").strip().upper() != "S":
            break  # Se o usuário não escolher "S", o loop é encerrado

    else:
        # Caso a fruta não esteja na lista, informa o usuário
        print(f"❌ Não temos {fruta_digitada.upper()} em nossa lista.")
        
        # Pergunta ao usuário se deseja incluir a fruta na lista de compras futuras
        pedido = input("Deseja incluir na lista de compras? (S / N): ").strip().upper()
        if pedido == "S":  # Se o usuário escolher "S"
            pedidos_compra.append(fruta_digitada.upper())  # Adiciona a fruta à lista de compras futuras
            print(f"📝 {fruta_digitada.upper()} adicionada à lista de compras futuras!")

# Exibição do resumo final após o término das compras
print("\n===== RESUMO DAS COMPRAS =====")

# Exibe os itens adicionados ao carrinho
print(f"🛒 Seu carrinho:")
for fruta, preco in carrinho:  # Percorre a lista de compras e exibe os itens
    print(f"   - {fruta}: R$ {preco:.2f}")  # Exibe nome e preço formatado com 2 casas decimais
    
# Calcula o total da compra somando os preços das frutas no carrinho
total = sum(preco for _, preco in carrinho)
print(f"\n💰 Total da compra: R$ {total:.2f}")  # Exibe o total da compra com duas casas decimais
