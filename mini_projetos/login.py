# Cadastro de usuário e senha (simulados)
import getpass  # Biblioteca para ocultar a senha ao digitar

# Banco de dados de usuários (simulado)
usuarios = {
    "JOAO": "SENHA123",
    "MARIA": "SEGREDO",
    "PEDRO": "12345"
}

tentativas = 3  # Número máximo de tentativas

while tentativas > 0:
    us = input("Usuário: ").strip().upper()  # Remove espaços extras e converte para maiúsculas
    se = getpass.getpass("Senha: ").strip()  # Oculta a senha ao digitar

    if us in usuarios and usuarios[us] == se:  
        print("\n✅ Login bem-sucedido! Bem-vindo ao sistema.")
        break  # Sai do loop
    else:
        tentativas -= 1
        print(f"\n❌ Usuário ou senha incorretos. Tentativas restantes: {tentativas}")

    if tentativas == 0:
        print("\n🚨 Conta bloqueada. Muitas tentativas erradas.")
