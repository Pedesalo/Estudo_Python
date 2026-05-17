import customtkinter as ctk

# Configuração inicial do tema e cor
ctk.set_appearance_mode("System")  # Opções: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Opções: "blue", "green", "dark-blue"


def clique_botao():
    # Função que será executada quando o botão for clicado
    texto_digitado = caixa_entrada.get()
    label_resultado.configure(text=f"Olá, {texto_digitado}!")


# 1. Criar a janela principal
janela = ctk.CTk()
janela.title("Exemplo Simples CustomTkinter")
janela.geometry("400x300")

# 2. Criar a Label (Etiqueta)
label_resultado = ctk.CTkLabel(
    janela, text="Digite seu nome abaixo:", font=("Arial", 16)
)
label_resultado.pack(pady=20)

# 3. Criar a Caixa de Entrada (Entry)
caixa_entrada = ctk.CTkEntry(
    janela, placeholder_text="Seu nome aqui...", width=200
)
caixa_entrada.pack(pady=10)

# 4. Criar o Botão
botao = ctk.CTkButton(janela, text="Enviar", command=clique_botao)
botao.pack(pady=20)

# Executar o loop principal da interface
janela.mainloop()