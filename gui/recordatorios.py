import flet as ft


def mostrar_recordatorios(page):

    page.clean()

    mascota = ft.TextField(
        label="Nombre de la mascota",
        width=400
    )

    actividad = ft.TextField(
        label="Actividad",
        hint_text="Ejemplo: vacuna, baño o desparasitación",
        width=400
    )

    fecha = ft.TextField(
        label="Fecha del recordatorio",
        hint_text="Ejemplo: 15/10/2026",
        width=400
    )

    mensaje_recordatorio = ft.TextField(
        label="Descripción del recordatorio",
        width=400,
        multiline=True
    )

    mensaje = ft.Text()

    def registrar(e):

        if mascota.value and actividad.value and fecha.value:
            mensaje.value = "Recordatorio registrado correctamente."
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
                    "🔔 Recordatorios",
                    size=30,
                    weight=ft.FontWeight.BOLD
                ),

                mascota,
                actividad,
                fecha,
                mensaje_recordatorio,

                ft.Button(
                    "Guardar recordatorio",
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