print("----Semaforo----")
print("\n    1.Verde")
print("\n    2.Amarelo")
print("\n    3.Vermelho")
semaforo = int(input("Digite o valor correspondente a cor"))

match semaforo:
    case 1:
        print("Siga")
    case 2:
        print("Atenção")
    case 3:
        print("Pare")
    case _:
        print("Valor inválido, escolha o número correspondente a cor corretamente!")