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