import flet as ft
from datos import clientes_registrados


def mostrar_clientes(contenido):

    # Campos para registrar los datos del propietario
    nombre = ft.TextField(
        label="Nombre del propietario",
        width=400,
        prefix_icon=ft.Icons.PERSON
    )

    telefono = ft.TextField(
        label="Teléfono",
        width=400,
        prefix_icon=ft.Icons.PHONE
    )

    correo = ft.TextField(
        label="Correo electrónico",
        width=400,
        prefix_icon=ft.Icons.EMAIL
    )

    direccion = ft.TextField(
        label="Dirección",
        width=400,
        prefix_icon=ft.Icons.HOME
    )

    mensaje = ft.Text()

    # Aquí aparecerán los clientes registrados
    lista_clientes = ft.Column(
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # Función para actualizar la lista de clientes
    def actualizar_lista():

        lista_clientes.controls.clear()

        for cliente in clientes_registrados:

            tarjeta = ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(
                            cliente["nombre"],
                            size=20,
                            weight=ft.FontWeight.BOLD
                        ),
                        ft.Text(
                            f"Teléfono: {cliente['telefono']}"
                        ),
                        ft.Text(
                            f"Correo: {cliente['correo'] or 'No indicado'}"
                        ),
                        ft.Text(
                            f"Dirección: {cliente['direccion'] or 'No indicada'}"
                        )
                    ],
                    spacing=5
                ),
                padding=15,
                width=450,
                border=ft.Border.all(
                    1,
                    ft.Colors.GREEN
                ),
                border_radius=10,
                bgcolor=ft.Colors.WHITE
            )

            lista_clientes.controls.append(tarjeta)

    # Función para registrar un cliente
    def registrar(e):

        if not nombre.value or not nombre.value.strip():
            mensaje.value = "Ingrese el nombre del propietario."
            mensaje.color = ft.Colors.RED
            contenido.update()
            return

        if not telefono.value or not telefono.value.strip():
            mensaje.value = "Ingrese el teléfono del propietario."
            mensaje.color = ft.Colors.RED
            contenido.update()
            return

        # Crear el registro del cliente
        cliente = {
            "nombre": nombre.value.strip(),
            "telefono": telefono.value.strip(),
            "correo": (correo.value or "").strip(),
            "direccion": (direccion.value or "").strip()
        }

        # Guardar el cliente en la lista compartida
        clientes_registrados.append(cliente)

        # Actualizar la lista que aparece en pantalla
        actualizar_lista()

        mensaje.value = (
            f"Cliente {cliente['nombre']} registrado correctamente."
        )
        mensaje.color = ft.Colors.GREEN

        # Limpiar los campos del formulario
        nombre.value = ""
        telefono.value = ""
        correo.value = ""
        direccion.value = ""

        contenido.update()

    # Contenido de la pantalla
    contenido.content = ft.Column(
        controls=[
            ft.Text(
                "REGISTRO DE CLIENTES",
                size=30,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.GREEN
            ),

            ft.Text(
                "Ingrese los datos del propietario de la mascota.",
                size=16
            ),

            nombre,
            telefono,
            correo,
            direccion,

            ft.Button(
                "Registrar cliente",
                icon=ft.Icons.PERSON_ADD,
                width=300,
                on_click=registrar
            ),

            mensaje,

            ft.Divider(),

            ft.Text(
                "CLIENTES REGISTRADOS",
                size=24,
                weight=ft.FontWeight.BOLD
            ),

            lista_clientes
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15,
        scroll=ft.ScrollMode.AUTO
    )

    # Mostrar los clientes que ya están registrados
    actualizar_lista()

    contenido.update()