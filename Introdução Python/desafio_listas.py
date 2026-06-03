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
animal = ['macaco','tartaruga','polvo','onça','coruja']
# 2. Mostre os animais na tela e peça para o usuário digitar um nome para remover.
animais = input(f"escolha um desses animais '{animal}': ")
# 3. Use 'if' para verificar se o animal digitado está na lista.
if animais in animal:
# 4. Se estiver, remova o animal (.remove) e mostre a lista atualizada.
    animal.remove(animais)
    print(f'{animais} removido, a lista de animais é {animal}')
# 5. Se não estiver, use o 'else' para mostrar uma mensagem de erro.
else:
    print('erro')


# --- Desafio 3 (Tamanho e Acesso) ---
# 1. Crie uma lista estática com 6 números inteiros de sua escolha.
numeros = [7,8,10,15,22,119]
# 2. Descubra e guarde o primeiro elemento usando o índice zero [0].
primeiro_numero = numeros[0]
# 3. Descubra e guarde o último elemento usando o índice negativo [-1].
ultimo_numero = numeros[-1]
# 4. Descubra o tamanho total da lista usando a função len().
contagem = len(numeros)
# 5. Imprima os três valores obtidos no terminal.
print(f'O primeiro número é {primeiro_numero} e o ultimo é {ultimo_numero}, está lista tem {contagem} itens.')

# ==========================================
# 2. NÍVEL INTERMEDIÁRIO: LAÇOS DE REPETIÇÃO
# ==========================================

# --- Desafio 4 (Exibição Formatada) ---
# 1. Crie uma lista chamada 'produtos' com 4 nomes de eletrônicos.
produtos = ["Smartphone", "Smart TV", "Notebook", "Fone de Ouvido Bluetooth"]
# 2. Crie outra lista chamada 'precos' com 4 valores numéricos (preços).
precos = [2500.00, 3500.00, 4200.00, 300.00]
# 3. Use um laço 'for' para percorrer os índices de 0 a 3 (use range).
for i in range(0,4):
# 4. Dentro do laço, acesse o produto e o preço correspondente ao índice atual.
    produto = produtos[i]
    preco = precos[i]
# 5. Imprima formatado na tela: "Produto: X - Preço: R$ Y".
    print(f"Produto: {produto} - Preço: R$ {preco}")

# --- Desafio 5 (Filtragem) ---
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


# --- Desafio 6 (Estatísticas) ---
# 1. Crie uma lista com 5 notas de alunos (números com ponto flutuante).
nota = [4.0,5.5,9.5,8.5,10.0]
# 2. Calcule a média: some todos os elementos (sum) e divida pelo total (len).
media = sum(nota)/len(nota)
# 3. Descubra a maior nota da lista usando a função max().
maior = max(nota)
# 4. Descubra a menor nota da lista usando a função min().
menor = min(nota)
# 5. Imprima a média, a maior e a menor nota na tela.
print(f'A média das notas é: {media}. A maior nota é: {maior}. A menor nota é: {menor}')

# ==========================================
# 3. NÍVEL AVANÇADO: ALGORITMOS E MATRIZES
# ==========================================

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


# --- Desafio 9 (Matrizes / Lista de Listas) ---
# 1. Crie uma matriz 3x3 (uma lista principal que contém 3 sublistas, cada uma com 3 números).
# 2. Crie uma variável contadora chamada 'maiores_que_10' começando em 0.
# 3. Use um laço 'for' externo para acessar cada linha da matriz.
# 4. Use um laço 'for' interno para acessar cada número daquela linha específica.
# 5. Se o número atual for maior que 10, aumente o contador em 1.
# 6. Imprima o total acumulado no contador no final.
