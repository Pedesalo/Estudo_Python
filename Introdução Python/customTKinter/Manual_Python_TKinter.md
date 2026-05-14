Com certeza! Como sou uma IA, não consigo "enviar" um arquivo físico diretamente para o seu disco rígido, mas eu gerei abaixo o conteúdo completo formatado em Markdown.

Como salvar:

    Abra o seu editor de texto (VS Code, Gedit ou Bloco de Notas).

    Copie o conteúdo abaixo.

    Salve o arquivo com o nome Manual_Python.md.

Markdown

# 📘 Manual de Estudos: Python, Dicionários e Interfaces

Este guia consolida os aprendizados sobre manipulação de dados, tratamento de erros e a criação de interfaces modernas com **CustomTkinter**, baseado no tutorial do canal *Dev Aprender*.

---

## 1. Configuração do Ambiente no Linux
Devido à proteção de pacotes do sistema (PEP 668), utilize sempre um ambiente virtual:

```bash
# 1. Criar o ambiente virtual
python3 -m venv venv

# 2. Ativar o ambiente
source venv/bin/activate

# 3. Instalar a biblioteca de interface
pip install customtkinter

2. Estrutura de Dados: Dicionários

Dicionários mapeiam chaves para valores. São ideais para representar objetos (produtos, usuários).

    Criação: produto = {"nome": "mouse", "preco": 80.0}

    Acesso Seguro: produto.get("estoque", 0) (retorna 0 se a chave não existir).

    Formatação de Texto: nome.capitalize() (Primeira letra maiúscula).

    Formatação de Números: f"R${valor:.2f}" (Força duas casas decimais).

3. Tratamento de Erros (try/except)

Evita que o programa pare de funcionar ao encontrar um erro inesperado.
Python

try:
    # Código que pode falhar
    preco = float(input("Digite o valor: "))
except ValueError:
    # Código executado em caso de erro
    print("Erro: Por favor, digite apenas números.")

4. Interfaces com CustomTkinter (Guia do Vídeo)
O Ciclo de 5 Passos:

    Importação: import customtkinter as ctk.

    Aparência: Definir tema Dark/Light e cores.

    Janela Principal: Criar o objeto ctk.CTk() e definir título/tamanho.

    Widgets (Elementos):

        CTkLabel: Textos e títulos.

        CTkEntry: Campos de entrada (use show="*" para senhas).

        CTkButton: Botões de ação.

    Mainloop: Iniciar o programa com app.mainloop().

Métodos Chave:

    .get(): Captura o que foi digitado no campo.

    .pack(pady=10): Posiciona o elemento na tela com espaçamento.

    .configure(text="Novo Texto"): Atualiza um elemento sem recriá-lo.

5. Script de Exemplo Completo

Este código une todos os conceitos aprendidos:
Python

import customtkinter as ctk

def acao_principal():
    produto = {"nome": "monitor", "preco": 1200.00}
    try:
        nome_formatado = produto["nome"].capitalize()
        valor_desconto = produto["preco"] * 0.9
        resultado = f"{nome_formatado} por apenas R${valor_desconto:.2f}"
        label_resultado.configure(text=resultado, text_color="green")
    except Exception as e:
        label_resultado.configure(text=f"Erro no sistema", text_color="red")

app = ctk.CTk()
app.title("Meu Manual App")
app.geometry("400x250")

ctk.CTkLabel(app, text="Consultor de Descontos", font=("Arial", 20)).pack(pady=20)
ctk.CTkButton(app, text="Calcular Preço", command=acao_principal).pack(pady=10)
label_resultado = ctk.CTkLabel(app, text="")
label_resultado.pack(pady=20)

app.mainloop()

Manual gerado para Claus - Estudos de Python 2026


---

**Dica Profissional:** Se você instalar a extensão "Markdown Preview" no seu VS Code, poderá ver esse arquivo com uma formatação visual incrível (tabelas, negritos e cores) enquanto estuda!