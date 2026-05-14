# 18. Escreva uma função que receba um nome e retorne "Bom dia, [nome]".

def cumprimento(nome):
    return f"Bom dia, {nome}"

se_identifique = input("Qual o seu nome: ")

nome = cumprimento(se_identifique)
print(nome)