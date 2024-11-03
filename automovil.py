from vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, nro_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):  #llama a la clase padre y concatena con atributos nuevos
        return super().__str__() + f" {self.velocidad} km/h, {self.cilindrada} cc"
    
    
    

#my_car = Automovil(marca="Nissan", modelo="Versa", nro_ruedas=4, velocidad=120, cilindrada=1400)
    
#print(my_car)