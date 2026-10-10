import datos
from entidades import Cliente, Mascota, Vacuna, Desparasitacion, Baño, Consulta


def registrar_cliente(nombre, telefono):
    datos.ultimo_id_cliente += 1

    cliente = Cliente(
        datos.ultimo_id_cliente,
        nombre,
        telefono
    )

    datos.clientes.append(cliente)

    return cliente


def registrar_mascota(nombre, especie, raza, edad, id_cliente):
    datos.ultimo_id_mascota += 1

    mascota = Mascota(
        datos.ultimo_id_mascota,
        nombre,
        especie,
        raza,
        edad,
        id_cliente
    )

    datos.mascotas.append(mascota)

    return mascota


def registrar_vacuna(id_mascota, nombre, fecha):
    vacuna = Vacuna(
        id_mascota,
        nombre,
        fecha
    )

    datos.vacunas.append(vacuna)

    return vacuna


def registrar_desparasitacion(id_mascota, fecha, medicamento):
    desparasitacion = Desparasitacion(
        id_mascota,
        fecha,
        medicamento
    )

    datos.desparasitaciones.append(desparasitacion)

    return desparasitacion


def registrar_bano(id_mascota, fecha):
    bano = Baño(
        id_mascota,
        fecha
    )

    datos.banos.append(bano)

    return bano


def registrar_consulta(id_mascota, fecha, motivo, observaciones):
    consulta = Consulta(
        id_mascota,
        fecha,
        motivo,
        observaciones
    )

    datos.consultas.append(consulta)

    return consulta

def obtener_clientes():
    return datos.clientes


def obtener_mascotas():
    return datos.mascotas


def obtener_vacunas():
    return datos.vacunas


def obtener_desparasitaciones():
    return datos.desparasitaciones


def obtener_banos():
    return datos.banos


def obtener_consultas():
    return datos.consultas