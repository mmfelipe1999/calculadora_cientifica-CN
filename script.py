# ==================================
# CALCULADORA CIENTIFICA BABADEIRA
# ==================================
import re
import numpy as np
import matplotlib.pyplot as plt

def criar_grafico(nome_operacao, num_central, tipo_angulo=None):
    if nome_operacao == "fatorial":
        print("Gráfico contínuo não é suportado para fatorial.")
        return

    print(f"\n--- Gerando gráfico de {nome_operacao}... Aguarde. ---")
    
    # AJUSTE INTELIGENTE DA JANELA (ZOOM)
    if tipo_angulo == "graus":
        eixo_x = np.linspace(num_central - 360, num_central + 360, 200)
    elif nome_operacao in ["ln", "log"]:
        inicio = 0.1
        fim = num_central + 20 if num_central > 0 else 20
        eixo_x = np.linspace(inicio, fim, 100)
    elif nome_operacao == "potencia":
        eixo_x = np.linspace(num_central - 3, num_central + 3, 100)
    else:
        eixo_x = np.linspace(num_central - 10, num_central + 10, 100)

    eixo_y = []
    y_central = 0 # Variável para guardar o Y exato do seu ponto

    # Calcula o Y para cada pontinho do X e acha o Y central
    for x in eixo_x:
        if nome_operacao == "exponencial":
            y = exp_taylor(x)
            if x == num_central: y_central = y
        elif nome_operacao == "ln":
            y = ln_taylor(x) if x > 0 else np.nan
        elif nome_operacao == "log":
            y = log_taylor(x) if x > 0 else np.nan
        elif nome_operacao == "potencia":
            y = potencia10(x)
        elif nome_operacao == "seno":
            y = seno_taylor(x, tipo_angulo)
        elif nome_operacao == "cosseno":
            y = cosseno_taylor(x, tipo_angulo)
        elif nome_operacao == "tangente":
            y = tangente_taylor(x, tipo_angulo)
            if y > 200 or y < -200: y = np.nan 
        elif nome_operacao == "senh":
            y = senh_taylor(x)
        elif nome_operacao == "cosh":
            y = cosh_taylor(x)
        
        eixo_y.append(y)

    # Calculando o Y_central especificamente para ter precisão na hora de anotar
    if nome_operacao == "exponencial": y_central = exp_taylor(num_central)
    elif nome_operacao == "ln": y_central = ln_taylor(num_central) if num_central > 0 else np.nan
    elif nome_operacao == "log": y_central = log_taylor(num_central) if num_central > 0 else np.nan
    elif nome_operacao == "potencia": y_central = potencia10(num_central)
    elif nome_operacao == "seno": y_central = seno_taylor(num_central, tipo_angulo)
    elif nome_operacao == "cosseno": y_central = cosseno_taylor(num_central, tipo_angulo)
    elif nome_operacao == "tangente": y_central = tangente_taylor(num_central, tipo_angulo)
    elif nome_operacao == "senh": y_central = senh_taylor(num_central)
    elif nome_operacao == "cosh": y_central = cosh_taylor(num_central)

    # Desenha o gráfico
    plt.figure(figsize=(8, 5))
    plt.plot(eixo_x, eixo_y, color='purple', linewidth=2, label=nome_operacao)
    
    # Desenha a linha pontilhada marcando o X
    plt.axvline(num_central, color='red', linestyle='--', alpha=0.5)
    
    # --- NOVIDADE: PLOTANDO O PONTO E A ANOTAÇÃO ---
    if not np.isnan(y_central):
        # Desenha uma bolinha vermelha no ponto exato
        plt.plot(num_central, y_central, marker='o', color='red')
        
        # Escreve as coordenadas (x, y) do lado da bolinha
        plt.annotate(
            f'({num_central}, {round(y_central, 4)})', # Texto que vai aparecer (arredondado para 4 casas para ficar bonito)
            xy=(num_central, y_central),               # Ponto de referência
            xytext=(10, 10),                           # Afasta o texto 10 pontinhos pra não ficar em cima da bolinha
            textcoords='offset points',
            fontsize=10,
            fontweight='bold',
            color='darkred'
        )
    # -----------------------------------------------

    plt.title(f'Gráfico da função {nome_operacao.capitalize()}')
    plt.xlabel('Valores de X')
    plt.ylabel('Resultado (Y)')
    plt.grid(True)
    plt.legend()
    plt.show()
    if nome_operacao == "fatorial":
        print("Gráfico contínuo não é suportado para fatorial.")
        return

    print(f"\n--- Gerando gráfico de {nome_operacao}... Aguarde. ---")
    
    # AJUSTE INTELIGENTE DA JANELA (ZOOM)
    if tipo_angulo == "graus":
        # Para ver as ondas trigonométricas inteiras, olhamos uma janela de 360 graus
        eixo_x = np.linspace(num_central - 360, num_central + 360, 200)
    elif nome_operacao in ["ln", "log"]:
        # Logaritmo não aceita zero ou negativo, então começamos de 0.1 até um pouco depois do seu número
        inicio = 0.1
        fim = num_central + 20 if num_central > 0 else 20
        eixo_x = np.linspace(inicio, fim, 100)
    elif nome_operacao == "potencia":
        # Potência cresce rápido demais, uma janela menor (-3 a 3) fica melhor
        eixo_x = np.linspace(num_central - 3, num_central + 3, 100)
    else:
        # Para as outras (exponencial, radianos, hiperbólicas), a janela padrão de -10 a 10
        eixo_x = np.linspace(num_central - 10, num_central + 10, 100)

    eixo_y = []

    # Calcula o Y para cada pontinho do X
    for x in eixo_x:
        if nome_operacao == "exponencial":
            y = exp_taylor(x)
        elif nome_operacao == "ln":
            y = ln_taylor(x) if x > 0 else np.nan
        elif nome_operacao == "log":
            y = log_taylor(x) if x > 0 else np.nan
        elif nome_operacao == "potencia":
            y = potencia10(x)
        elif nome_operacao == "seno":
            y = seno_taylor(x, tipo_angulo)
        elif nome_operacao == "cosseno":
            y = cosseno_taylor(x, tipo_angulo)
        elif nome_operacao == "tangente":
            # Tangente tem assíntotas que estragam o gráfico, limitamos valores muito absurdos
            y = tangente_taylor(x, tipo_angulo)
            if y > 200 or y < -200: y = np.nan 
        elif nome_operacao == "senh":
            y = senh_taylor(x)
        elif nome_operacao == "cosh":
            y = cosh_taylor(x)
        
        eixo_y.append(y)

    # Desenha o gráfico
    plt.figure(figsize=(8, 5))
    plt.plot(eixo_x, eixo_y, color='purple', linewidth=2, label=nome_operacao)
    
    # Desenha a linha marcando o número que você digitou
    plt.axvline(num_central, color='red', linestyle='--', label=f'Seu X = {num_central}')
    
    plt.title(f'Gráfico da função {nome_operacao.capitalize()}')
    plt.xlabel('Valores de X')
    plt.ylabel('Resultado (Y)')
    plt.grid(True)
    plt.legend()
    plt.show()


