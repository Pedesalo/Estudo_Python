# 16. Crie uma lista de 5 números, ordene-os e exiba o menor e o maior valor.

lista = [1,3,2,5,4]
listaOrdem = sorted(lista)
listaMenor = min(lista)
listaMaior = max(lista)

print(f"Os números são: {lista}, em ordem crescente fica: {listaOrdem}, o maior número é: {listaMaior}, e o menor número é: {listaMenor}.")