import time
import random

#Lista de códigos para praticar
desafios = [
    "[x**2 for x in range(10) if x % 2 == 0]",
    "print(f'Olá, {nome}!')",
    "sorted(lista, key=lamba) x: x['preco']",
    "with open('arquivo.txt', 'r') as f:",
    "dict_comprehension = {k: v for k, v in itens}",
    "try:\n   pass\nexcept Exception as e:\n    print(e)",
    "import json\ndados = json.loads(resposta.text)"
]

def treinar():
    print("---Desafio de Digitação Python ---")
    print("Copie  o código exatamente como ele aparece.\n")

    codigo_alvo = random.choice(desafios)
    print("DIGITE O CÓDIGO ABAIXO:")
    print("-" * 30)
    print(codigo_alvo)
    print("-" * 30)

    inicio = time.time()
    entrada = input("\n> ")
    fim = time.time()

    tempo_gasto = fim - inicio

    if entrada == codigo_alvo.replace("\n", " "): # Simplifica a entrada de múltiplas linhas de input
        print(f"\n Perfeito! Tempo: {tempo_gasto:.2f} segundos.")
    elif entrada == codigo_alvo:
        print(f"\n Perfeito! Tempo: {tempo_gasto:.2f} segundos.")
    else:
        print("\n Erro na digitação.")
        print(f"Esperado: {codigo_alvo}")
        print(f"Digitado: {entrada}")

if __name__ == "__main__":
    while True:
        treinar()
        if input("\nContinuar treinando? (s/n)").lower() != 's':
            break