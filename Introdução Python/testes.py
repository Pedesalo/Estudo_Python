# 19. Escreva uma função que verifique se um número é positivo ou negativo (retorne True ou False).

def pos_neg(numero):
    if numero > 0:
        numero = True
    else:
        numero = False
    print(numero)

numero = -1
pos_neg(numero)