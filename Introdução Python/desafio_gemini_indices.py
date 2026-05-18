# Lista de temperaturas (da segunda-feira passada até domingo)
temperaturas = [28.5, 30.1, 29.0, 32.4, 26.8, 25.0, 27.3]
dias = {"Segunda":0,"Terça":1,"Quarta":2,"Quinta":3,"Sexta":4,"Sábado":5,"Domingo":6}

# --- SEU OBJETIVO ---
# 1. Acesse e imprima a temperatura de quarta-feira (quarto elemento).
print(f"Temperatura de Quarta-Feira é {temperaturas[dias['Quarta']]}")
# 2. Acesse e imprima a temperatura do último dia (domingo) usando índice negativo.
print(f'Temperaduta de Domingo é {temperaturas[-1]}')
# 3. Extraia uma sublista apenas com os dias do fim de semana (sexta, sábado e domingo).
print(f'As Temperaturas de Sexta-feira até Domingo serão: {temperaturas[4:7]}')

# --- COMENTÁRIO GUIA (Siga estes passos):
# Passo 1: Lembre-se que o Python começa a contar os índices do 0. Então, segunda é 0, terça é 1...
# Passo 2: Para pegar o último elemento direto, use o índice [-1].
# Passo 3: No fatiamento [inicio:fim], o índice de 'fim' não é incluído. Descubra onde começa a sexta-feira e vá até o final.

#-------------------------------------------------------------------------------------------------------------------------------------------

cidades_acessos = ['Joinville', 'Blumenau', 'Joinville', 'Florianópolis', 'Joinville', 'Blumenau', 'Itajaí']

# --- SEU OBJETIVO ---
# Criar um dicionário chamado 'contagem' onde a chave é o nome da cidade e o valor é a quantidade de acessos.
contagem = {}
for cidade in cidades_acessos:
    if cidade in contagem:
        contagem[cidade] = contagem[cidade] + 1
    else:
        contagem[cidade] = 1
# O resultado final deve ser: {'Joinville': 3, 'Blumenau': 2, 'Florianópolis': 1, 'Itajaí': 1}
print(contagem)
# --- COMENTÁRIO GUIA (Siga estes passos):
# Passo 1: Inicialize um dicionário vazio. ex: contagem = {}
# Passo 2: Faça um laço 'for' para percorrer cada cidade da lista 'cidades_acessos'.
# Passo 3: Dentro do laço, use um 'if' para verificar se a cidade já existe como CHAVE no dicionário.
# Passo 4: Se já existir, some +1 no valor daquela chave.
# Passo 5: Se não existir (else), adicione a cidade ao dicionário com o valor inicial de 1.

#-------------------------------------------------------------------------------------------------------------------------------------------
estoque = [
    {"id": 101, "nome": "Placa ESP32", "preco": 45.00, "quantidade": 15},
    {"id": 102, "nome": "Sensor LDR", "preco": 5.50, "quantidade": 50},
    {"id": 103, "nome": "Cabo Jumper (40 un)", "preco": 12.00, "quantidade": 30}
]

# --- SEU OBJETIVO ---
# 1. Usuário digita um ID (ex: 102).
# 2. Seu programa deve percorrer a lista, encontrar o produto e exibir o nome e o valor total em estoque (preco * quantidade).
# 3. Se o ID não existir, avise o usuário.

# --- COMENTÁRIO GUIA (Siga estes passos):
# Passo 1: Use a função input() para pedir o ID ao usuário (lembre-se de converter para int).
# Passo 2: Crie uma variável 'produto_encontrado = False' para te ajudar no controle.
# Passo 3: Use um 'for' para iterar pela lista 'estoque'. Cada item do loop será um dicionário (ex: 'produto').
# Passo 4: Dentro do loop, acesse a chave do ID do dicionário: if produto["id"] == id_digitado:
# Passo 5: Se achar, calcule o total (preco * quantidade), imprima as informações e mude 'produto_encontrado' para True. Use o comando 'break' para parar o loop.
# Passo 6: Fora do loop, use um 'if not produto_encontrado:' para exibir a mensagem de erro caso o ID não exista.

#----------------------------------------------------------------------------------------------------------------------------------------------

vendas = [
    {"cliente": "Ana", "valor": 150.00, "status": "Pago"},
    {"cliente": "Carlos", "valor": 85.50, "status": "Pendente"},
    {"cliente": "Bruno", "valor": 200.00, "status": "Pago"},
    {"cliente": "Ana", "valor": 45.00, "status": "Cancelado"},
    {"cliente": "Diego", "valor": 120.00, "status": "Pendente"}
]

# --- SEU OBJETIVO ---
# Criar um dicionário chamado 'status_agrupado'.
# O resultado esperado deve ser:
# {
#    "Pago": ["Ana", "Bruno"],
#    "Pendente": ["Carlos", "Diego"],
#    "Cancelado": ["Ana"]
# }

# --- COMENTÁRIO GUIA (Siga estes passos):
# Passo 1: Comece com um dicionário vazio: status_agrupado = {}
# Passo 2: Percorra a lista 'vendas' com um laço 'for'.
# Passo 3: Para cada venda, extraia o status e o cliente em variáveis para facilitar.
# Passo 4: Verifique se o 'status' NÃO está no dicionário 'status_agrupado'.
# Passo 5: Se NÃO estiver, você precisa criar a chave e iniciar ela com uma LISTA vazia: status_agrupado[status] = []
# Passo 6: Agora que a chave com a lista existe (ou acabou de ser criada), use o método .append(cliente) para adicionar o nome do cliente àquela lista.