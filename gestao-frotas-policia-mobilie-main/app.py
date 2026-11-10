import flet as ft


def main(page: ft.Page):
    page.title = "PMSC Operacional - Login"
    page.window.width = 400
    page.window.height = 740
    page.window.resizable = False
    page.window.maximized = False
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

    txt_erro = ft.Text(
        "",
        color="red",
        size=12,
        weight=ft.FontWeight.BOLD
    )

    # Tela principal criada antes das funções
    tela_principal = ft.Column(
        controls=[],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    def mostrar_pagina(titulo, descricao, icone):
        tela_principal.controls = [
            ft.Container(
                margin=ft.Margin(0, 20, 0, 0),
                padding=20,
                bgcolor="white",
                border_radius=15,
                width=370,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=12,
                    controls=[
                        ft.Icon(
                            icon=icone,
                            size=40,
                            color="#1A252F"
                        ),
                        ft.Text(
                            titulo,
                            size=18,
                            color="#1A252F",
                            weight=ft.FontWeight.BOLD
                        ),
                        ft.Text(
                            descricao,
                            size=12,
                            color="grey700",
                            text_align=ft.TextAlign.CENTER
                        )
                    ]
                )
            )
        ]
        page.update()

    def navegar_paginas(e):
        pagina = e.control.selected_index

        if pagina == 0:
            mostrar_pagina(
                "Check-list",
                "Área de checklist operacional.",
                ft.Icons.CHECKLIST
            )

        elif pagina == 1:
            mudar_para_dashboard()

        elif pagina == 2:
            mostrar_pagina(
                "Viaturas",
                "Área de gerenciamento de viaturas.",
                ft.Icons.DIRECTIONS_CAR
            )

    # Navegação inferior
    navigation_bar = ft.NavigationBar(
        selected_index=1,
        bgcolor="white",
        indicator_color="#f5dede",
        on_change=navegar_paginas,
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icons.CHECKLIST_OUTLINED,
                selected_icon=ft.Icons.CHECKLIST,
                label="Check-list",
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.HOME_OUTLINED,
                selected_icon=ft.Icons.HOME,
                label="Página inicial",
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.DIRECTIONS_CAR_OUTLINED,
                selected_icon=ft.Icons.DIRECTIONS_CAR,
                label="Viaturas",
            ),
        ],
    )

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

        page.navigation_bar = navigation_bar
        navigation_bar.selected_index = 1

        # Segunda tela (inicial)
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
                                                            content=ft.Text(
                                                                "10º BPM",
                                                                size=10,
                                                                color="grey700",
                                                                weight=ft.FontWeight.W_500
                                                            ),
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
                                ft.Icon(
                                    icon=ft.Icons.CHECK_CIRCLE_OUTLINED,
                                    color="grey600",
                                    size=18
                                )
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
                                        ft.Text(
                                            "Turno: ",
                                            size=12,
                                            color="grey700",
                                            weight=ft.FontWeight.BOLD
                                        ),
                                        ft.Text(
                                            "Aguardando Checklist de Abertura",
                                            size=12,
                                            color="#7B341E",
                                            weight=ft.FontWeight.W_500
                                        )
                                    ]
                                ),
                                ft.Container(
                                    content=ft.Text(
                                        "Pendente",
                                        size=10,
                                        color="#7B341E",
                                        weight=ft.FontWeight.BOLD
                                    ),
                                    bgcolor="#FEF3C7",
                                    padding=6,
                                    border_radius=12
                                )
                            ]
                        )
                    ]
                )
            ),

            # Card vermelho
            ft.Container(
                margin=ft.Margin(0, 12, 0, 0),
                padding=12,
                bgcolor="#B70F33",
                border_radius=16,
                width=368,
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Row(
                            spacing=12,
                            controls=[
                                ft.Container(
                                    width=46,
                                    height=46,
                                    bgcolor="white10",
                                    border_radius=12,
                                    alignment=ft.Alignment.CENTER,
                                    border=ft.Border(
                                        top=ft.BorderSide(1, "white24"),
                                        bottom=ft.BorderSide(1, "white24"),
                                        left=ft.BorderSide(1, "white24"),
                                        right=ft.BorderSide(1, "white24")
                                    ),
                                    content=ft.Icon(
                                        icon=ft.Icons.ASSIGNMENT_TURNED_IN_OUTLINED,
                                        color="white",
                                        size=20
                                    )
                                ),

                                ft.Column(
                                    spacing=2,
                                    controls=[
                                        ft.Text(
                                            "AÇÃO OBRIGATÓRIA",
                                            size=11,
                                            color="white70",
                                            weight=ft.FontWeight.W_500
                                        ),
                                        ft.Text(
                                            "Iniciar Checklist de Turno",
                                            size=14,
                                            color="white",
                                            weight=ft.FontWeight.BOLD
                                        ),
                                    ]
                                )
                            ]
                        ),
                        ft.Container(
                            width=36,
                            height=36,
                            bgcolor="white10",
                            shape=ft.BoxShape.CIRCLE,
                            alignment=ft.Alignment.CENTER,
                            content=ft.Icon(
                                icon=ft.Icons.ARROW_FORWARD,
                                color="white",
                                size=16
                            )
                        )
                    ]
                )
            ),

            ft.Column(
                width=340,
                spacing=12,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Row(
                                spacing=6,
                                controls=[
                                    ft.Icon(
                                        icon=ft.Icons.ANALYTICS_OUTLINED,
                                        color="white",
                                        size=16
                                    ),
                                    ft.Text(
                                        "SITUAÇÃO DA FROTA HOJE",
                                        size=12,
                                        weight=ft.FontWeight.BOLD,
                                        color="white",
                                    ),
                                ]
                            ),
                            ft.Text(
                                "Atualizado agora",
                                size=11,
                                color="grey600"
                            )
                        ]
                    ),

                    # Linha dos 2 cards
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        spacing=10,
                        controls=[
                            ft.Container(
                                bgcolor="white",
                                border_radius=16,
                                padding=12,
                                expand=True,
                                border=ft.Border(
                                    top=ft.BorderSide(1, "#E2E8F0"),
                                    bottom=ft.BorderSide(1, "#E2E8F0"),
                                    left=ft.BorderSide(1, "#E2E8F0"),
                                    right=ft.BorderSide(1, "#E2E8F0"),
                                ),
                                content=ft.Column(
                                    spacing=6,
                                    controls=[
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                            controls=[
                                                ft.Text(
                                                    "Sua Viatura Recente",
                                                    size=10,
                                                    color="grey600",
                                                    weight=ft.FontWeight.W_500
                                                ),
                                                ft.Container(
                                                    content=ft.Icon(
                                                        icon=ft.Icons.DIRECTIONS_CAR_OUTLINED,
                                                        color="#10B981",
                                                        size=14
                                                    ),
                                                    bgcolor="#E6F4EA",
                                                    padding=4,
                                                    border_radius=6,
                                                )
                                            ]
                                        ),
                                        ft.Text(
                                            "M-0124",
                                            size=18,
                                            weight=ft.FontWeight.BOLD,
                                            color="#1A252F"
                                        ),
                                        ft.Text(
                                            "Renault Duster • 45.210 km",
                                            size=10,
                                            color="grey600"
                                        ),
                                        ft.Divider(height=10, color="#F1F5F9"),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                            controls=[
                                                ft.Text(
                                                    "Status",
                                                    size=10,
                                                    color="grey500"
                                                ),
                                                ft.Container(
                                                    content=ft.Row(
                                                        spacing=4,
                                                        controls=[
                                                            ft.Text(
                                                                "●",
                                                                color="#10B981",
                                                                size=8
                                                            ),
                                                            ft.Text(
                                                                "Operacional",
                                                                size=9,
                                                                color="#10B981",
                                                                weight=ft.FontWeight.BOLD
                                                            ),
                                                        ],
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                    ),
                                                    bgcolor="#E6F4EA",
                                                    padding=4,
                                                    border_radius=12,
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ),

                            ft.Container(
                                bgcolor="white",
                                border_radius=16,
                                padding=12,
                                expand=True,
                                border=ft.Border(
                                    top=ft.BorderSide(1, "#E2E8F0"),
                                    bottom=ft.BorderSide(1, "#E2E8F0"),
                                    left=ft.BorderSide(1, "#E2E8F0"),
                                    right=ft.BorderSide(1, "#E2E8F0"),
                                ),
                                content=ft.Column(
                                    spacing=6,
                                    controls=[
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                            controls=[
                                                ft.Text(
                                                    "Último Alerta",
                                                    size=10,
                                                    color="grey600",
                                                    weight=ft.FontWeight.W_500
                                                ),
                                                ft.Container(
                                                    content=ft.Icon(
                                                        icon=ft.Icons.WARNING_AMBER_ROUNDED,
                                                        color="#D97706",
                                                        size=14
                                                    ),
                                                    bgcolor="#FEF3C7",
                                                    padding=4,
                                                    border_radius=6,
                                                )
                                            ]
                                        ),
                                        ft.Text(
                                            "RP-09",
                                            size=18,
                                            weight=ft.FontWeight.BOLD,
                                            color="#1A252F"
                                        ),
                                        ft.Text(
                                            "Óleo Baixo verificado",
                                            size=10,
                                            color="#7B341E",
                                            weight=ft.FontWeight.W_500
                                        ),
                                        ft.Divider(height=10, color="#F1F5F9"),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                            controls=[
                                                ft.Text(
                                                    "Ação",
                                                    size=10,
                                                    color="grey500"
                                                ),
                                                ft.Container(
                                                    content=ft.Row(
                                                        spacing=4,
                                                        controls=[
                                                            ft.Text(
                                                                "●",
                                                                color="#D97706",
                                                                size=8
                                                            ),
                                                            ft.Text(
                                                                "Atenção",
                                                                size=9,
                                                                color="#D97706",
                                                                weight=ft.FontWeight.BOLD
                                                            ),
                                                        ],
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                    ),
                                                    bgcolor="#FEF3C7",
                                                    padding=4,
                                                    border_radius=12,
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ),
                        ]
                    )
                ]
            )
        ]

        page.update()

    def mudar_para_login():
        page.appbar = None
        page.navigation_bar = None
        navigation_bar.selected_index = 1

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
                        ft.Text(
                            "Autenticação de Serviço",
                            color="#1a252f",
                            size=16,
                            weight=ft.FontWeight.BOLD
                        ),
                        ft.Text(
                            "Informe suas credenciais para checklist e escala operacional",
                            color="grey",
                            size=11,
                            text_align=ft.TextAlign.CENTER
                        ),
                    ]
                ),
                ft.Column(
                    controls=[
                        ft.Text(
                            "MATRÍCULA POLICIAL",
                            color="#1a252f",
                            size=10,
                            weight=ft.FontWeight.BOLD
                        ),
                        txt_matricula
                    ],
                    spacing=4
                ),
                ft.Column(
                    controls=[
                        ft.Text(
                            "SENHA / PIN DE ACESSO",
                            color="#1a252f",
                            size=10,
                            weight=ft.FontWeight.BOLD
                        ),
                        txt_senha
                    ],
                    spacing=4
                ),
                txt_erro,
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Icon(
                                ft.Icons.GPP_GOOD,
                                color="grey700",
                                size=18
                            ),
                            ft.Container(
                                content=ft.Text(
                                    "Ambiente seguro conectado à rede interna do 10º BPM.",
                                    color="grey700",
                                    size=10
                                ),
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
                                ft.Icon(
                                    ft.Icons.SHIELD_OUTLINED,
                                    size=16
                                ),
                                ft.Text(
                                    "Entrar no Turno",
                                    weight=ft.FontWeight.BOLD
                                ),
                                ft.Icon(
                                    ft.Icons.ARROW_FORWARD,
                                    size=16
                                ),
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
                            ft.Icon(
                                ft.Icons.SUPPORT_AGENT,
                                color="grey600",
                                size=14
                            ),
                            ft.Text(
                                "Suporte Técnico Operacional (Helpdesk)",
                                color="grey600",
                                size=11
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=5
                    )
                )
            ]
        )
    )

    # Tela inicial de login
    tela_principal.controls = [
        header_title,
        ft.Divider(height=16, color="transparent"),
        card_content
    ]

    page.add(tela_principal)


ft.run(main)