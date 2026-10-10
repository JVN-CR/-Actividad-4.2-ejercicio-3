class Cliente:
    def __init__(self, id_cliente, nombre, telefono):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.telefono = telefono


class Mascota:
    def __init__(
        self,
        id_mascota,
        nombre,
        especie,
        raza,
        edad,
        id_cliente
    ):
        self.id_mascota = id_mascota
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.id_cliente = id_cliente


class Vacuna:
    def __init__(self, id_mascota, nombre, fecha):
        self.id_mascota = id_mascota
        self.nombre = nombre
        self.fecha = fecha


class Desparasitacion:
    def __init__(self, id_mascota, fecha, medicamento):
        self.id_mascota = id_mascota
        self.fecha = fecha
        self.medicamento = medicamento


class Baño:
    def __init__(self, id_mascota, fecha):
        self.id_mascota = id_mascota
        self.fecha = fecha


class Consulta:
    def __init__(self, id_mascota, fecha, motivo, observaciones):
        self.id_mascota = id_mascota
        self.fecha = fecha
        self.motivo = motivo
        self.observaciones = observaciones