# 1. Crie uma lista inicial com 10 números misturados (pares e ímpares).
pares_impares = [1,2,3,4,5,6,7,8,9,10]
# 2. Crie duas listas novas e vazias: 'pares' e 'impares'.
pares = []
impares = []
# 3. Use um laço 'for' para avaliar cada número da lista inicial.
for i in range(len(pares_impares)):
# 4. Se o número for divisível por 2 (num % 2 == 0), adicione na lista 'pares'.
    if pares_impares[i] % 2 == 0:
        pares.append(pares_impares[i])
# 5. Se não for, adicione na lista 'impares'.
    else:
         impares.append(pares_impares[i])
# 6. Imprima as três listas ao final.
print(f'lista: {pares_impares}')
print(f'pares: {pares}')
print(f'impares: {impares}')