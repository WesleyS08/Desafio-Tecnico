# Desafio Técnico - Sistema de Cálculos e Processamentos

Este repositório contém a solução para um desafio técnico com diversas funcionalidades implementadas em Python. O programa oferece um menu interativo que permite ao usuário escolher entre várias operações, incluindo cálculos de soma, verificação de Fibonacci, análise de faturamento, cálculo de percentuais de estados e inversão de strings.

## Funcionalidades

O programa oferece as seguintes opções:

1. **Calcular o valor de SOMA**: Soma os números de 1 até 13 e exibe o resultado.
2. **Verificar se um número pertence à sequência de Fibonacci**: O usuário insere um número, e o sistema verifica se ele pertence ou não à sequência de Fibonacci.
3. **Calcular dados de faturamento**: O programa analisa um arquivo JSON contendo o faturamento diário de uma distribuidora, calcula o menor e maior faturamento e os dias com faturamento superior à média.
4. **Calcular o percentual de representação por estado**: Calcula e exibe o percentual que cada estado representa no faturamento total de uma distribuidora.
5. **Inverter uma string**: O programa inverte a string fornecida pelo usuário.

## Como Usar

### Pré-requisitos
- **Python** 3.x instalado no seu sistema.
- Um arquivo JSON chamado `faturamento.json` no mesmo diretório do script, com a seguinte estrutura:

```json
{
  "faturamento_diario": [
    {"dia": "2025-01-01", "faturamento": 1500},
    {"dia": "2025-01-02", "faturamento": 2500},
    {"dia": "2025-01-03", "faturamento": 3000},
    {"dia": "2025-01-04", "faturamento": 0},
    {"dia": "2025-01-05", "faturamento": 4500},
    {"dia": "2025-01-06", "faturamento": 0},
    {"dia": "2025-01-07", "faturamento": 5000},
    {"dia": "2025-01-08", "faturamento": 3000},
    {"dia": "2025-01-09", "faturamento": 1500},
    {"dia": "2025-01-10", "faturamento": 6000}
  ]
}
```
### Passo a Passo
 - 1 Clone o repositório:
   ``` git clone https://github.com/WesleyS08/Desafio-Tecnico ```
- 2 Execute o script Python: Navegue até o diretório onde o arquivo .py está localizado e execute ``` python desafio_tecnico.py ```

### Exemplo de Execução: 
```
 Menu de Opções:
1. Calcular o valor de SOMA
2. Verificar se um número pertence à sequência de Fibonacci
3. Calcular dados de faturamento
4. Calcular o percentual de representação por estado
5. Inverter uma string
0. Sair
Escolha uma opção: 3
Menor faturamento: R$1500.00
Maior faturamento: R$6000.00
Número de dias com faturamento superior à média mensal: 5
Dias com faturamento superior à média: 2025-01-02, 2025-01-03, 2025-01-05, 2025-01-07, 2025-01-10
```
