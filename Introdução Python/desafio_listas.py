# ==========================================
# 1. NÍVEL INICIANTE: MANIPULAÇÃO BÁSICA
# ==========================================

# --- Desafio 1 (Criando e Adicionando) ---
# 1. Crie uma lista vazia chamada 'compras'.
compras = []
# 2. Use um laço 'for' que rode 3 vezes.
for i in range(3):
# 3. Dentro do laço, peça para o usuário digitar um item (use input).
    lista = input("digite algo: ")
# 4. Adicione esse item na lista usando o método adequado (.append).
    compras.append(lista)
# 5. Fora do laço, imprima a lista completa na tela.
print(f"conteúdo da lista compras é : {compras}")


# --- Desafio 2 (Removendo itens) ---
# 1. Crie uma lista com 5 nomes de animais.
# 2. Mostre os animais na tela e peça para o usuário digitar um nome para remover.
# 3. Use 'if' para verificar se o animal digitado está na lista.
# 4. Se estiver, remova o animal (.remove) e mostre a lista atualizada.
# 5. Se não estiver, use o 'else' para mostrar uma mensagem de erro.


# --- Desafio 3 (Tamanho e Acesso) ---
# 1. Crie uma lista estática com 6 números inteiros de sua escolha.
# 2. Descubra e guarde o primeiro elemento usando o índice zero [0].
# 3. Descubra e guarde o último elemento usando o índice negativo [-1].
# 4. Descubra o tamanho total da lista usando a função len().
# 5. Imprima os três valores obtidos no terminal.


# ==========================================
# 2. NÍVEL INTERMEDIÁRIO: LAÇOS DE REPETIÇÃO
# ==========================================

# --- Desafio 4 (Exibição Formatada) ---
# 1. Crie uma lista chamada 'produtos' com 4 nomes de eletrônicos.
# 2. Crie outra lista chamada 'precos' com 4 valores numéricos (preços).
# 3. Use um laço 'for' para percorrer os índices de 0 a 3 (use range).
# 4. Dentro do laço, acesse o produto e o preço correspondente ao índice atual.
# 5. Imprima formatado na tela: "Produto: X - Preço: R$ Y".


# --- Desafio 5 (Filtragem) ---
# 1. Crie uma lista inicial com 10 números misturados (pares e ímpares).
# 2. Crie duas listas novas e vazias: 'pares' e 'impares'.
# 3. Use um laço 'for' para avaliar cada número da lista inicial.
# 4. Se o número for divisível por 2 (num % 2 == 0), adicione na lista 'pares'.
# 5. Se não for, adicione na lista 'impares'.
# 6. Imprima as três listas ao final.


# --- Desafio 6 (Estatísticas) ---
# 1. Crie uma lista com 5 notas de alunos (números com ponto flutuante).
# 2. Calcule a média: some todos os elementos (sum) e divida pelo total (len).
# 3. Descubra a maior nota da lista usando a função max().
# 4. Descubra a menor nota da lista usando a função min().
# 5. Imprima a média, a maior e a menor nota na tela.


# ==========================================
# 3. NÍVEL AVANÇADO: ALGORITMOS E MATRIZES
# ==========================================

# --- Desafio 7 (Inversão Sem Função Nativa) ---
# 1. Crie uma lista com 5 palavras quaisquer.
# 2. Crie uma lista vazia chamada 'invertida'.
# 3. Use um laço 'for' que comece no último índice e vá até o primeiro (andando para trás).
# 4. Dica: você pode usar range(len(lista) - 1, -1, -1) para gerar os índices invertidos.
# 5. Adicione os elementos na lista 'invertida' com base nesses índices e imprima o resultado.


# --- Desafio 8 (Ordenação Simples - Bubble Sort) ---
# 1. Crie uma lista com 8 números totalmente desordenados.
# 2. Crie dois laços 'for' aninhados (um dentro do outro) para comparar os vizinhos.
# 3. O laço interno deve comparar se o elemento atual é maior que o próximo elemento.
# 4. Se for maior, você deve trocar os dois de posição na lista.
# 5. Repita o processo até que nenhum elemento precise ser trocado. Imprima a lista final.


# --- Desafio 9 (Matrizes / Lista de Listas) ---
# 1. Crie uma matriz 3x3 (uma lista principal que contém 3 sublistas, cada uma com 3 números).
# 2. Crie uma variável contadora chamada 'maiores_que_10' começando em 0.
# 3. Use um laço 'for' externo para acessar cada linha da matriz.
# 4. Use um laço 'for' interno para acessar cada número daquela linha específica.
# 5. Se o número atual for maior que 10, aumente o contador em 1.
# 6. Imprima o total acumulado no contador no final.
