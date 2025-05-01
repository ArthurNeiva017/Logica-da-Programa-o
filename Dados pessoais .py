nome = (input("Digite seu nome: "))
while len(nome) < 3 or len(nome) > 40:
    print("Nome inválido. O nome deve ter entre 3 e 40 caracteres.")
    nome = input("Digite seu nome: ")

idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 150:
    print("Idade inválida. A idade deve estar entre 0 e 150 anos.")
    idade = int(input("Digite sua idade: "))

salario = int(input("Digite seu salário: "))
while salario < 0:
    print("Salário inválido. O salário não pode ser negativo.")
    salario = int(input("Digite seu salário: "))

sexo = input("Digite seu sexo 'Masculino' ou 'Feminino': ")
while sexo not in ['Masculino', 'Feminino']:
    print("Sexo inválido. O sexo deve ser 'Masculino' ou 'Feminino'.")
    sexo = input("Digite seu sexo 'Masculino' ou 'Feminino': ")


estado_civil = input("Digite seu estado civil (Solteiro/Casado/Viuvo/Divorciado): ")
while estado_civil not in ['Solteiro', 'Casado', 'Viuvo', 'Divorciado']:
    print("Estado civil inválido. O estado civil deve ser Solteiro, Casado, Viuvo ou Divorciado.")
    estado_civil = input("Digite seu estado civil Solteiro/Casado/Viuvo/Divorciado: ")

print("Cadastro realizado com sucesso!")
print(f''' 
      
      
           ________________________________________________
           |                                                              
           |               Dados Cadastrais                            
           |                                                              
           |                                                              
           | Nome: {nome}                                                 
           | Salário: {salario}                                           
           | Idade: {idade}                                               
           | Sexo: {sexo}                                                 
           | Estado Civil: {estado_civil}                                 
           |_________________________________________________
      
      
      
      
      ''')