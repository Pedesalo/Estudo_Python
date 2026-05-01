# =================================================================
# MARATONA PYTHON: 20 EXERCÍCIOS DE FIXAÇÃO
# =================================================================

# --- BÁSICO: VARIÁVEIS E ARITMÉTICA ---

# 1. Crie uma variável para o raio de um círculo e calcule a área (Area = 3.14 * raio^2).
# 2. Receba um valor em Reais e converta para Dólares (considere a cotação de 5.00).
# 3. Peça dois números e exiba o resto da divisão entre eles (operador %).
# 4. Receba uma palavra e exiba quantas letras ela tem (use len).
# 5. Crie uma variável frase e converta-a toda para MAIÚSCULAS (metodo .upper()).

# --- INTERMEDIÁRIO: DECISÃO E LÓGICA ---

# 6. Peça um número e diga se ele é PAR ou ÍMPAR.

n1 = int(input("digite um número inteiro: "))
if n1 % 2 == 0:
    resultado = "par"
else:
    resultado = "ímpar"
print(resultado)


# 7. Receba a idade de uma pessoa e diga se ela é "Criança", "Adolescente" ou "Adulto".

idade = int(input("Escreva sua idade: "))

if idade < 13:
    resultado = "Criança"
elif idade < 18:
    resultado = "Adolecente"
elif idade >= 18:
    resultado = "Adulto"
print(resultado)
    
# 8. Peça dois números e mostre qual é o maior.

n1 = float(input("digite um primeiro número: "))
n2 = float(input("digite um segundo número: "))

numeros = [n1,n2]
resultado = int(max(numeros))
print(f"O maior número digitado foi: {resultado}")

# 9. Verifique se uma letra digitada é Vogal ou Consoante.
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

# 10. Simule um semáforo: peça uma cor. Se "Verde", siga; "Amarelo", atenção; "Vermelho", pare.
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
# --- REPETIÇÃO: LOOPS (FOR/WHILE) ---

# 11. Imprima a tabuada do 5 (do 1 ao 10) usando um laço 'for'.
# 12. Use um laço 'while' para somar números digitados pelo usuário até que ele digite 0.
# 13. Crie uma lista de nomes e use um 'for' para imprimir cada nome com "Olá, [nome]!".
# 14. Faça um programa que conte de 10 até 0 (contagem regressiva).
# 15. Dada a lista [10, 20, 30, 40, 50], use um loop para calcular a média dos valores.

# --- AVANÇADO: COLEÇÕES E FUNÇÕES ---

# 16. Crie uma lista de 5 números, ordene-os e exiba o menor e o maior valor.
# 17. Crie um dicionário 'produto' com nome e preço. Aplique 10% de desconto e exiba o novo preço.
# 18. Escreva uma função que receba um nome e retorne "Bom dia, [nome]".
# 19. Escreva uma função que verifique se um número é positivo ou negativo (retorne True ou False).

# --- O DESAFIO FINAL ---

# 20. Crie um programa que use 'try/except' para pedir um número ao usuário. 
# Se ele digitar uma letra em vez de número, exiba uma mensagem de erro amigável.