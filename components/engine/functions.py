import math

class RecepcionArroz:
    def __init__(self, peso, humedad, fecha_hora, proveedor, variedad):
        self.peso = peso
        self.humedad = humedad
        self.fecha_hora = fecha_hora
        self.proveedor = proveedor
        self.variedad = variedad

class CargaDescarga:
    def __init__(self, peso, numero_camion, conductor, fecha_hora):
        self.peso = peso
        self.numero_camion = numero_camion
        self.conductor = conductor
        self.fecha_hora = fecha_hora

class Almacenamiento:
    def __init__(self, ubicacion, capacidad, nivel_actual, temperatura, humedad):
        self.ubicacion = ubicacion
        self.capacidad = capacidad
        self.nivel_actual = nivel_actual
        self.temperatura = temperatura
        self.humedad = humedad

class Secado:
    def __init__(self, temp_aire, humedad_aire, duracion, velocidad_flujo):
        self.temp_aire = temp_aire
        self.humedad_aire = humedad_aire
        self.duracion = duracion
        self.velocidad_flujo = velocidad_flujo

class Mantenimiento:
    def __init__(self, fecha_hora, descripcion="", personal=""):
        self.fecha_hora = fecha_hora
        self.descripcion = descripcion
        self.personal = personal

class NuevaOrden:
    def __init__(self, cliente="", tipo_arroz=""):
        self.cliente = cliente
        self.tipo_arroz = tipo_arroz