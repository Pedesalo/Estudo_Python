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