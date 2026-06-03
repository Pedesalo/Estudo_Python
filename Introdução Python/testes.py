# --- Desafio 7 (Inversão Sem Função Nativa) ---
# 1. Crie uma lista com 5 palavras quaisquer.
palavras = ['anatel','marmelada','mamaqui','mamaco','papaquica']
# 2. Crie uma lista vazia chamada 'invertida'.
invertida = []
# 3. Use um laço 'for' que comece no último índice e vá até o primeiro (andando para trás).
for i in range(len(palavras),0,-1):
# 4. Dica: você pode usar range(len(lista) - 1, -1, -1) para gerar os índices invertidos.
# 5. Adicione os elementos na lista 'invertida' com base nesses índices e imprima o resultado.
    local = i-1
    invertida.append(palavras[local])
print(f" A lista invertida é : {invertida}")