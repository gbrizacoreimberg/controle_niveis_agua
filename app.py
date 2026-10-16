
from colorama import Fore, Style, init

# Inicializa a biblioteca Colorama
init(autoreset=False)

# Lista com os níveis do reservatório
niveis_agua = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
]

# Função que define a cor conforme o nível
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# Exibe os alertas do reservatório
for indice in range(len(niveis_agua)):
    nivel = indice + 1
    cor = definir_cor(nivel)

    print(cor + niveis_agua[indice] + Style.RESET_ALL)
    