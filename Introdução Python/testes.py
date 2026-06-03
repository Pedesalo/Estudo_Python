# --- Desafio 8 (Ordenação Simples - Bubble Sort) ---
# 1. Crie uma lista com 8 números totalmente desordenados.
numeros = [9,6,1,3,6,2,4,25]
# 2. Crie dois laços 'for' aninhados (um dentro do outro) para comparar os vizinhos.
# 3. O laço interno deve comparar se o elemento atual é maior que o próximo elemento.
# 4. Se for maior, você deve trocar os dois de posição na lista.
# 5. Repita o processo até que nenhum elemento precise ser trocado. Imprima a lista final.
for j in range(8):
    for i in range(7):
        if numeros[i] < numeros[int(i+1)]:
            n1 = numeros[i]
            n2 = numeros[i+1]
            numeros[i] = n2
            numeros[i+1] = n1
print(numeros)