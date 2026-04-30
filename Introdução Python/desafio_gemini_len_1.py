# ==========================================
# DESAFIO 1: Validador de Usuário
# Objetivo: Verificar se o nome tem entre 5 e 15 caracteres.
# ==========================================

usuario = input("Digite seu nome de usuário: ")

# Escreva seu código abaixo:

Qt_caracteres = len(usuario)

resultado = "O nome tem entre 5 e 15 caracteres" if  5 <= Qt_caracteres <= 15 else "o Nome não tem entre 5 e 15 caracteres"
print(resultado)

# ==========================================
# DESAFIO 2: Contador de Inteiros
# Objetivo: Contar quantos dígitos tem um número inteiro.
# ==========================================

numero = int(input("Digite um número inteiro: "))

# Escreva seu código abaixo (dica: converta para str antes do len):

reslt = len(str(numero))
print(reslt)

# ==========================================
# DESAFIO 3: Calculadora de Média de Texto
# Objetivo: Calcular a média de tamanho de duas palavras.
# ==========================================

palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

# Escreva seu código abaixo:

p1 = len(palavra1)
p2 = len(palavra2)

print(f'a média dos caracteres é : {(p1+p2)/2}')