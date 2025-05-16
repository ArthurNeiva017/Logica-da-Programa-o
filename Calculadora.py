def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    if num2 == 0:
        return "Divisão por zero não é permitida."
    return num1 / num2
def power(num1, num2):
    return num1 ** num2
def square_root(num):
    if num < 0:
        return "Raiz quadrada de número negativo não é permitida."
    return num ** 0.5
def media_aritimetica(valores):
    Soma = 0
    for i in range(valores):
        a = int(input("Digite os Números desejados: "))
        Soma += a
    media = (Soma) / valores
    return media

operacao = input("Digite a operação desejada\n1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão\n5-Potencia\n6-Raiz quadrada\n7-Media Aritimetica\n")
while operacao != "1" and operacao != "2" and operacao != "3" and operacao != "4" and operacao != "5" and operacao != "6" and operacao != "7":
    print("Operação inválida!")
    operacao = input("Digite a operação desejada:\n1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão\n5-Potencia\n6-Raiz quadrada\n7-Media Aritimetica\n")
num1 = int(input("Digite o primeiro número desejado: "))
num2 = int(input("Digite o segundo número desejado: "))

while divide(num1, num2) == "Divisão por zero não é permitida.":
    print("Divisão por zero não é permitida.")
    num1 = int(input("Digite o primeiro número desejado: "))
    num2 = int(input("Digite o segundo número desejado: "))
    operacao = input("Digite a operação desejada\n1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão\n5-Potencia\n6-Raiz quadrada\n7-Media Aritimetica\n")

if operacao == "1":
    resultado = add(num1, num2)
    print(f'{num1} + {num2} = {resultado}')
elif operacao == "2":
    resultado = subtract(num1, num2)
    print(f'{num1} - {num2} = {resultado}')
elif operacao == "3":
    resultado = multiply(num1, num2)
    print(f'{num1} x {num2} = {resultado}')
elif operacao == "4":
    resultado = divide(num1, num2)
    print(f'{num1} / {num2} = {resultado}')
elif operacao == "5":
    resultado = power(num1, num2)
    print(f'{num1} ^ {num2} = {resultado}')
elif operacao == "6":
    resultado = square_root(num1)
    print(f'A raiz quadrada de {num1} é {resultado}')
elif operacao == "7":
    valores = int(input("Quantos números deseja calcular a média aritimetica? "))
    resultado = media_aritimetica(valores)
    print(f'A média aritimetica é {resultado}')
