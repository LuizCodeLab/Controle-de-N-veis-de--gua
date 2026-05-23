from colorama import Fore, Style

# Lista com os níveis do reservatório
niveis = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

# Função para definir cor
def definir_cor(nivel):
    if nivel == 0:
        return Fore.RED
    elif nivel == 1:
        return Fore.YELLOW
    elif nivel == 2:
        return Fore.GREEN
    elif nivel == 3:
        return Fore.CYAN
    elif nivel == 4:
        return Fore.ORANGE

# Mostra a lista de níveis
print("=== NÍVEIS DO RESERVATÓRIO ===\n")

for i in range(len(niveis)):
    print(f"Nível {i+1} - {niveis[i]}")

print("\n==============================\n")

# Usuário escolhe o nível atual
nivel_atual = int(input("Informe o nível atual do reservatório (1 a 5): "))

# Ajuste (usuário 1-5 → índice 0-4)
indice = nivel_atual - 1

# Verificação de segurança
if indice < 0 or indice > 4:
    print("Nível inválido!")
else:
    cor = definir_cor(indice)

    print("\n=== SITUAÇÃO ATUAL ===\n")
    print(cor + f"Nível {nivel_atual}: {niveis[indice]}")
    print(Style.RESET_ALL)

    print("\nSistema em monitoramento...")