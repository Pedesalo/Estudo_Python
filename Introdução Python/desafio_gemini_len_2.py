# =================================================================
# ATIVIDADE DE PRÁTICA EM PYTHON
# Instruções: Desenvolva o código logo abaixo de cada comentário.
# =================================================================

# --- NÍVEL 1: BÁSICO (Variáveis e Operações) ---

# EXERCÍCIO 1: 
# Crie uma variável 'nome', uma 'idade' e uma 'cidade'.
nome = "Claus"
idade = 18
cidade = "Rio de Janeiro"

# Imprima uma frase formatada usando f-string: "Olá, meu nome é [nome], tenho [idade] anos e moro em [cidade]."
print(f"Olá, meu nome é {nome}, tenho {idade} anos e moro em {cidade}.")


# EXERCÍCIO 2:
# Receba dois números do usuário (lembre-se do input e de converter para float).
n1 = float(input("Escreva um número: "))
n2 = float(input("Escreva um sergundo número: "))

# Calcule e exiba a soma, subtração, multiplicação e a potência do primeiro pelo segundo.
print(f"{n1} + {n2} = {n1+n2}")
print(f"{n1} - {n2} = {n1-n2}")
print(f"{n1} x {n2} = {n1*n2}")
print(f"{n1} elevado a {n2} = {n1**n2}")

# --- NÍVEL 2: ESTRUTURAS DE DECISÃO (If/Else) ---

# EXERCÍCIO 3:
# Peça a nota de um aluno. 
nota = float(input("Escreva a nota do aluno: "))
# Se for maior ou igual a 7, imprima "Aprovado".
if nota >= 7:
    print("Aprovado")
# Se estiver entre 5 e 6.9, imprima "Recuperação".
if 5 <= nota <= 6.9:
    print("Recuperação")
# Se for menor que 5, imprima "Reprovado".
if nota <= 4.9: 
    print("Reprovado")


# --- NÍVEL 3: ESTRUTURAS DE REPETIÇÃO (Loops) ---

# EXERCÍCIO 4:
# Use um laço 'for' para imprimir todos os números pares de 1 a 20.
for i in range(1,21):
    print(i)

# EXERCÍCIO 5:
# Crie um laço 'while' que peça uma senha ao usuário.
# O laço só deve parar quando a senha digitada for "python123".
# Quando acertar, exiba "Acesso Concedido".
while True:
    senha = input("digite a senha correta: ")

    if senha == "python123":
        break

    print("Senha incorreta, Acesso Negado!")

print("Acesso Concedido")

# --- NÍVEL 4: COLEÇÕES (Listas e Dicionários) ---

# EXERCÍCIO 6:
# Crie uma lista de compras com 5 itens.
itens = ["biscoito","marmita","mela cueca","5","2.6"]
# Adicione um item novo à lista, remova o segundo item e imprima a lista em ordem alfabética.
itens.append("cookie")
itens.pop(1)
itens.sort()
print(itens)


# EXERCÍCIO 7:
# Crie um dicionário para representar um carro (marca, modelo, ano).
carro = {
    "marca": "citroen",
    "modelo": "c3",
    "ano": 1996
}
# Altere o ano do carro e adicione uma nova chave 'cor'. Imprima o dicionário final.
carro["ano"] = 1993
carro["cor"] = "azul"
print(carro)


# --- NÍVEL 5: FUNÇÕES ---

# EXERCÍCIO 8:
# Escreva uma função chamada 'calcular_area' que recebe a base e a altura de um retângulo.
def calcular_area(base,altura):

    area = base*altura

    return area

# A função deve retornar a área. Chame a função e imprima o resultado.
base = int(input("Digite o valor para a base do retangulo: "))
altura = int(input("Digite o valor para a altura do retangulo: "))

area = calcular_area(base, altura)

print(f"A area do retangulo é de {area}")