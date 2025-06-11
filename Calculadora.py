# Listas Vaizas Para armazenar o histórico de operações
Historico_operações_adição = []

Historico_operações_subtração = []

Historico_operações_multiplicação = []

Historico_operações_divisão = []

Historico_operações_potenciação = []

Historico_operações_raiz = []

Historico_operações_media_aritmética = []

# Funções para realizar as operações
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Erro: Divisão por zero não é permitida."
    return num1 / num2

def power(num1, num2):
    return num1 ** num2

def square_root(num1):
    if num1 < 0:
        return "Erro: Raiz quadrada de número negativo não é permitida."
    return num1 ** (1/2)

def media_aritimetica(valores):
        Soma = 0
        for i in range(valores):
            a = int(input("Digite os Números desejados: "))
            Soma += a
        media = (Soma) / valores
        return media

# O usuário escolhe a operação
while True:
    operações =  input("Selecione a operação desejada\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Potenciação\n6 - Raiz Quadrada\n7 - Média Aritmética\n8 - Histórico de operações\n9 - Sair\n")
    while operações != "1" and operações != "2" and operações != "3" and operações != "4" and operações != "5" and operações != "6" and operações != "7" and operações != "8":
        print("Operação inválida. Por favor, selecione uma operação válida.")
        operações =  input("Selecione a operação desejada\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Potenciação\n6 - Raiz Quadrada\n7 - Média Aritmética\n7 - Histórico de operações\n9 - Sair\n")
    
    # Operação de Adição
    if operações == "1":
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado = add(num1, num2)
        ope_adição = f"({num1} + {num2} = {resultado})"
        print(f'{num1} + {num2} = {resultado}')
        Historico_operações_adição.append(ope_adição)

    # Operação de Subtração
    elif operações == "2":
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado = subtract(num1, num2)
        ope_subtração = f"({num1} - {num2} = {resultado})"
        print(f'{num1} - {num2} = {resultado}')
        Historico_operações_subtração.append(ope_subtração)

    # Operação de Multiplicação
    elif operações == "3":
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado = multiply(num1, num2)
        ope_Mutiplicação = f"({num1} x {num2} = {resultado})"
        print(f'{num1} x {num2} = {resultado}')
        Historico_operações_multiplicação.append(ope_Mutiplicação)

    # Operação de Divisão
    elif operações == "4":
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado = divide(num1, num2)
        ope_divisão = f"({num1} / {num2} = {resultado})"
        print(f'{num1} / {num2} = {resultado}')
        Historico_operações_divisão.append(ope_divisão)

    # Operação de Potenciação
    elif operações == "5":
        num1 = int(input("Digite a base: "))
        num2 = int(input("Digite o expoente: "))
        resultado = power(num1, num2)
        ope_potenciação = f"({num1} ^ {num2} = {resultado})"
        print(f'{num1} ^ {num2} = {resultado}')
        Historico_operações_potenciação.append(ope_potenciação)

    # Operação de Raiz Quadrada
    elif operações == "6":
        num1 = int(input("Digite o número: "))
        resultado = square_root(num1)
        ope_raiz_quadrada = f"(√{num1} = {resultado})"
        print(f'√{num1} = {resultado}')
        Historico_operações_raiz.append(ope_raiz_quadrada)

    # Operação de Média Aritmética
    elif operações == "7":
        valores = int(input("Quantos números deseja calcular a média aritmética? "))
        resultado = media_aritimetica(valores)
        ope_media_aritimetica = f"(Média Aritmética dos {valores} números = {resultado})"
        print(f'Média Aritmética dos {valores} números = {resultado}')
        Historico_operações_media_aritmética.append(ope_media_aritimetica)

    # Histórico de Operações
    elif operações == "8":
        historicos = input("Selecione o histórico desejado\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Potenciação\n6 - Raiz Quadrada\n7 - Média Aritmética\n")
        
        if len(Historico_operações_adição ) == 0 and len(Historico_operações_subtração) == 0 and len(Historico_operações_multiplicação) == 0 and len(Historico_operações_divisão) == 0 and len(Historico_operações_potenciação) == 0 and len(Historico_operações_raiz) == 0 and len(Historico_operações_media_aritmética) == 0:
            print("Nenhum histórico disponível.")
            
        if historicos == "1":
                print(f"Histórico de Adição: {Historico_operações_adição}")
        elif historicos == "2":
            print(f"Histórico de Subtração: {Historico_operações_subtração}")
        elif historicos == "3":
            print(f"Histórico de Multiplicação: {Historico_operações_multiplicação}")
        elif historicos == "4":
            print(f"Histórico de Divisão: {Historico_operações_divisão}")
        elif historicos == "5":
            print(f"Histórico de Potenciação: {Historico_operações_potenciação}")
        elif historicos == "6":
            print(f"Histórico de Raiz Quadrada: {Historico_operações_raiz}")
        elif historicos == "7":
            print(f"Histórico de Média Aritmética: {Historico_operações_media_aritmética}")
        else:
            print("Opção inválida. Por favor, selecione uma operação válida.")
    
    elif operações == "9":
        print("Saindo do programa.")
        print("Obrigado por usar a calculadora!")
        break