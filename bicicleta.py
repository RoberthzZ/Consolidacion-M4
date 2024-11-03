from vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, tipo):
        super().__init__(marca, modelo, nro_ruedas)
        self.tipo = tipo

    def __str__(self): #llama a la clase padre
        return super().__str__() + f" Tipo: {self.tipo}"

    def guardar_datos_csv(self):
        return f'<class \'Vehiculo.Bicicleta\'>,"{{"marca": "{self.marca}", "modelo": "{self.modelo}", "nro_ruedas": {self.nro_ruedas}, "tipo": "{self.tipo}"}}"'
