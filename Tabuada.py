tab = int(input("Digite um número interio para ver sua tabuada: "))
print(f"Tabuada do {tab}:")
for i in range(1, 11):
    resultado = tab * i
    print(f"{tab} x {i} = {resultado}")
print("Tabuada finalizada!")