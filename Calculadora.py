num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))  
operação = input("Selecione a operação desejada (1-Soma\n2-Subtração\3-Multiplicação\4-Divisão): ")
if operação == "1":
    resultado = num1 + num2
    print(f'{num1} + {num2} = {resultado}')
elif operação == "2":
    resultado = num1 - num2
    print(f'{num1} - {num2} = {resultado}')
elif operação == "3":
    resultado = num1 * num2
    print(f'{num1} * {num2} = {resultado}')
elif operação == "4":
    resultado = num1 / num2
    print(f'{num1} / {num2} = {resultado}')
else:
    print("Operação inválida. Tente novamente.")
