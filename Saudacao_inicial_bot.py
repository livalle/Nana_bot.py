# Saudação inicial do bot
print("Olá! Bem-vindo(a)")

while True:
    print("Você já possui uma conta? (sim/não)")
    resposta_usuario = input("").strip().lower()

    if resposta_usuario == "sim":
        print("Aguarde, inicializando...")
        break
    elif resposta_usuario == "não":
        print("Por favor, registre-se.")
        # Aqui você pode adicionar lógica de registro, se necessário.
        # Por enquanto, vamos considerar que o usuário se registra e depois reinicia o loop.
    else:
        print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")

# Captura e valida a idade do usuário
while True:
    age_input = input("Digite sua idade: ")
    if age_input.isdigit():
        age = int(age_input)
        break
    else:
        print("Por favor, insira um número válido para a idade.")

# Captura e valida o nome do usuário
while True:
    nome = input("Digite seu nome: ")
    if nome.isalpha():
        break
    else:
        print("Por favor, insira um nome válido sem números ou caracteres especiais.")

# Saudação personalizada
print(f"Olá {nome}, bem-vindo ao seu assistente virtual Nana.")
print(f"Você tem: {age} anos.")

# Verificação condicional
if not nome.strip():
    print("Oh não... parece que houve um erro.")
    print("Por favor insira novamente.")
else:
    print("Aguarde um instante...")
    # Simulando algum processo
    print("Reconectando...")
