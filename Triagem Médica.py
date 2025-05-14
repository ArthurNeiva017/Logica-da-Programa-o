# Programa simples de triagem médica

# Lista para armazenar os atendimentos
atendimentos = []

# Mapeamento de sintomas para níveis de urgência
mapa_urgencia = {
    "urgente": ["dor no peito", "desmaio", "dificuldade para respirar", "hemorragia"],
    "alto": ["febre alta", "vômito", "dor intensa", "queda"],
    "médio": ["dor moderada", "tontura", "tosse", "diarreia"],
    "leve": ["dor de cabeça", "espirro", "coriza", "cansaço leve"]
}

def classificar_urgencia(sintomas):
    sintomas = sintomas.lower()
    for nivel, palavras in mapa_urgencia.items():
        for palavra in palavras:
            if palavra in sintomas:
                return nivel.capitalize()
    return "Leve"  # padrão se não encontrar correspondência

def solicitar_dados():
    cpf = (input("Digite o CPF: "))
    while len(cpf) < 11:
        print('CPF inválido. O CPF deve ter 11 dígitos.')
        cpf = (input("Digite o CPF: "))
    nome = (input("Digite o nome completo: "))
    while len(nome) < 3 or len(nome) > 120:
        print('Nome inválido. O nome deve ter mais de 3 caracteres.')
        nome = (input("Digite o nome completo: "))
    idade = int(input("Digite a idade: "))
    while idade < 0 or idade > 120:
        print('Idade inválida. A idade deve ser entre 0 e 120 anos.')
        idade = int(input("Digite a idade: "))
    peso = int(input("Digite o peso: "))
    while peso < 0 or peso > 300:
        print('Peso inválido. O peso deve ser entre 0 e 300 kg.')
        peso = int(input("Digite o peso: "))
    sintomas = input("Descreva os sintomas: ")

    urgencia = classificar_urgencia(sintomas)

    atendimento = {
        "CPF": cpf,
        "Nome": nome,
        "Idade": idade,
        "Peso": peso,
        "Sintomas": sintomas,
        "Urgência": urgencia
    }

    atendimentos.append(atendimento)

def mostrar_atendimentos():
    # Ordenar por urgência: Urgente > Alto > Médio > Leve
    prioridade = {"Urgente": 1, "Alto": 2, "Médio": 3, "Leve": 4}
    atendimentos.sort(key=lambda x: prioridade.get(x["Urgência"], 5))

    print("\n--- Lista de Atendimentos ---")
    print("{:<15} {:<20} {:<10} {:<8} {:<15} {:<10}".format("CPF", "Nome", "Idade", "Peso", "Urgência", "Sintomas"))
    print("-" * 80)
    for a in atendimentos:
        print("{:<15} {:<20} {:<10} {:<8} {:<15} {:<10}".format(
            a["CPF"], a["Nome"], a["Idade"], a["Peso"], a["Urgência"], a["Sintomas"][:25] + "..."
        ))

# Loop principal
while True:
    solicitar_dados()
    cont = input("Deseja adicionar outro paciente? (s/n): ")
    if cont.lower() != 's':
        break

mostrar_atendimentos()
