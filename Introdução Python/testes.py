
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
status_agrupado = {}

for status in vendas:
    if status in status_agrupado:
        
    else:
        status_agrupado['status'] = []