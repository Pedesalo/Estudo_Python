letra = input("Digite uma letra: ").lower() # .lower() para aceitar "A" ou "a"
vogais = ["a", "e", "i", "o", "u"]

e_vogal = False
for n in range(len(vogais)):
    if vogais[n] == letra:
        print(f"{letra} é uma vogal")
        e_vogal = True
        break

if not e_vogal:
    print(f"{letra} é uma consoante")