# ==================================
# CALCULADORA CIENTIFICA BABADEIRA
# ==================================
def fatorial(num):
    resultado = 1
    contador = 1
    while contador <= num:
        resultado = resultado * contador
        contador = contador + 1
    return resultado

def exp(num):
    soma = 1
    k = 1
    while k <= 500:
        termo = (num**k)/fatorial(k)
        soma = soma + termo
        k = k + 1
    return soma

def ln_taylor(num):
    soma = 0
    k = 0
    y = (num - 1) / (num + 1)
    while k <= 500:
        n = 2 * k + 1 
        termo = (y**n)/ n
        soma += termo 
        k = k + 1
    return 2 * soma
    



print("Olá, bem vindo a calculadora científica")
operacao = input("Digite a operação que você deseja realizar: ")

if operacao == "fatorial":
    num = int(input("Digite o numero que você quer calcular o fatorial: "))
    resultado = fatorial(num)
    print(f"O resultado do fatorial é: {resultado}")

if operacao == "exponencial":
    num = int(input("Digite o valor de X: "))
    resultado = exp(num)
    print(f"O resultado do exponencial é: {resultado}")

if operacao == "ln":
    num = float(input("Digite o valor de X [O NUMERO DEVE SER OBRIGATORIAMENTE DIFERENTE DE ZERO]: "))
    resultado = ln_taylor(num)
    print(f"O resultado do ln é: {resultado}")
