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
str_id = int(input("Escolha entre os usuários 101,102,103: "))
# Passo 2: Crie uma variável 'produto_encontrado = False' para te ajudar no controle.
produto_encontrado = False
# Passo 3: Use um 'for' para iterar pela lista 'estoque'. Cada item do loop será um dicionário (ex: 'produto').
for produto in estoque:
# Passo 4: Dentro do loop, acesse a chave do ID do dicionário: if produto["id"] == id_digitado:
    if produto['id'] == str_id:
# Passo 5: Se achar, calcule o total (preco * quantidade), imprima as informações e mude 'produto_encontrado' para True. Use o comando 'break' para parar o loop.
        faturamento = produto['preco'] * produto['quantidade']
        print(f'Preço total do produto é {faturamento}')
        produto_encontrado = True
        break
    else:
        continue
# Passo 6: Fora do loop, use um 'if not produto_encontrado:' para exibir a mensagem de erro caso o ID não exista.
if not produto_encontrado:
    print("ID não existe.")