# Lista de temperaturas (da segunda-feira passada até domingo)
temperaturas = [28.5, 30.1, 29.0, 32.4, 26.8, 25.0, 27.3]
dias = {"Segunda":0,"Terça":1,"Quarta":2,"Quinta":3,"Sexta":4,"Sábado":5,"Domingo":6}

# --- SEU OBJETIVO ---
# 1. Acesse e imprima a temperatura de quarta-feira (quarto elemento).
print(f"Temperatura de Quarta-Feira é {temperaturas[dias['Quarta']]}")
# 2. Acesse e imprima a temperatura do último dia (domingo) usando índice negativo.
print(f'Temperaduta de Domingo é {temperaturas[-6]}')
# 3. Extraia uma sublista apenas com os dias do fim de semana (sexta, sábado e domingo).
print(f'As Temperaturas de Sexta-feira até Domingo serão: {temperaturas[4:7]}')

# --- COMENTÁRIO GUIA (Siga estes passos):
# Passo 1: Lembre-se que o Python começa a contar os índices do 0. Então, segunda é 0, terça é 1...
# Passo 2: Para pegar o último elemento direto, use o índice [-1].
# Passo 3: No fatiamento [inicio:fim], o índice de 'fim' não é incluído. Descubra onde começa a sexta-feira e vá até o final.