# 3. Peça dois números e exiba o resto da divisão entre eles (operador %).

def calcular_resto(dividendo, divisor):
    resultado = dividendo // divisor
    resto = dividendo % divisor
    print(f"{dividendo} % {divisor} = {resultado} com resto {resto}.")

dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))
calcular_resto(dividendo, divisor)