class Cuenta:
    __ultimo_numero = 100000  # atributo de clase

    def __init__(self, dni, saldo, interes_anual):
        Cuenta.__ultimo_numero += 1
        self.numero_cuenta = Cuenta.__ultimo_numero
        self.dni = dni
        self.saldo = saldo
        self.interes_anual = interes_anual

    @classmethod
    def verificarSaldo(cls, saldo):
        if saldo < 0:
            return 'Saldo insuficiente'
        elif saldo == 0:
            return 'Saldo es 0'
        else:
            return 'Saldo positivo'

    def actualizarSaldo(self):
        estado_saldo = self.__class__.verificarSaldo(self.saldo)
        print("Estado del saldo:", estado_saldo)

        if self.saldo > 0:
            interes_diario = (self.interes_anual / 100) / 365
            interes = self.saldo * interes_diario
            self.saldo += interes
        else:
            raise ValueError('No hay saldo suficiente para aplicar interés')

    def Ingresar(self, monto):
        self.saldo += monto

    def Retirar(self, monto):
        if monto > self.saldo:
            raise ValueError("Fondos insuficientes")
        self.saldo -= monto

    def mostrarInformacion(self):
        info = (
            f"Cuenta N°: {self.numero_cuenta}\n"
            f"DNI del titular: {self.dni}\n"
            f"Saldo actual: ${self.saldo:.2f}\n"
            f"Interés anual: {self.interes_anual:.2f}%\n"
            f"Estado del saldo: {self.verificarSaldo(self.saldo)}"
        )
        print(info)

def menu():
    cuentas = []

    while True:
        print("\n--- BANCO PYTHON ---")
        print("1. Crear nueva cuenta")
        print("2. Ver información de una cuenta")
        print("3. Ingresar dinero")
        print("4. Retirar dinero")
        print("5. Actualizar saldo (interés diario)")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            dni = input("Ingrese DNI: ")
            saldo = float(input("Ingrese saldo inicial: "))
            interes = float(input("Ingrese interés anual (%): "))
            cuenta = Cuenta(dni, saldo, interes)
            cuentas.append(cuenta)
            print(f"Cuenta creada con número: {cuenta.numero_cuenta}")

        elif opcion == '2':
            numero = int(input("Ingrese número de cuenta: "))
            cuenta = next((c for c in cuentas if c.numero_cuenta == numero), None)
            if cuenta:
                cuenta.mostrarInformacion()
            else:
                print("Cuenta no encontrada.")

        elif opcion == '3':
            numero = int(input("Ingrese número de cuenta: "))
            monto = float(input("Ingrese monto a ingresar: "))
            cuenta = next((c for c in cuentas if c.numero_cuenta == numero), None)
            if cuenta:
                cuenta.Ingresar(monto)
                print("Dinero ingresado correctamente.")
            else:
                print("Cuenta no encontrada.")

        elif opcion == '4':
            numero = int(input("Ingrese número de cuenta: "))
            monto = float(input("Ingrese monto a retirar: "))
            cuenta = next((c for c in cuentas if c.numero_cuenta == numero), None)
            if cuenta:
                try:
                    cuenta.Retirar(monto)
                    print("Retiro exitoso.")
                except ValueError as e:
                    print("Error:", e)
            else:
                print("Cuenta no encontrada.")

        elif opcion == '5':
            numero = int(input("Ingrese número de cuenta: "))
            cuenta = next((c for c in cuentas if c.numero_cuenta == numero), None)
            if cuenta:
                try:
                    cuenta.actualizarSaldo()
                    print("Saldo actualizado con interés diario.")
                except ValueError as e:
                    print("Error:", e)
            else:
                print("Cuenta no encontrada.")

        elif opcion == '6':
            print("Gracias por usar el sistema bancario. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
