from automovil import Automovil
from vehiculo import Vehiculo
from particular import Particular
from carga import Carga
from bicicleta import Bicicleta
from motocicleta import Motocicleta

def ingresar_automoviles():
    automoviles = []
    n = int(input("Cuantos Vehiculos desea insertar: "))

    for i in range(n):
        print(f"\nDatos del automóvil {i+1}")
        marca = input("Inserte la marca del automovil: ")
        modelo = input("Inserte el modelo: ")
        nro_ruedas = input("Inserte el numero de ruedas: ")
        velocidad = input("Inserte la velocidad en km/h: ")
        cilindrada = input("Inserte el cilindraje en cc: ")

        automovil = Automovil(marca, modelo, nro_ruedas, velocidad, cilindrada)
        automoviles.append(automovil)

    return automoviles

def guardar_vehiculos(vehiculos):
    try:
        with open('vehiculos.csv', 'w', newline='') as archivo:
            for vehiculo in vehiculos:
                archivo.write(vehiculo.guardar_datos_csv() + '\n')
    except Exception as e:
        print(f"Error al guardar el archivo: {str(e)}")

def leer_vehiculos():
    try:
        with open('vehiculos.csv', 'r') as archivo:
            for linea in archivo:
                clase, datos = linea.strip().split(',', 1)
                if "Particular" in clase:
                    print("\nLista de Vehiculos Particular")
                elif "Carga" in clase:
                    print("\nLista de Vehiculos Carga")
                elif "Motocicleta" in clase:
                    print("\nLista de Vehiculos Motocicleta")
                elif "Bicicleta" in clase and "Motocicleta" not in clase:
                    print("\nLista de Vehiculos Bicicleta")
                print(datos.strip('"'))
    except FileNotFoundError:
        print("El archivo vehiculos.csv no existe")
    except Exception as e:
        print(f"Error al leer el archivo: {str(e)}")

def main():
    automoviles = ingresar_automoviles()
    print("\nImprimiendo por pantalla los Vehículos:")
    for i, auto in enumerate(automoviles, 1):
        print(f"Datos del automóvil {i} : {auto}")

    particular = Particular("Ford", "Fiesta", "4", "180", "500", "5")
    carga = Carga("Daft Trucks", "G 38", "10", "120", "1000", "20000")
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", 21, "Doble Viga", "2T")

    print("\n")
    print(particular)
    print(carga)
    print(bicicleta)
    print(motocicleta)

    print("\nVerificación de relaciones de instancia:")
    print(f"Motocicleta es instancia con relación a Vehículo: {isinstance(motocicleta, Vehiculo)}")
    print(f"Motocicleta es instancia con relación a Automovil: {isinstance(motocicleta, Automovil)}")
    print(f"Motocicleta es instancia con relación a Vehículo particular: {isinstance(motocicleta, Particular)}")
    print(f"Motocicleta es instancia con relación a Vehículo de Carga: {isinstance(motocicleta, Carga)}")
    print(f"Motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta, Bicicleta)}")
    print(f"Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta, Motocicleta)}")

    vehiculos_especificos = [particular, carga, bicicleta, motocicleta]
    guardar_vehiculos(vehiculos_especificos)
    print("\nLeyendo vehículos desde CSV:")
    leer_vehiculos()

if __name__ == "__main__":
    main()
