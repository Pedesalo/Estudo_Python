# 20. Crie um programa que use 'try/except' para pedir um número ao usuário. 

try:
    numero = int(input("escreva um número inteiro: "))
    print(f"você escreveu o número {numero}.")
except:
    print("Era pra você escrever um número inteiro, não use letras nem números de ponto flutuante da próxima vez!")