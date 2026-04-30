# =================================================================
# DESAFIO: MANIPULAÇÃO DE DADOS COMPLEXOS
# =================================================================

# EXERCÍCIO 9:
# Crie uma função chamada 'analisar_lista' que receba uma lista de números.
# A função deve realizar as seguintes operações:
# 1. Somar todos os números da lista.
# 2. Encontrar o maior número.
# 3. Filtrar a lista para gerar uma nova lista apenas com números > 10.
# 4. Retornar um dicionário com as chaves: 'soma', 'maior' e 'maiores_que_10'.

def analisar_lista(numeros):
    # DICA: Você pode usar as funções nativas sum() e max() do Python.
    # Para o filtro, você pode usar um loop 'for' ou 'list comprehension'.
    soma = sum(numeros)
    maior = max(numeros)
    maiores_que_10 = [n for n in numeros if n > 10]

    return {
        "soma" : soma,
        "maior" : maior,
        "maiores_que_10" : maiores_que_10
    }

# --- ÁREA DE TESTE ---
# 1. Crie uma lista chamada 'meus_numeros' com os valores: [5, 12, 7, 20, 3, 15]
# 2. Chame a função 'analisar_lista' passando essa lista.
# 3. Imprima o dicionário retornado.
numeros = [5, 12, 7, 20, 3, 15]

resultado = analisar_lista(numeros)
print(resultado)