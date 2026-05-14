# 17. Crie um dicionário 'produto' com nome e preço. Aplique 10% de desconto e exiba o novo preço.

produto = {"nome":"notebook", "preço": 3000.50}

print(f'{produto["nome"].capitalize()} custa agora com 10% de desconto R${produto["preço"]*0.90:.2f}.')