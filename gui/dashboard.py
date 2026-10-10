import flet as ft

from datos import (
    clientes_registrados,
    mascotas_registradas,
    historial_cuidados,
    recordatorios_registrados
)


def mostrar_dashboard(page: ft.Page):
    page.clean()

    page.title = "Clínica Veterinaria"
    page.padding = 0
    page.bgcolor = "#EAF2FF"

    # Contenedor que cambia de contenido
    contenido = ft.Container(
        expand=True,
        padding=25,
        bgcolor="#EAF2FF"
    )

    # ----------------------------------
    # NAVEGACIÓN ENTRE SECCIONES
    # ----------------------------------

    def abrir_seccion(nombre):
        try:
            if nombre == "Inicio":
                mostrar_inicio()
                return

            secciones = {
                "Clientes": (
                    "gui.clientes",
                    "mostrar_clientes"
                ),
                "Mascotas": (
                    "gui.mascotas",
                    "mostrar_mascotas"
                ),
                "Vacunas": (
                    "gui.vacunas",
                    "mostrar_vacunas"
                ),
                "Desparasitaciones": (
                    "gui.desparasitaciones",
                    "mostrar_desparasitaciones"
                ),
                "Baños": (
                    "gui.banos",
                    "mostrar_banos"
                ),
                "Consultas": (
                    "gui.consultas",
                    "mostrar_consultas"
                ),
                "Historial": (
                    "gui.historial",
                    "mostrar_historial"
                ),
                "Recordatorios": (
                    "gui.recordatorios",
                    "mostrar_recordatorios"
                )
            }

            modulo, funcion = secciones[nombre]

            archivo = __import__(
                modulo,
                fromlist=[funcion]
            )

            mostrar = getattr(archivo, funcion)

            mostrar(contenido)

        except Exception as error:
            contenido.content = ft.Column(
                controls=[
                    ft.Text(
                        f"No se pudo abrir {nombre}",
                        size=25,
                        weight=ft.FontWeight.BOLD,
                        color="#DC2626"
                    ),
                    ft.Text(
                        str(error),
                        color="#475569"
                    )
                ],
                scroll=ft.ScrollMode.AUTO
            )

            contenido.update()

    # ----------------------------------
    # TARJETAS DEL DASHBOARD
    # ----------------------------------

    def crear_tarjeta(titulo, cantidad, color, icono):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon(
                        icono,
                        size=35,
                        color="#FFFFFF"
                    ),
                    ft.Text(
                        str(cantidad),
                        size=32,
                        weight=ft.FontWeight.BOLD,
                        color="#FFFFFF"
                    ),
                    ft.Text(
                        titulo,
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        color="#FFFFFF"
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=8
            ),
            bgcolor=color,
            padding=20,
            border_radius=18,
            expand=True
        )

    # ----------------------------------
    # PANTALLA DE INICIO
    # ----------------------------------

    def mostrar_inicio():
        contenido.content = ft.Column(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "¡Bienvenido al sistema!",
                                size=30,
                                weight=ft.FontWeight.BOLD,
                                color="#FFFFFF"
                            ),
                            ft.Text(
                                "Gestiona los cuidados de tus mascotas.",
                                size=16,
                                color="#DBEAFE"
                            ),
                            ft.Text("🐶  🐱  🐾", size=40)
                        ],
                        spacing=10
                    ),
                    bgcolor="#2563EB",
                    padding=25,
                    border_radius=20
                ),

                ft.Text(
                    "Resumen general",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color="#172554"
                ),

                ft.Row(
                    controls=[
                        crear_tarjeta(
                            "Clientes",
                            len(clientes_registrados),
                            "#2563EB",
                            ft.Icons.PEOPLE
                        ),
                        crear_tarjeta(
                            "Mascotas",
                            len(mascotas_registradas),
                            "#059669",
                            ft.Icons.PETS
                        )
                    ],
                    spacing=15
                ),

                ft.Row(
                    controls=[
                        crear_tarjeta(
                            "Historiales",
                            len(historial_cuidados),
                            "#7C3AED",
                            ft.Icons.HISTORY
                        ),
                        crear_tarjeta(
                            "Recordatorios",
                            len(recordatorios_registrados),
                            "#EA580C",
                            ft.Icons.NOTIFICATIONS
                        )
                    ],
                    spacing=15
                ),

                ft.Text(
                    "Accesos rápidos",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color="#172554"
                ),

                ft.Button(
                    "Registrar clientes",
                    icon=ft.Icons.PEOPLE,
                    bgcolor="#2563EB",
                    color="#FFFFFF",
                    on_click=lambda e: abrir_seccion("Clientes")
                ),

                ft.Button(
                    "Registrar mascotas",
                    icon=ft.Icons.PETS,
                    bgcolor="#059669",
                    color="#FFFFFF",
                    on_click=lambda e: abrir_seccion("Mascotas")
                ),

                ft.Button(
                    "Consultar historial",
                    icon=ft.Icons.HISTORY,
                    bgcolor="#7C3AED",
                    color="#FFFFFF",
                    on_click=lambda e: abrir_seccion("Historial")
                ),

                ft.Button(
                    "Ver recordatorios",
                    icon=ft.Icons.NOTIFICATIONS,
                    bgcolor="#EA580C",
                    color="#FFFFFF",
                    on_click=lambda e: abrir_seccion("Recordatorios")
                )
            ],
            spacing=20,
            scroll=ft.ScrollMode.AUTO
        )

        contenido.update()

    # ----------------------------------
    # OPCIONES DEL MENÚ SUPERIOR
    # ----------------------------------

    opciones = [
        ("Inicio", ft.Icons.HOME),
        ("Clientes", ft.Icons.PEOPLE),
        ("Mascotas", ft.Icons.PETS),
        ("Vacunas", ft.Icons.HEALTH_AND_SAFETY),
        ("Desparasitaciones", ft.Icons.MEDICAL_SERVICES),
        ("Baños", ft.Icons.WATER_DROP),
        ("Consultas", ft.Icons.LOCAL_HOSPITAL),
        ("Historial", ft.Icons.HISTORY),
        ("Recordatorios", ft.Icons.NOTIFICATIONS)
    ]

    botones = []

    for nombre, icono in opciones:
        botones.append(
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Icon(
                            icono,
                            size=23,
                            color="#FFFFFF"
                        ),
                        ft.Text(
                            nombre,
                            size=11,
                            color="#FFFFFF",
                            text_align=ft.TextAlign.CENTER
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=5
                ),
                padding=ft.Padding.symmetric(
                    horizontal=12,
                    vertical=10
                ),
                border_radius=10,
                ink=True,
                on_click=lambda e, n=nombre: abrir_seccion(n)
            )
        )

    # ----------------------------------
    # CERRAR SESIÓN
    # ----------------------------------

    def cerrar_sesion(e):
        from gui.login import mostrar_login
        mostrar_login(page)

    botones.append(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon(
                        ft.Icons.LOGOUT,
                        size=23,
                        color="#FCA5A5"
                    ),
                    ft.Text(
                        "Salir",
                        size=11,
                        color="#FCA5A5"
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=5
            ),
            padding=10,
            ink=True,
            on_click=cerrar_sesion
        )
    )

    # ----------------------------------
    # MENÚ PERMANENTE
    # ----------------------------------

    menu = ft.Container(
        content=ft.Row(
            controls=botones,
            spacing=5,
            scroll=ft.ScrollMode.AUTO
        ),
        bgcolor="#172554",
        padding=8
    )

    # ----------------------------------
    # ENCABEZADO
    # ----------------------------------

    encabezado = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text("🐾", size=35),
                ft.Column(
                    controls=[
                        ft.Text(
                            "CLÍNICA VETERINARIA",
                            size=23,
                            weight=ft.FontWeight.BOLD,
                            color="#172554"
                        ),
                        ft.Text(
                            "Sistema de gestión y cuidado de mascotas",
                            size=13,
                            color="#64748B"
                        )
                    ],
                    spacing=3
                )
            ]
        ),
        bgcolor="#FFFFFF",
        padding=15
    )

    # ----------------------------------
    # ESTRUCTURA PRINCIPAL
    # ----------------------------------

    page.add(
        ft.Column(
            controls=[
                encabezado,
                menu,
                ft.Container(
                    content=contenido,
                    expand=True
                )
            ],
            spacing=0,
            expand=True
        )
    )

    mostrar_inicio()
    page.update()