import flet as ft
from datos import clientes_registrados, mascotas_registradas


def mostrar_mascotas(contenido):

    # ==========================================
    # CAMPOS DEL FORMULARIO
    # ==========================================

    nombre = ft.TextField(
        label="Nombre de la mascota",
        prefix_icon=ft.Icons.PETS,
        border_radius=10,
        bgcolor="#FFFFFF"
    )

    especie = ft.Dropdown(
        label="Especie",
        prefix_icon=ft.Icons.CATEGORY,
        options=[
            ft.dropdown.Option("Perro"),
            ft.dropdown.Option("Gato"),
            ft.dropdown.Option("Ave"),
            ft.dropdown.Option("Conejo"),
            ft.dropdown.Option("Hámster"),
            ft.dropdown.Option("Otro")
        ],
        border_radius=10,
        bgcolor="#FFFFFF"
    )

    raza = ft.TextField(
        label="Raza",
        prefix_icon=ft.Icons.PETS,
        border_radius=10,
        bgcolor="#FFFFFF"
    )

    edad = ft.TextField(
        label="Edad",
        hint_text="Ejemplo: 2 años",
        prefix_icon=ft.Icons.CALENDAR_MONTH,
        border_radius=10,
        bgcolor="#FFFFFF"
    )

    propietario = ft.Dropdown(
        label="Propietario",
        prefix_icon=ft.Icons.PERSON,
        options=[],
        border_radius=10,
        bgcolor="#FFFFFF"
    )

    mensaje = ft.Text(size=14)

    lista_mascotas = ft.Column(
        spacing=12
    )

    # ==========================================
    # CARGAR PROPIETARIOS REGISTRADOS
    # ==========================================

    def cargar_propietarios():

        propietario.options = [
            ft.dropdown.Option(
                key=str(i),
                text=f'{cliente["nombre"]} - {cliente["telefono"]}'
            )
            for i, cliente in enumerate(clientes_registrados)
        ]

    # ==========================================
    # MOSTRAR MASCOTAS REGISTRADAS
    # ==========================================

    def actualizar_lista():

        lista_mascotas.controls.clear()

        if not mascotas_registradas:
            lista_mascotas.controls.append(
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Icon(
                                ft.Icons.PETS,
                                size=45,
                                color="#94A3B8"
                            ),
                            ft.Text(
                                "Todavía no hay mascotas registradas.",
                                size=16,
                                color="#64748B"
                            )
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    bgcolor="#FFFFFF",
                    padding=25,
                    border_radius=15,
                    alignment=ft.Alignment.CENTER
                )
            )

        else:
            for mascota in mascotas_registradas:

                tarjeta = ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Text("🐾", size=35),
                                bgcolor="#D1FAE5",
                                padding=12,
                                border_radius=15
                            ),

                            ft.Column(
                                controls=[
                                    ft.Text(
                                        mascota["nombre"],
                                        size=19,
                                        weight=ft.FontWeight.BOLD,
                                        color="#047857"
                                    ),

                                    ft.Text(
                                        f'Especie: {mascota["especie"]}'
                                    ),

                                    ft.Text(
                                        f'Raza: {mascota["raza"]}'
                                    ),

                                    ft.Text(
                                        f'Edad: {mascota["edad"]}'
                                    ),

                                    ft.Text(
                                        f'Propietario: {mascota["propietario"]}',
                                        color="#2563EB"
                                    )
                                ],
                                spacing=5,
                                expand=True
                            )
                        ],
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=15
                    ),

                    bgcolor="#FFFFFF",
                    padding=18,
                    border_radius=15,
                    border=ft.Border.all(
                        1,
                        "#A7F3D0"
                    )
                )

                lista_mascotas.controls.append(tarjeta)

    # ==========================================
    # REGISTRAR MASCOTA
    # ==========================================

    def registrar_mascota(e):

        if not nombre.value or not nombre.value.strip():
            mensaje.value = "Escribe el nombre de la mascota."
            mensaje.color = "#DC2626"
            contenido.update()
            return

        if not especie.value:
            mensaje.value = "Selecciona la especie."
            mensaje.color = "#DC2626"
            contenido.update()
            return

        if not propietario.value:
            mensaje.value = "Selecciona un propietario."
            mensaje.color = "#DC2626"
            contenido.update()
            return

        indice = int(propietario.value)

        if indice >= len(clientes_registrados):
            mensaje.value = "Actualiza la lista de propietarios."
            mensaje.color = "#DC2626"
            contenido.update()
            return

        cliente = clientes_registrados[indice]

        nueva_mascota = {
            "nombre": nombre.value.strip(),
            "especie": especie.value,
            "raza": raza.value.strip() if raza.value else "No especificada",
            "edad": edad.value.strip() if edad.value else "No indicada",
            "propietario": cliente["nombre"],
            "telefono_propietario": cliente["telefono"]
        }

        mascotas_registradas.append(nueva_mascota)

        # Limpiar el formulario después de guardar
        nombre.value = ""
        especie.value = None
        raza.value = ""
        edad.value = ""
        propietario.value = None

        mensaje.value = "¡Mascota registrada correctamente!"
        mensaje.color = "#059669"

        actualizar_lista()
        contenido.update()

    # ==========================================
    # ACTUALIZAR PROPIETARIOS
    # ==========================================

    def actualizar_propietarios(e):

        cargar_propietarios()

        mensaje.value = (
            "Lista de propietarios actualizada."
            if clientes_registrados
            else "Primero debes registrar un cliente."
        )

        mensaje.color = (
            "#059669"
            if clientes_registrados
            else "#D97706"
        )

        contenido.update()

    # ==========================================
    # CONSTRUIR LA PANTALLA
    # ==========================================

    cargar_propietarios()
    actualizar_lista()

    formulario = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    "Información de la mascota",
                    size=21,
                    weight=ft.FontWeight.BOLD,
                    color="#172554"
                ),

                nombre,
                especie,
                raza,
                edad,
                propietario,

                ft.Button(
                    "Actualizar propietarios",
                    icon=ft.Icons.REFRESH,
                    on_click=actualizar_propietarios,
                    bgcolor="#DBEAFE",
                    color="#1D4ED8"
                ),

                ft.Button(
                    "Registrar mascota",
                    icon=ft.Icons.PETS,
                    on_click=registrar_mascota,
                    bgcolor="#059669",
                    color="#FFFFFF",
                    width=250,
                    height=45
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
                                    "Registro de Mascotas",
                                    size=30,
                                    weight=ft.FontWeight.BOLD,
                                    color="#172554"
                                ),

                                ft.Text(
                                    "Registra y organiza la información de tus mascotas.",
                                    size=15,
                                    color="#64748B"
                                )
                            ],
                            spacing=5,
                            expand=True
                        ),

                        ft.Text(
                            "🐶",
                            size=55
                        )
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                ),
                bgcolor="#DBEAFE",
                padding=20,
                border_radius=18
            ),

            formulario,

            ft.Text(
                "Mascotas registradas",
                size=23,
                weight=ft.FontWeight.BOLD,
                color="#172554"
            ),

            lista_mascotas
        ],
        spacing=20,
        scroll=ft.ScrollMode.AUTO
    )

    # Actualiza únicamente el contenido central.
    # No uses page.clean() aquí.
    contenido.update()