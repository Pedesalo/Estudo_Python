Aqui está o manual de referência rápida e atualizado do Flet. Este documento contém apenas a sintaxe moderna vigente, trazendo os principais comandos, propriedades e suas respectivas finalidades estruturais — sem históricos ou comparações.

📑 Guia de Referência de Comandos: Flet Atual
1. Inicialização e Configuração de Página (ft.Page)
O ponto de partida de qualquer aplicação Flet para configurar a janela e o comportamento global do app.

ft.run(main): Inicializa a aplicação executando a função principal (main).

page.title = "Nome": Define o título da janela ou da aba do navegador.

page.window_width = int / page.window_height = int: Define a largura e a altura da janela em pixels.

page.window_resizable = False: Bloqueia o redimensionamento da janela pelo usuário.

page.bgcolor = "cor_ou_hex": Define a cor de fundo global da página.

page.horizontal_alignment = ft.CrossAxisAlignment.CENTER: Alinha os elementos horizontalmente no centro da página.

page.vertical_alignment = ft.MainAxisAlignment.CENTER: Alinha os elementos verticalmente no centro da página.

page.add(componente): Renderiza e exibe um componente ou layout na tela.

page.launch_url("url"): Abre o link especificado no navegador padrão do sistema.

2. Componentes de Layout (Containers e Organização)
Elementos estruturais para agrupar, espaçar e estilizar blocos de conteúdo.

ft.Container(): Bloco genérico de estilização e posicionamento.

content=...: Recebe o elemento filho que ficará dentro do bloco.

width=int / height=int: Define dimensões fixas para o bloco.

padding=int: Aplica espaçamento interno uniforme (ex: padding=20).

margin=int: Aplica margem externa uniforme (ex: margin=10).

bgcolor="cor": Define a cor de fundo do container.

border_radius=int: Arredonda os cantos do bloco.

ink=True: Ativa o efeito visual de onda (Ripple) quando o elemento recebe cliques.

expand=True: Faz o container se expandir para preencher todo o espaço disponível na tela.

ft.Column(): Organiza os elementos filhos em uma pilha vertical (um abaixo do outro).

ft.Row(): Organiza os elementos filhos em uma linha horizontal (um ao lado do outro).

ft.Divider(height=int, color="cor"): Cria uma linha divisória horizontal para separação de blocos.

3. Componentes de Conteúdo (Texto, Ícones e Mídia)
Elementos visuais para exibir informações, identidades e mídias para o usuário.

ft.Text(): Exibe um bloco de texto na interface.

value="Texto": O conteúdo textual a ser exibido.

size=int: O tamanho da fonte.

weight=ft.FontWeight.BOLD: Define a intensidade da fonte (valores comuns: BOLD, W_600, NORMAL).

color="cor": Define a cor do texto.

text_align=ft.TextAlign.CENTER: Alinha o texto dentro do seu próprio bloco (ex: CENTER, LEFT, RIGHT).

ft.Icon(): Exibe um ícone vetorial da biblioteca nativa.

name=ft.Icons.NOME: Define qual ícone carregar (ex: ft.Icons.CODE, ft.Icons.BUSINESS).

color="cor": Define a cor de preenchimento do ícone.

size=int: Define o tamanho do ícone em pixels.

ft.CircleAvatar(): Exibe um elemento circular, ideal para fotos de perfil.

foreground_image_src="url": Define o endereço da imagem da internet ou arquivo local para preencher o círculo.

radius=int: Define o raio (tamanho) do círculo.

4. Efeitos Visuais e Interatividade
Propriedades aplicadas a componentes para gerenciar estados, interações do usuário e design avançado.

ft.BoxShadow(): Aplica uma sombra projetada sob o componente.

blur_radius=int: Intensidade do esfumaçado da sombra.

spread_radius=int: O quanto a sombra se espalha além dos limites do bloco.

color="cor": A cor e opacidade da sombra.

on_click=lambda e: função: Evento disparado quando o usuário clica ou toca no componente.

on_hover=lambda e: função: Evento disparado quando o cursor do mouse entra ou sai da área do componente.

e.control.update(): Atualiza dinamicamente as propriedades visuais de um componente específico após uma mudança de estado (utilizado dentro de funções de evento).

5. Código Limpo Consolidado (Gabarito de Produção)
Abaixo está a aplicação prática de todos os comandos listados, estruturados na arquitetura atualizada para um aplicativo de cartões de links:

Python
import flet as ft

def main(page: ft.Page):
    # Configuração de Janela
    page.title = "Social Hub Mobile"
    page.window_width = 380
    page.window_height = 700
    page.window_resizable = False
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#0F172A" 

    # Gerenciador de Evento (Hover)
    def atualizar_hover(e):
        e.control.bgcolor = "#334155" if e.data == "true" else "#1E293B"
        e.control.update()

    # Fábrica de Botões Sociais Interativos
    def criar_botao_social(texto, url, cor_icone, icone):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(icone, color=cor_icone, size=28),
                    ft.Text(texto, size=16, weight=ft.FontWeight.W_600, color="#F8FAFC"),
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=20,
            ),
            margin=10,        
            padding=15,       
            border_radius=12,
            bgcolor="#1E293B",  
            ink=True,  
            on_click=lambda e: page.launch_url(url),
            on_hover=lambda e: atualizar_hover(e)
        )

    # Componentes Visuais
    avatar = ft.CircleAvatar(
        foreground_image_src="https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=150",
        radius=50,
    )
    
    nome_usuario = ft.Text("@seu_usuario", size=22, weight=ft.FontWeight.BOLD, color="#F8FAFC")
    bio = ft.Text("Desenvolvedor Mobile", size=14, color="#94A3B8", text_align=ft.TextAlign.CENTER)

    # Container Estrutural (Mockup do Smartphone)
    mockup_celular = ft.Container(
        width=350,
        height=640,
        bgcolor="#111827",
        border_radius=30,
        shadow=ft.BoxShadow(blur_radius=10, color="#334155", spread_radius=1),
        padding=25, 
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                # Topo do Celular (Notch)
                ft.Row([ft.Container(width=60, height=5, bgcolor="#334155", border_radius=10)], alignment=ft.MainAxisAlignment.CENTER), 
                ft.Divider(height=10, color="transparent"),
                
                # Seção de Perfil
                avatar,
                ft.Divider(height=5, color="transparent"),
                nome_usuario,
                bio,
                ft.Divider(height=20, color="#334155"),
                
                # Links Atuais
                criar_botao_social("Instagram", "https://instagram.com", "#E1306C", ft.Icons.CAMERA_ALT),
                criar_botao_social("LinkedIn", "https://linkedin.com", "#0077B5", ft.Icons.BUSINESS),
                criar_botao_social("GitHub", "https://github.com", "#FFFFFF", ft.Icons.CODE),
                
                # Espaçador Dinâmico Atual
                ft.Container(expand=True),
                
                # Rodapé do App
                ft.Text("Criado com Flet 💜", size=11, color="#64748B")
            ]
        )
    )

    page.add(mockup_celular)

if __name__ == "__main__":
    ft.run(main)