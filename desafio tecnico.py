import json


def opcao_1():
    INDICE = 13
    SOMA = 0
    K = 0

    while K < INDICE:
        K = K + 1
        SOMA = SOMA + K

    print(f"O valor final de SOMA é: {SOMA}")

def opcao_2():
    def fibonacci(n):
        fib_sequence = [0, 1]
        while fib_sequence[-1] < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return n in fib_sequence

    numero = int(input("Informe um número: "))

    if fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")

def opcao_3():
    with open('faturamento.json', 'r') as file:
        dados = json.load(file)
    
    faturamento_diario = dados['faturamento_diario']

    dias_com_faturamento = [item['faturamento'] for item in faturamento_diario if item['faturamento'] > 0]
    
    if len(dias_com_faturamento) == 0:
        print("Não há faturamento registrado nos dias úteis.")
        return

    media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

    menor_faturamento = min(dias_com_faturamento)
    maior_faturamento = max(dias_com_faturamento)

    dias_acima_media = [
        item['dia'] for item in faturamento_diario if item['faturamento'] > media_mensal
    ]

    print(f"Menor faturamento: R${menor_faturamento}")
    print(f"Maior faturamento: R${maior_faturamento}")
    print(f"Número de dias com faturamento superior à média mensal: {len(dias_acima_media)}")
    print(f"Dias com faturamento superior à média: {', '.join(dias_acima_media)}")

def opcao_4():
    faturamento_estado = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }

    total_faturamento = sum(faturamento_estado.values())

    percentuais = {estado: (faturamento / total_faturamento) * 100 for estado, faturamento in faturamento_estado.items()}

    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")

def opcao_5():
    def inverter_string(s):
        return s[::-1]

    texto = input("Digite uma string: ")

    print(f"String invertida: {inverter_string(texto)}")

def menu():
    while True:
        print("\nMenu de Opções:")
        print("1. Calcular o valor de SOMA")
        print("2. Verificar se um número pertence à sequência de Fibonacci")
        print("3. Calcular dados de faturamento")
        print("4. Calcular o percentual de representação por estado")
        print("5. Inverter uma string")
        print("0. Sair")
        
        try:
            escolha = input("Escolha uma opção: ")
        except KeyboardInterrupt:
            print("\nExecução interrompida. Saindo...")
            break

        if escolha == '1':
            opcao_1()
        elif escolha == '2':
            opcao_2()
        elif escolha == '3':
            opcao_3()
        elif escolha == '4':
            opcao_4()
        elif escolha == '5':
            opcao_5()
        elif escolha == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Executa o menu
menu()
