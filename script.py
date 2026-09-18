# ==================================
# CALCULADORA CIENTIFICA BABADEIRA
# ==================================
import re


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
    

# ==================================
# CALCULADORA CIENTIFICA BABADEIRA
# ==================================
print("Olá, bem vindo a calculadora científica")
operacao = input("Digite a operação que você deseja realizar: ").lower().strip()

if operacao == "fatorial":
    num = int(input("Digite o numero que você quer calcular o fatorial: "))
    resultado = fatorial(num)
    print(f"O resultado do fatorial é: {resultado}")

if operacao == "exponencial":
    num = int(input("Digite o valor de X: "))
    resultado = exp_taylor(num)
    print(f"O resultado do exponencial é: {resultado}")

if operacao == "ln":
    num = float(
        input(
            "Digite o valor de X [O NUMERO DEVE SER OBRIGATORIAMENTE MAIOR QUE ZERO]: "
        )
    )
    resultado = ln_taylor(num)
    print(f"O resultado do ln é: {resultado}")

if operacao == "log":
    num = float(input("Digite o valor de X: "))
    resultado = log_taylor(num)
    print(f"O resultado do log é: {resultado}")

if operacao == "potencia":
    num = float(input("Digite o valor de X: "))
    resultado = potencia10(num)
    print(f"O resultado da potência é: {resultado}")

if operacao == "seno":
    entrada = input("Digite o valor de X: ")
    num = processar_entrada(entrada)
    tipo = input("RESULTADO EM GRAUS OU RADIANOS?: ")
    resultado = seno_taylor(num, tipo)

    print(f"O resultado do seno é: {resultado} para x = {num}")

if operacao == "cosseno":
    entrada = input("Digite o valor de X: ")
    num = processar_entrada(entrada)
    tipo = input("RESULTADO EM GRAUS OU RADIANOS?: ")
    resultado = cosseno_taylor(num, tipo)

    print(f"O resultado do cosseno é: {resultado} para x = {num}")
  
if operacao == "tangente":
    entrada = input("Digite o valor de X: ")
    num = processar_entrada(entrada)
    tipo = input("RESULTADO EM GRAUS OU RADIANOS?: ")
    resultado = tangente_taylor(num, tipo)

    print(f"O resultado da tangente é: {resultado} para x = {num}")