def pi_taylor():
    # Calcula arctan(x) usando Taylor (Fórmula de Machin para Pi exato)
    def arctan_taylor(x):
        soma = 0
        for k in range(20):
            termo = (((-1) ** k) * (x ** (2 * k + 1))) / (2 * k + 1)
            soma += termo
        return soma

    return 4 * (4 * arctan_taylor(1 / 5) - arctan_taylor(1 / 239))


def processar_entrada(texto):
    # Calcula o valor de Pi com altíssima precisão
    PI = pi_taylor()

    # Limpa espaços e deixa tudo em minúsculo
    texto = texto.lower().replace(" ", "")

    # Transforma "3pi" em "3*pi" para o Python entender a multiplicação
    texto = re.sub(r"(\d)(pi)", r"\1*\2", texto)

    # Substitui 'pi' pelo valor numérico correto
    texto = texto.replace("pi", str(PI))

    # Avalia a expressão matemática tratada
    try:
        return float(eval(texto))
    except:
        raise ValueError("Expressão inválida!")


def fatorial(num):
    resultado = 1
    contador = 1
    while contador <= num:
        resultado = resultado * contador
        contador = contador + 1
    return resultado


def exp_taylor(num):
    soma = 1
    k = 1
    while k <= 100:
        termo = (num**k) / fatorial(k)
        soma = soma + termo
        k = k + 1
    return soma


def ln_taylor(num):
    soma = 0
    k = 0
    y = (num - 1) / (num + 1)
    while k <= 500:
        n = 2 * k + 1
        termo = (y**n) / n
        soma += termo
        k = k + 1
    return 2 * soma


def log_taylor(num):
    log = ln_taylor(num) / ln_taylor(10)
    return log


def potencia10(num):
    potencia = 10**num
    return potencia


def seno_taylor(num, tipo):
    # Se o tipo for graus, converte num para radianos usando pi_taylor
    if tipo == "graus":
        num = num * (pi_taylor() / 180)

    seno = 0
    k = 0
    while k <= 15:
        n = 2 * k + 1
        termo = (((-1) ** k) * (num**n)) / fatorial(n)
        seno += termo
        k = k + 1
    return round(seno,10)


def cosseno_taylor(num, tipo):
    # Se o tipo for graus, converte num para radianos usando pi_taylor
    if tipo == "graus":
        num = num * (pi_taylor() / 180)

    cos = 0
    k = 0
    while k <= 15:
        n = 2 * k
        termo = (((-1) ** k) * (num**n)) / fatorial(n)
        cos += termo
        k = k + 1
    return round(cos,10)


