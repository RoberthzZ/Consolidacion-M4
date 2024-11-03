from automovil import Automovil

class Carga(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, carga):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self): #llama a la clase padre y se concatena con el atributo nuevo
        return super().__str__() + f" Carga: {self.carga} Kg"

    def guardar_datos_csv(self):
        return f'<class \'Vehiculo.Carga\'>,"{{"marca": "{self.marca}", "modelo": "{self.modelo}", "nro_ruedas": "{self.nro_ruedas}", "velocidad": "{self.velocidad}", "cilindraje": "{self.cilindrada}", "carga": "{self.carga}"}}"'
