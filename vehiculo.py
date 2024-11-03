class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas"
    
    
    
    
#my_car = Vehiculo(marca="Nissan", modelo="Versa", nro_ruedas=4)
    
#print(my_car)