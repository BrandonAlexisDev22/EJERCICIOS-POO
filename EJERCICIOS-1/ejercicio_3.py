class Cafetera:
    def __init__(self, capacidad_maxima: int = 1000, capacidad_actual: int = 0):
        self.capacidad_maxima = capacidad_maxima
        self.capacidad_actual = min(capacidad_actual, capacidad_maxima)

    def servirTaza(self, cantidad: int):
        if self.capacidad_actual >= cantidad:
            self.capacidad_actual -= cantidad
            print(f"Se sirvió una taza con {cantidad} ml de café.")
        else:
            print(f"No hay suficiente café. Se sirvieron solo {self.capacidad_actual} ml.")
            self.capacidad_actual = 0

    def vaciarCafetera(self):
        self.capacidad_actual = 0
        print("La cafetera ha sido vaciada.")

    def agregarCafe(self, cantidad: int):
        if self.capacidad_actual + cantidad > self.capacidad_maxima:
            self.capacidad_actual = self.capacidad_maxima
            print("Se llenó la cafetera al máximo.")
        else:
            self.capacidad_actual += cantidad
            print(f"Se agregó {cantidad} ml de café.")

    def mostrarEstado(self):
        print(f"Café actual: {self.capacidad_actual} ml / {self.capacidad_maxima} ml\n")


def main():
    print("=== Bienvenido al sistema de Cafetera ===")
    capacidad_max = int(input("Ingrese la capacidad máxima de la cafetera (ml): "))
    cantidad_actual = int(input("Ingrese la cantidad de café actual (ml): "))
    cafetera = Cafetera(capacidad_max, cantidad_actual)

    while True:
        print("\n--- Menú ---")
        print("1. Servir taza")
        print("2. Vaciar cafetera")
        print("3. Agregar café")
        print("4. Mostrar estado")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cantidad = int(input("¿Cuántos ml desea servir?: "))
            cafetera.servirTaza(cantidad)
        elif opcion == "2":
            cafetera.vaciarCafetera()
        elif opcion == "3":
            cantidad = int(input("¿Cuántos ml de café desea agregar?: "))
            cafetera.agregarCafe(cantidad)
        elif opcion == "4":
            cafetera.mostrarEstado()
        elif opcion == "5":
            print("¡Gracias por usar la cafetera!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
