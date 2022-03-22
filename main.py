class Asiento:
    def __init__(self, color, precio, registro):
        self.cambiarColor(color)
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, color):
        colores = ["rojo","verde","amarillo","negro","blanco"]
        if color in colores:
            self.color = color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self, registro):
        self.registro = registro
    def asignarTipo(self, tipo):
        opciones = ["electrico", "gasolina"]
        if tipo in opciones:
            self.tipo = tipo
class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    
    def cantidadAsientos(self):
        contador = 0
        for el in self.asientos:
            if (isinstance(el, Asiento)):
                contador += 1
        return contador
    def verificarIntegridad(self):
        for el in self.asientos:
            if (isinstance(el, Asiento)):
                if el.registro != self.registro:
                    return "Las piezas no son originales"
        if self.motor.registro != self.registro:
            return "Las piezas no son originales"
        else:
            return "Auto original"
