import flet as ft


def main(page: ft.Page):
    page.title = "PMSC Operacional - Login"
    page.window_width = 360
    page.window_height = 740
    page.window_resizable = False
    page.window_maximized = False
    page.scroll = ft.ScrollMode.AUTO

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 16
    page.bgcolor = "#1E293B"

    txt_matricula = ft.TextField(
        hint_text="Ex: 923.456-7",
        prefix_icon=ft.Icons.BADGE,
        border_radius=ft.BorderRadius.all(8),
        border_color=ft.Colors.GREY_400,
        height=48,
        text_size=14,
    )

    txt_senha = ft.TextField(
        hint_text="********",
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK,
        border_radius=ft.BorderRadius.all(8),
        border_color=ft.Colors.GREY_400,
        height=48,
        text_size=14,
    )

    txt_erro = ft.Text("", color="red", size=12, weight=ft.FontWeight.BOLD)


    def mudar_para_dashboard():
        page.appbar = ft.AppBar(
            leading=ft.Container(
                content=ft.Image(
                    src="logo.png",
                ),
                padding=6,
            ),
            leading_width=50,
            title=ft.Text(
                "PMSC Operacional",
                color="white",
                size=16,
                weight=ft.FontWeight.BOLD
            ),
            bgcolor="#111c24",
            center_title=False,
            actions=[
                ft.IconButton(
                    icon=ft.Icons.LOGOUT,
                    icon_color="white",
                    on_click=lambda _: mudar_para_login()
                )
            ]
        )
        # segunda tela (inicial)
        tela_principal.controls = [
            ft.Container(
                margin=ft.Margin(0, 20, 0, 0),
                padding=16,
                bgcolor="white",
                border_radius=15,
                width=370,
                border=ft.Border(
                    top=ft.BorderSide(width=4, color="#1e7e34")
                ),
                content=ft.Column(
                    controls=[
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Row(
                                    spacing=10,
                                    controls=[
                                        ft.Container(
                                            width=46,
                                            height=46,
                                            bgcolor="#1A252F",
                                            border_radius=12,
                                            alignment=ft.Alignment.CENTER,
                                            content=ft.Text(
                                                "JS" if txt_matricula.value == "342.910-2" else "PM",
                                                color="white",
                                                weight=ft.FontWeight.BOLD,
                                                size=14
                                            )
                                        ),
                                        ft.Column(
                                            spacing=2,
                                            controls=[
                                                ft.Row(
                                                    spacing=6,
                                                    controls=[
                                                        ft.Text(
                                                            "Cb. Jefferson Silva" if txt_matricula.value == "342.910-2" else "Policial Militar",
                                                            size=14,
                                                            weight=ft.FontWeight.BOLD,
                                                            color="#1A252F"
                                                        ),
                                                        ft.Container(
                                                            content=ft.Text("10º BPM", size=10, color="grey700",
                                                                            weight=ft.FontWeight.W_500),
                                                            bgcolor="#E2E8F0",
                                                            padding=4,
                                                            border_radius=4
                                                        )
                                                    ]
                                                ),
                                                ft.Text(
                                                    f"Matrícula: {txt_matricula.value if txt_matricula.value else 'Não informada'}",
                                                    size=12,
                                                    color="grey600"
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                ft.Icon(icon=ft.Icons.CHECK_CIRCLE_OUTLINED, color="grey600", size=18)
                            ]
                        ),

                        ft.Divider(height=16, color="#E2E8F0"),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Row(
                                    spacing=6,
                                    controls=[
                                        ft.Text("●", color="#F59E0B", size=14),
                                        ft.Text("Turno: ", size=12, color="grey700", weight=ft.FontWeight.BOLD),
                                        ft.Text("Aguardando Checklist de Abertura", size=12, color="#7B341E",
                                                weight=ft.FontWeight.W_500)
                                    ]
                                ),
                                ft.Container(
                                    content=ft.Text("Pendente", size=10, color="#7B341E", weight=ft.FontWeight.BOLD),
                                    bgcolor="#FEF3C7",
                                    padding=6,
                                    border_radius=12
                                )
                            ]
                        )
                    ]
                )
            )
        ]
        page.update()

    def mudar_para_login():
        page.appbar = None
        txt_matricula.value = ""
        txt_senha.value = ""
        txt_erro.value = ""
        tela_principal.controls = [
            header_title,
            ft.Divider(height=16, color="transparent"),
            card_content
        ]
        page.update()

    def efetuar_login(e):
        matricula = txt_matricula.value
        senha = txt_senha.value

        if not matricula or not senha:
            txt_erro.value = "Por favor, preencha todos os campos!"
            page.update()
        else:
            txt_erro.value = ""
            mudar_para_dashboard()

    header_title = ft.Column(
        controls=[
            ft.Image(
                src="logo.png",
                width=120,
                fit="contain",
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    card_content = ft.Container(
        bgcolor="white",
        border_radius=20,
        padding=20,
        width=320,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=18,
            controls=[
                ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=5,
                    controls=[
                        ft.Text("Autenticação de Serviço", color="#1a252f", size=16, weight=ft.FontWeight.BOLD),
                        ft.Text("Informe suas credenciais para checklist e escala operacional", color="grey", size=11,
                                text_align=ft.TextAlign.CENTER),
                    ]
                ),
                ft.Column(
                    controls=[
                        ft.Text("MATRÍCULA POLICIAL", color="#1a252f", size=10, weight=ft.FontWeight.BOLD),
                        txt_matricula
                    ],
                    spacing=4
                ),
                ft.Column(
                    controls=[
                        ft.Text("SENHA / PIN DE ACESSO", color="#1a252f", size=10, weight=ft.FontWeight.BOLD),
                        txt_senha
                    ],
                    spacing=4
                ),
                txt_erro,
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.GPP_GOOD, color="grey700", size=18),
                            ft.Container(
                                content=ft.Text("Ambiente seguro conectado à rede interna do 10º BPM.", color="grey700",
                                                size=10),
                                expand=True
                            )
                        ]
                    ),
                    bgcolor="#f5f6f8",
                    padding=10,
                    border_radius=8,
                ),
                ft.Container(
                    content=ft.Button(
                        content=ft.Row(
                            controls=[
                                ft.Icon(ft.Icons.SHIELD_OUTLINED, size=16),
                                ft.Text("Entrar no Turno", weight=ft.FontWeight.BOLD),
                                ft.Icon(ft.Icons.ARROW_FORWARD, size=16),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        style=ft.ButtonStyle(
                            bgcolor="#c0392b",
                            color="white",
                            shape=ft.RoundedRectangleBorder(radius=10),
                        ),
                        height=48,
                        on_click=efetuar_login,
                    ),
                    width=float("inf"),
                ),
                ft.TextButton(
                    content=ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.SUPPORT_AGENT, color="grey600", size=14),
                            ft.Text("Suporte Técnico Operacional (Helpdesk)", color="grey600", size=11)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=5
                    )
                )
            ]
        )
    )

    tela_principal = ft.Column(
        controls=[
            header_title,
            ft.Divider(height=16, color="trans7parent"),
            card_content
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    page.add(tela_principal)


ft.run(main)
