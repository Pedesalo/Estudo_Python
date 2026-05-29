# --- Desafio 2 (Removendo itens) ---
# 1. Crie uma lista com 5 nomes de animais.
animal = ['macaco','tartaruga','polvo','onça','coruja']
# 2. Mostre os animais na tela e peça para o usuário digitar um nome para remover.
animais = input(f"escolha um desses animais '{animal}': ")
# 3. Use 'if' para verificar se o animal digitado está na lista.
if animais in animal:
# 4. Se estiver, remova o animal (.remove) e mostre a lista atualizada.
    animal.remove(animais)
    print(f'{animais} removido, a lista de animais é {animal}')
# 5. Se não estiver, use o 'else' para mostrar uma mensagem de erro.
else:
    print('erro')