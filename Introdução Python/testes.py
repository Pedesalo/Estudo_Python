# 1. Crie uma variável para o raio de um círculo e calcule a área (Area = 3.14 * raio^2).
def areaCirculo(raio):
    area = 3.14 * (raio ** 2)
    return area


print("Escreva o raio de um circulo, que eu entro o valor da area!")
raio = float(input("Escreva o raio(cm): "))
area = areaCirculo(raio)
print(f"Area do circulo de raio {raio}cm é de {area}cm²")