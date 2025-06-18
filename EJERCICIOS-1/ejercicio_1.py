from enum import Enum
class EstadoIMC(Enum):
    BAJO_PESO = -1
    NORMAL = 0
    SOBREPESO = 1
    OBESIDAD = 2
    OBESIDAD_EXTREMA = 3

# Clase Persona
class Persona:
    __contador_dni = 1  
    def __init__(self, documento='', nombre='', edad=0, sexo='M', peso=0.0, altura=0.0):
        self.__documento = documento
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = self.__comprobarSexo(sexo)
        self.__peso = peso
        self.__altura = altura
        self.__dni = self.__generaDNI()

    @classmethod
    def crear_con_datos(cls, documento, nombre, edad, sexo):
        return cls(documento, nombre, edad, sexo)

    @classmethod
    def crear_completo(cls, documento, nombre, edad, sexo, peso, altura):
        return cls(documento, nombre, edad, sexo, peso, altura)

    # Métodos privados
    def __comprobarSexo(self, sexo):
        return sexo.upper() if sexo.upper() in ['M', 'F'] else 'M'

    def __generaDNI(self):
        dni = Persona.__contador_dni
        Persona.__contador_dni += 1
        return dni

    # Getters
    def get_documento(self): return self.__documento
    def get_nombre(self): return self.__nombre
    def get_edad(self): return self.__edad
    def get_sexo(self): return self.__sexo
    def get_peso(self): return self.__peso
    def get_altura(self): return self.__altura
    def get_dni(self): return self.__dni

    # Setters
    def set_documento(self, documento): self.__documento = documento
    def set_nombre(self, nombre): self.__nombre = nombre
    def set_edad(self, edad): self.__edad = edad
    def set_sexo(self, sexo): self.__sexo = self.__comprobarSexo(sexo)
    def set_peso(self, peso): self.__peso = peso
    def set_altura(self, altura): self.__altura = altura

    def calcularIMC(self):
        if self.__altura <= 0:
            return None
        imc = self.__peso / ((self.__altura / 100) ** 2)
        if imc < 18.5:
            return EstadoIMC.BAJO_PESO
        elif 18.5 <= imc <= 24.9:
            return EstadoIMC.NORMAL
        elif 25.0 <= imc <= 29.9:
            return EstadoIMC.SOBREPESO
        elif 30.0 <= imc <= 39.9:
            return EstadoIMC.OBESIDAD
        else:
            return EstadoIMC.OBESIDAD_EXTREMA

    def esMayorDeEdad(self):
        return self.__edad >= 18

    def listarInformacion(self):
        estado_str = self.calcularIMC().name.replace('_', ' ').capitalize() if self.calcularIMC() else "Desconocido"
        sexo_str = "Masculino" if self.__sexo == 'M' else "Femenino"
        return (f"Hola {self.__nombre}, tu código dentro del sistema es {self.__dni}. "
                f"Tu identificación es {self.__documento}. Tu edad es {self.__edad} años. "
                f"Tu género es {sexo_str}. Tu peso es {self.__peso} kg y tu altura es {self.__altura} cm. "
                f"Al calcular tu IMC concluimos que tu peso está: {estado_str}.")

def ejecutar():
    while True:
        print("\n--- Ingresar datos de una persona ---")
        doc = input("Documento: ")
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        sexo = input("Sexo (M/F): ")
        peso = float(input("Peso (kg): "))
        altura = float(input("Altura (cm): "))

        persona1 = Persona.crear_completo(doc, nombre, edad, sexo, peso, altura)
        persona2 = Persona.crear_con_datos("12345", "Pedro Gomez", 25, "M")
        persona3 = Persona()

        persona3.set_documento("67890")
        persona3.set_nombre("Ana Torres")
        persona3.set_edad(32)
        persona3.set_sexo("F")
        persona3.set_peso(58)
        persona3.set_altura(160)

        personas = [persona1, persona2, persona3]

        for i, p in enumerate(personas, 1):
            print(f"\n--- Persona {i} ---")
            imc_resultado = p.calcularIMC()
            imc_texto = imc_resultado.name.replace('_', ' ').capitalize() if imc_resultado else "Desconocido"
            print("IMC:", imc_texto)
            print("Es mayor de edad:", "Sí" if p.esMayorDeEdad() else "No")
            print(p.listarInformacion())

        otra = input("\n¿Desea ingresar otra persona? (s/n): ").lower()
        if otra != 's':
            break

if __name__ == "__main__":
    ejecutar()
