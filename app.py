# Importação da biblioteca colorama para utilizar as cores no terminal:
from colorama import Fore, Style

# Criação de uma lista para armazenar os níveis de água:
niveis = [
    "Muito Baixo (Crítico!)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito Alto (Alerta!)"
]

# Definindo uma cor para cada nível de água através de uma função:
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

# Definindo um nível para visualizar uma mensagem:
nivel_atual = 1

# Atribuindo a cor e a mensagem ao nível de água:
cor_exibida = definir_cor(nivel_atual)
mensagem = niveis[nivel_atual - 1]

#Exibirá a mensagem e retornará as cores ao padrão:
print(cor_exibida + mensagem + Style.RESET_ALL)