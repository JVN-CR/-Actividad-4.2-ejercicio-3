import flet as ft


def mostrar_consultas(page):

    page.clean()

    mascota = ft.TextField(
        label="Nombre de la mascota",
        width=400
    )

    fecha = ft.TextField(
        label="Fecha de la consulta",
        hint_text="Ejemplo: 08/10/2026",
        width=400
    )

    veterinario = ft.TextField(
        label="Veterinario",
        width=400
    )

    motivo = ft.TextField(
        label="Motivo de la consulta",
        width=400
    )

    observaciones = ft.TextField(
        label="Observaciones",
        width=400,
        multiline=True
    )

    mensaje = ft.Text()

    def registrar(e):

        if mascota.value and fecha.value and motivo.value:
            mensaje.value = "Consulta registrada correctamente."
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
                    "🩺 Consultas Veterinarias",
                    size=30,
                    weight=ft.FontWeight.BOLD
                ),

                mascota,
                fecha,
                veterinario,
                motivo,
                observaciones,

                ft.Button(
                    "Registrar consulta",
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