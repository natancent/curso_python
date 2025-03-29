# Lista de produtos disponíveis
produtos = [
    "iphone 15", "iphone 15 plus", "iphone 15 pro", 
    "iphone 15 pro max", "iphone se", "iphone 16",
    "ipad", "ipad mini", "ipad air", "ipad pro",
    "macbook air", "macbook pro", "mac mini", "mac studio", 
    "mac pro", "apple watch series 9", "apple watch ultra 2", 
    "apple watch se", "apple watch series 10", "airpods",
    "airpods pro", "airpods max", "apple vision pro",
    "apple tv 4k", "homepod", "homepod mini"
]

# Adicionando um novo item à lista
produtos.append("Yamaha MT-07")  

# Removendo um item específico da lista
if "iphone 15" in produtos:
    produtos.remove("iphone 15")  

# Removendo item pelo índice
if len(produtos) > 5:
    produtos.pop(5)  

# Lista de preços
precos = [100, 2000, 5000, 150, 540, 800, 750, 110, 2, 10, 1000, 58]

# Modificando valores na lista de preços
precos[2] = 1500
precos[0] *= 1.5  # Aumentando o primeiro item em 50%

# Contando quantas vezes um item aparece na lista
nova_lista = ["camisas", "calças", "camisas", "bonés", "camisas"]
print(f"Camisas: {nova_lista.count('camisas')}, Bonés: {nova_lista.count('bonés')}")

# Ordenação de listas
produtos.sort()  # Ordena a lista de produtos em ordem alfabética
precos.sort(reverse=True)  # Ordena a lista de preços do maior para o menor

# Exibindo resultados
print("\nLista de Produtos Ordenada:", produtos)
print("\nLista de Preços Ordenada:", precos)
