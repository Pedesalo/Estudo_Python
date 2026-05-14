import customtkinter as ctk

# Configurações de aparência
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

def acao_botao():
    produto = {"nome": "teclado gamer", "preço": 250.00}
    nome_formatado = produto["nome"].capitalize()
    label.configure(text=f"{nome_formatado} selecionado!")

# Criando a janela principal
janela = ctk.CTk()
janela.geometry("400x240")
janela.title("Minha Primeira Interface")

# Adicionando elementos (Widgets)
label = ctk.CTkLabel(janela, text="Bem-vindo ao Python!", font=("Roboto", 20))
label.pack(pady=20)

botao = ctk.CTkButton(janela, text="Clique Aqui", command=acao_botao)
botao.pack(pady=10)

# Iniciando o programa
janela.mainloop()