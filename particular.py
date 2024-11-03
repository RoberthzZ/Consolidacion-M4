from automovil import Automovil

class Particular(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puestos):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.nro_puestos = nro_puestos

    def __str__(self): #llama a la clase padre y se concatena con el atributo nuevo
        return super().__str__() + f" Puestos: {self.nro_puestos}"

    def guardar_datos_csv(self):
        return f'<class \'Vehiculo.Particular\'>,"{{"marca": "{self.marca}", "modelo": "{self.modelo}", "nro_ruedas": "{self.nro_ruedas}", "velocidad": "{self.velocidad}", "cilindraje": "{self.cilindrada}", "nro_puestos": "{self.nro_puestos}"}}"'
