# 12. Use um laço 'while' para somar números digitados pelo usuário até que ele digite 0.
numero = True
soma = 0
while numero != 0:
    numero = int(input("Digite um número diferente de 0: "))
    soma = soma + numero
print(f"A soma dos números é {soma}.")