def tangente_taylor(num, tipo):
    if tipo.lower() == "graus":
        num = num * (pi_taylor() / 180)

    tang = seno_taylor(num, "radianos") / cosseno_taylor(num, "radianos")
    return round(tang, 10)


def senh_taylor(num):
    primeiro_termo = exp_taylor(num)
    segundo_termo = exp_taylor(-num)
    soma = (primeiro_termo - segundo_termo) / 2
    return soma


def cosh_taylor(num):
    primeiro_termo = exp_taylor(num)
    segundo_termo = exp_taylor(-num)
    soma = (primeiro_termo + segundo_termo) / 2
    return soma
    

# ==================================
# CALCULADORA CIENTIFICA BABADEIRA
# ==================================
print("Olá, bem vindo a calculadora científica")
operacao = input("Digite a operação que você deseja realizar: ").lower().strip()

if operacao == "fatorial":
    num = int(input("Digite o numero que você quer calcular o fatorial: "))
    resultado = fatorial(num)
    print(f"O resultado do fatorial é: {resultado}")
    criar = input("Você deseja criar o gráfico dessa função? [sim/não] ")
    if criar == "sim":
        criar_grafico(operacao, num)

if operacao == "exponencial":
    num = int(input("Digite o valor de X: "))
    resultado = exp_taylor(num)
    print(f"O resultado do exponencial é: {resultado}")
    criar = input("Você deseja criar o gráfico dessa função? [sim/não] ")
    if criar == "sim":
        criar_grafico(operacao, num)

if operacao == "ln":
    num = float(
        input(
            "Digite o valor de X [O NUMERO DEVE SER OBRIGATORIAMENTE MAIOR QUE ZERO]: "
        )
    )
    resultado = ln_taylor(num)
    print(f"O resultado do ln é: {resultado}")
    criar = input("Você deseja criar o gráfico dessa função? [sim/não] ")
    if criar == "sim":
        criar_grafico(operacao, num)

if operacao == "log":
    num = float(input("Digite o valor de X: "))
    resultado = log_taylor(num)
    print(f"O resultado do log é: {resultado}")
    criar = input("Você deseja criar o gráfico dessa função? [sim/não] ")
    if criar == "sim":
        criar_grafico(operacao, num)

if operacao == "potencia":
    num = float(input("Digite o valor de X: "))
    resultado = potencia10(num)
    print(f"O resultado da potência é: {resultado}")
    criar = input("Você deseja criar o gráfico dessa função? [sim/não] ")
    if criar == "sim":
        criar_grafico(operacao, num)

if operacao == "seno":
    entrada = input("Digite o valor de X: ")
    num = processar_entrada(entrada)
    tipo = input("RESULTADO EM GRAUS OU RADIANOS?: ")
    resultado = seno_taylor(num, tipo)

    print(f"O resultado do seno é: {resultado} para x = {num}")
    criar = input("Você deseja criar o gráfico dessa função? [sim/não] ")
    if criar == "sim":
        criar_grafico(operacao, num, tipo)

if operacao == "cosseno":
    entrada = input("Digite o valor de X: ")
    num = processar_entrada(entrada)
    tipo = input("RESULTADO EM GRAUS OU RADIANOS?: ")
    resultado = cosseno_taylor(num, tipo)

    print(f"O resultado do cosseno é: {resultado} para x = {num}")
    criar = input("Você deseja criar o gráfico dessa função? [sim/não] ")
    if criar == "sim":
        criar_grafico(operacao, num, tipo)
  
if operacao == "tangente":
    entrada = input("Digite o valor de X: ")
    num = processar_entrada(entrada)
    tipo = input("RESULTADO EM GRAUS OU RADIANOS?: ")
    resultado = tangente_taylor(num, tipo)

    print(f"O resultado da tangente é: {resultado} para x = {num}")
    criar = input("Você deseja criar o gráfico dessa função? [sim/não] ")
    if criar == "sim":
        criar_grafico(operacao, num, tipo)

if operacao == "senh":
    entrada = input("Digite o valor de X: ")
    num = processar_entrada(entrada)
    resultado = senh_taylor(num)
    print(f"O resultado do seno hiperbólico é: {resultado} para x = {num}")
    criar = input("Você deseja criar o gráfico dessa função? [sim/não] ")
    if criar == "sim":
        criar_grafico(operacao, num)

if operacao == "cosh":
    entrada = input("Digite o valor de X: ")
    num = processar_entrada(entrada)
    resultado = cosh_taylor(num)
    print(f"O resultado do seno hiperbólico é: {resultado} para x = {num}")
    criar = input("Você deseja criar o gráfico dessa função? [sim/não] ")
    if criar == "sim":
        criar_grafico(operacao, num)