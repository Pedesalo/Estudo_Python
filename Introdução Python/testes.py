# --- Desafio 6 (Estatísticas) ---
# 1. Crie uma lista com 5 notas de alunos (números com ponto flutuante).
nota = [4.0,5.5,9.5,8.5,10.0]
# 2. Calcule a média: some todos os elementos (sum) e divida pelo total (len).
media = sum(nota)/len(nota)
# 3. Descubra a maior nota da lista usando a função max().
maior = max(nota)
# 4. Descubra a menor nota da lista usando a função min().
menor = min(nota)
# 5. Imprima a média, a maior e a menor nota na tela.
print(f'A média das notas é: {media}. A maior nota é: {maior}. A menor nota é: {menor}')