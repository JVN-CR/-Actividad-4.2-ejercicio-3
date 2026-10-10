import flet as ft


def mostrar_login(page: ft.Page):
    page.clean()
    page.bgcolor = "#DBEAFE"
    page.padding = 0

    intentos = 0

    usuario = ft.TextField(
        label="Usuario",
        width=320,
        prefix_icon=ft.Icons.PERSON,
        border_radius=12,
        bgcolor="#FFFFFF"
    )

    contrasena = ft.TextField(
        label="Contraseña",
        width=320,
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK,
        border_radius=12,
        bgcolor="#FFFFFF"
    )

    mensaje = ft.Text("", color="#DC2626")
    contador = ft.Text(
        "Intentos disponibles: 3",
        color="#475569"
    )

    def iniciar_sesion(e):
        nonlocal intentos

        if usuario.value == "admin" and contrasena.value == "1234":
            from gui.dashboard import mostrar_dashboard
            mostrar_dashboard(page)

        else:
            intentos += 1
            restantes = 3 - intentos

            if restantes > 0:
                mensaje.value = "Usuario o contraseña incorrectos."
                contador.value = f"Intentos disponibles: {restantes}"

            else:
                mensaje.value = "Acceso bloqueado por superar los intentos."
                boton.disabled = True
                usuario.disabled = True
                contrasena.disabled = True

            page.update()

    boton = ft.Button(
        "Iniciar sesión",
        width=320,
        height=48,
        bgcolor="#2563EB",
        color="#FFFFFF",
        on_click=iniciar_sesion
    )

    tarjeta = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("🐾", size=60),
                ft.Text(
                    "CLÍNICA VETERINARIA",
                    size=27,
                    weight=ft.FontWeight.BOLD,
                    color="#1D4ED8"
                ),
                ft.Text(
                    "Sistema de control veterinario",
                    color="#64748B"
                ),
                ft.Divider(),
                usuario,
                contrasena,
                boton,
                contador,
                mensaje
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=16
        ),
        width=430,
        padding=35,
        bgcolor="#FFFFFF",
        border_radius=25,
        shadow=ft.BoxShadow(
            blur_radius=20,
            color="#33000000",
            offset=ft.Offset(0, 8)
        )
    )

    page.add(
        ft.Container(
            content=tarjeta,
            alignment=ft.Alignment.CENTER,
            expand=True,
            padding=20,
            bgcolor="#DBEAFE"
        )
    )

    page.update()