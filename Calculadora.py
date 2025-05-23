Lista_de_operações = []

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

def square_root(num1):
    if num1 < 0:
        return "Raiz quadrada de número negativo não é permitida."
    return num1 ** 0.5

def media_aritimetica(valores):
        Soma = 0
        for i in range(valores):
            a = int(input("Digite os Números desejados: "))
            Soma += a
        media = (Soma) / valores
        return media

operação = input("Selecione a operação desejada: \n1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Potência\n6. Raiz Quadrada\n7. Média Aritimética\n9. Historico de Operações\n")

if operação == '1':
     num1 = int(input("Digite o primeiro número: "))
     num2 = int(input("Digite o segundo número: "))
     resultado_adição = add(num1, num2)
     print(f'Resultado: {num1} + {num2} = {resultado_adição}')
     Lista_de_operações.append(resultado_adição)

elif operação == '2':
     num1 = int(input("Digite o primeiro número: "))
     num2 = int(input("Digite o segundo número: "))
     resultado_subtração = subtract(num1, num2)
     print(f'Resultado: {num1} - {num2} = {resultado_subtração}')
     Lista_de_operações.append(resultado_subtração)

elif operação == '3':
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado_multiplicação = multiply(num1, num2)
        print(f'Resultado: {num1} x {num2} = {resultado_multiplicação}')
        Lista_de_operações.append(resultado_multiplicação)

elif operação == '4':
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado_divisão = divide(num1, num2)
        print(f'Resultado: {num1} / {num2} = {resultado_divisão}')
        Lista_de_operações.append(resultado_divisão)

elif operação == '5':
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado_potência = power(num1, num2)
        print(f'Resultado: {num1} ^ {num2} = {resultado_potência}')
        Lista_de_operações.append(resultado_potência)

elif operação == '6':
        num1 = int(input("Digite o número: "))
        resultado_raiz_quadrada = square_root(num1)
        print(f'Resultado: √{num1} = {resultado_raiz_quadrada}')
        Lista_de_operações.append(resultado_raiz_quadrada)

elif operação == '7':
        valores = int(input("Quantos números deseja calcular a média: "))
        resultado_media_aritimetica = media_aritimetica(valores)
        print(f'Resultado: {resultado_media_aritimetica}')
        Lista_de_operações.append(resultado_media_aritimetica)

elif operação == '9':
        
        if len(Lista_de_operações) == 0:
            print("Nenhuma operação foi realizada.")
        else:
          print(f'Esse é o histórico de operações: {Lista_de_operações}')

if operação != "1" and operação != "2" and operação != "3" and operação != "4" and operação != "5" and operação != "6" and operação != "7" and operação != "9":
    print("Operação inválida.")

while True:
      continuar = input("Deseja continuar? (s/n): ")
      
      if continuar.lower() == 'n':
            print("Encerrando o programa.")
            break
      
      elif continuar.lower() == 's':
            operação = input("Selecione a operação desejada: \n1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Potência\n6. Raiz Quadrada\n7. Média Aritimética\n9. Histórico de Operações\n")
            
            if operação == '1':
                num1 = int(input("Digite o primeiro número: "))
                num2 = int(input("Digite o segundo número: "))
                resultado_adição = add(num1, num2)
                print(f'Resultado: {num1} + {num2} = {resultado_adição}')
                Lista_de_operações.append(resultado_adição)
            
            elif operação == '2':
                num1 = int(input("Digite o primeiro número: "))
                num2 = int(input("Digite o segundo número: "))
                resultado_subtração = subtract(num1, num2)
                print(f'Resultado: {num1} - {num2} = {resultado_subtração}')
                Lista_de_operações.append(resultado_subtração)
            
            elif operação == '3':
                    num1 = int(input("Digite o primeiro número: "))
                    num2 = int(input("Digite o segundo número: "))
                    resultado_multiplicação = multiply(num1, num2)
                    print(f'Resultado: {num1} x {num2} = {resultado_multiplicação}')
                    Lista_de_operações.append(resultado_multiplicação)
            
            elif operação == '4':
                    num1 = int(input("Digite o primeiro número: "))
                    num2 = int(input("Digite o segundo número: "))
                    resultado_divisão = divide(num1, num2)
                    print(f'Resultado: {num1} / {num2} = {resultado_divisão}')
                    Lista_de_operações.append(resultado_divisão)
            
            elif operação == '5':
                    num1 = int(input("Digite o primeiro número: "))
                    num2 = int(input("Digite o segundo número: "))
                    resultado_potência = power(num1, num2)
                    print(f'Resultado: {num1} ^ {num2} = {resultado_potência}')
                    Lista_de_operações.append(resultado_potência)
            
            elif operação == '6':
                    num1 = int(input("Digite o número: "))
                    resultado_raiz_quadrada = square_root(num1)
                    print(f'Resultado: √{num1} = {resultado_raiz_quadrada}')
                    Lista_de_operações.append(resultado_raiz_quadrada)
            
            elif operação == '7':
                    valores = int(input("Quantos números deseja calcular a média: "))
                    resultado_media_aritimetica = media_aritimetica(valores)
                    print(f'Resultado: {resultado_media_aritimetica}')
                    Lista_de_operações.append(resultado_media_aritimetica)
            
            elif operação == '9':
                    
                    if len(Lista_de_operações) == 0:
                        print("Nenhuma operação foi realizada.")
                    
                    else:
                      print(f'Esse é o histórico de operações: {Lista_de_operações}')
            
            else:
                print("Operação inválida.")