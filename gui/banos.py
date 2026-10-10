import flet as ft


def mostrar_banos(page):

    page.clean()

    mascota = ft.TextField(
        label="Nombre de la mascota",
        width=400
    )

    fecha = ft.TextField(
        label="Fecha del baño",
        hint_text="Ejemplo: 08/10/2026",
        width=400
    )

    tipo = ft.TextField(
        label="Tipo de baño",
        hint_text="Ejemplo: baño normal, medicado, antipulgas",
        width=400
    )

    observaciones = ft.TextField(
        label="Observaciones",
        width=400,
        multiline=True
    )

    mensaje = ft.Text()

    def registrar(e):

        if mascota.value and fecha.value:
            mensaje.value = "Baño registrado correctamente."
        else:
            mensaje.value = "Complete los datos obligatorios."

        page.update()

    def volver(e):
        from gui.dashboard import mostrar_dashboard
        mostrar_dashboard(page)

    page.add(
        ft.Column(
            controls=[
                ft.Text(
                    "🛁 Registro de Baños",
                    size=30,
                    weight=ft.FontWeight.BOLD
                ),

                mascota,
                fecha,
                tipo,
                observaciones,

                ft.Button(
                    "Registrar baño",
                    width=300,
                    on_click=registrar
                ),

                ft.Button(
                    "Volver al Dashboard",
                    width=300,
                    on_click=volver
                ),

                mensaje
            ],

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        )
    )