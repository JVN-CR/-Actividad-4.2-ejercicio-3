import flet as ft
from datetime import datetime
from datos import mascotas_registradas, historial_cuidados


def mostrar_vacunas(contenido):

    # Título y mensajes
    mensaje = ft.Text(size=14)

    # Seleccionar mascota
    mascota = ft.Dropdown(
        label="Seleccionar mascota",
        options=[
            ft.dropdown.Option(
                key=str(i),
                text=f'{m["nombre"]} - {m["propietario"]}'
            )
            for i, m in enumerate(mascotas_registradas)
        ],
        width=450,
        border_radius=10
    )

    # Campos del formulario
    nombre_vacuna = ft.TextField(
        label="Nombre de la vacuna",
        prefix_icon=ft.Icons.MEDICAL_SERVICES,
        width=450,
        border_radius=10
    )

    fecha = ft.TextField(
        label="Fecha de vacunación (AAAA-MM-DD)",
        hint_text="2026-10-10",
        prefix_icon=ft.Icons.CALENDAR_MONTH,
        width=450,
        border_radius=10
    )

    observaciones = ft.TextField(
        label="Observaciones",
        multiline=True,
        min_lines=2,
        max_lines=3,
        width=450,
        border_radius=10
    )

    lista_vacunas = ft.Column(spacing=12)

    # Mostrar las vacunas registradas
    def actualizar_lista():
        lista_vacunas.controls.clear()

        registros = [
            r for r in reversed(historial_cuidados)
            if r.get("tipo") == "Vacuna"
        ]

        if not registros:
            lista_vacunas.controls.append(
                ft.Container(
                    content=ft.Text(
                        "Todavía no hay vacunas registradas.",
                        color="#64748B"
                    ),
                    bgcolor="#FFFFFF",
                    padding=20,
                    border_radius=12
                )
            )
        else:
            for registro in registros:
                lista_vacunas.controls.append(
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Icon(
                                    ft.Icons.HEALTH_AND_SAFETY,
                                    size=35,
                                    color="#2563EB"
                                ),
                                ft.Column(
                                    controls=[
                                        ft.Text(
                                            registro["mascota"],
                                            size=18,
                                            weight=ft.FontWeight.BOLD,
                                            color="#1D4ED8"
                                        ),
                                        ft.Text(
                                            f'Vacuna: {registro["descripcion"]}'
                                        ),
                                        ft.Text(
                                            f'Fecha: {registro["fecha"]}'
                                        )
                                    ],
                                    spacing=5,
                                    expand=True
                                )
                            ]
                        ),
                        bgcolor="#FFFFFF",
                        padding=18,
                        border_radius=12,
                        border=ft.Border.all(1, "#BFDBFE")
                    )
                )

    # Registrar una vacuna
    def registrar_vacuna(e):

        if not mascotas_registradas:
            mensaje.value = (
                "Primero debes registrar una mascota en la sección Mascotas."
            )
            mensaje.color = "#DC2626"
            contenido.update()
            return

        if not mascota.value:
            mensaje.value = "Selecciona una mascota."
            mensaje.color = "#DC2626"
            contenido.update()
            return

        if not nombre_vacuna.value or not nombre_vacuna.value.strip():
            mensaje.value = "Escribe el nombre de la vacuna."
            mensaje.color = "#DC2626"
            contenido.update()
            return

        try:
            datetime.strptime(fecha.value or "", "%Y-%m-%d")
        except ValueError:
            mensaje.value = "Escribe una fecha válida: AAAA-MM-DD."
            mensaje.color = "#DC2626"
            contenido.update()
            return

        indice = int(mascota.value)
        m = mascotas_registradas[indice]

        detalle = nombre_vacuna.value.strip()

        if observaciones.value and observaciones.value.strip():
            detalle += " - " + observaciones.value.strip()

        historial_cuidados.append({
            "mascota": m["nombre"],
            "propietario": m["propietario"],
            "tipo": "Vacuna",
            "fecha": fecha.value,
            "descripcion": detalle
        })

        nombre_vacuna.value = ""
        fecha.value = ""
        observaciones.value = ""

        mensaje.value = "¡Vacuna registrada correctamente!"
        mensaje.color = "#059669"

        actualizar_lista()
        contenido.update()

    # Actualizar las opciones de mascotas
    def actualizar_mascotas(e):
        mascota.options = [
            ft.dropdown.Option(
                key=str(i),
                text=f'{m["nombre"]} - {m["propietario"]}'
            )
            for i, m in enumerate(mascotas_registradas)
        ]

        mascota.value = None

        if mascotas_registradas:
            mensaje.value = "Lista de mascotas actualizada."
            mensaje.color = "#059669"
        else:
            mensaje.value = "Todavía no hay mascotas registradas."
            mensaje.color = "#D97706"

        contenido.update()

    # Construir pantalla
    actualizar_lista()

    formulario = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    "Información de la vacunación",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color="#172554"
                ),
                mascota,
                ft.Button(
                    "Actualizar mascotas",
                    icon=ft.Icons.REFRESH,
                    bgcolor="#DBEAFE",
                    color="#1D4ED8",
                    on_click=actualizar_mascotas
                ),
                nombre_vacuna,
                fecha,
                observaciones,
                ft.Button(
                    "Registrar vacuna",
                    icon=ft.Icons.CHECK_CIRCLE,
                    bgcolor="#2563EB",
                    color="#FFFFFF",
                    width=250,
                    height=45,
                    on_click=registrar_vacuna
                ),
                mensaje
            ],
            spacing=15
        ),
        bgcolor="#FFFFFF",
        padding=25,
        border_radius=18,
        border=ft.Border.all(1, "#D5E3F5")
    )

    contenido.content = ft.Column(
        controls=[
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Text(
                                    "Registro de Vacunas",
                                    size=30,
                                    weight=ft.FontWeight.BOLD,
                                    color="#1D4ED8"
                                ),
                                ft.Text(
                                    "Controla las vacunas aplicadas a tus mascotas.",
                                    color="#64748B"
                                )
                            ],
                            expand=True,
                            spacing=8
                        ),
                        ft.Text("🐾", size=45)
                    ]
                ),
                bgcolor="#DBEAFE",
                padding=20,
                border_radius=15
            ),
            formulario,
            ft.Text(
                "Vacunas registradas",
                size=24,
                weight=ft.FontWeight.BOLD,
                color="#172554"
            ),
            lista_vacunas
        ],
        spacing=20,
        scroll=ft.ScrollMode.AUTO
    )

    contenido.update()