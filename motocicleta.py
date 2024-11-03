from bicicleta import Bicicleta

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nro_ruedas, tipo, nro_radios, cuadro, motor):
        super().__init__(marca, modelo, nro_ruedas, tipo)
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor

    def __str__(self): #llama a la clase padre y se concatena con los atributos nuevos
        return super().__str__() + f" Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nro_radios}"

    def guardar_datos_csv(self):
        return f'<class \'Vehiculo.Motocicleta\'>,"{{"marca": "{self.marca}", "modelo": "{self.modelo}", "nro_ruedas": {self.nro_ruedas}, "tipo": "{self.tipo}", "motor": "{self.motor}", "cuadro": "{self.cuadro}", "nro_radios": {self.nro_radios}}}"'
