import flet as ft
from datetime import datetime
from datos import mascotas_registradas, historial_cuidados


def mostrar_desparasitaciones(contenido):

    mascota = ft.Dropdown(
        label="Seleccionar mascota",
        options=[
            ft.dropdown.Option(
                key=str(i),
                text=f'{m["nombre"]} - {m["propietario"]}'
            )
            for i, m in enumerate(mascotas_registradas)
        ]
    )

    fecha = ft.TextField(label="Fecha (AAAA-MM-DD)")
    producto = ft.TextField(label="Producto utilizado")
    mensaje = ft.Text()
    lista = ft.Column(spacing=10)

    def actualizar_lista():
        lista.controls.clear()

        for r in reversed(historial_cuidados):
            if r["tipo"] == "Desparasitación":
                lista.controls.append(
                    ft.Container(
                        content=ft.Column([
                            ft.Text(
                                r["mascota"],
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color="#7C3AED"
                            ),
                            ft.Text(f'Detalles: {r["descripcion"]}'),
                            ft.Text(f'Fecha: {r["fecha"]}')
                        ]),
                        bgcolor="#FFFFFF",
                        padding=15,
                        border_radius=12
                    )
                )

    def registrar(e):
        try:
            datetime.strptime(fecha.value or "", "%Y-%m-%d")

            if not mascota.value or not producto.value:
                mensaje.value = "Completa todos los campos."
                mensaje.color = "#DC2626"
                contenido.update()
                return

            m = mascotas_registradas[int(mascota.value)]

            historial_cuidados.append({
                "mascota": m["nombre"],
                "propietario": m["propietario"],
                "tipo": "Desparasitación",
                "fecha": fecha.value,
                "descripcion": producto.value
            })

            fecha.value = ""
            producto.value = ""
            mensaje.value = "Desparasitación registrada."
            mensaje.color = "#059669"

            actualizar_lista()

        except ValueError:
            mensaje.value = "Usa una fecha válida: AAAA-MM-DD."
            mensaje.color = "#DC2626"

        contenido.update()

    actualizar_lista()

    contenido.content = ft.Column([
        ft.Text(
            "Registro de Desparasitaciones",
            size=30,
            weight=ft.FontWeight.BOLD,
            color="#7C3AED"
        ),
        ft.Container(
            content=ft.Column([
                mascota,
                fecha,
                producto,
                ft.Button(
                    "Registrar desparasitación",
                    bgcolor="#7C3AED",
                    color="#FFFFFF",
                    on_click=registrar
                ),
                mensaje
            ], spacing=15),
            bgcolor="#FFFFFF",
            padding=20,
            border_radius=15
        ),
        ft.Text(
            "Registros anteriores",
            size=22,
            weight=ft.FontWeight.BOLD
        ),
        lista
    ], spacing=18, scroll=ft.ScrollMode.AUTO)

    contenido.update()