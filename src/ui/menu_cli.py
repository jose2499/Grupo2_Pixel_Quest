import sys
import os

# Aseguramos que Python encuentre los módulos en src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from domain.models import Heroe
from services.juego_service import JuegoService

class MenuCLI:
    def __init__(self):
        self.heroe = None
        self.juego_service = None

    def iniciar_juego(self):
        print("=== BIENVENIDO A PIXEL QUEST ===")
        nombre = input("Ingresa el nombre de tu héroe: ").strip()
        if not nombre:
            nombre = "Héroe Legendario"
        
        # Creación del personaje principal
        self.heroe = Heroe(nombre=nombre, vida_maxima=100, vida_actual=100, ataque=15)
        self.juego_service = JuegoService(self.heroe)
        
        print(f"\n¡Bienvenido, {self.heroe.nombre}! Tu aventura comienza ahora.\n")
        self.menu_principal()

    def menu_principal(self):
        while True:
            print("\n--- MENÚ PRINCIPAL ---")
            print("1. Explorar la Mazmorra")
            print("2. Ver Estadísticas del Héroe")
            print("3. Salir")
            
            opcion = input("Selecciona una opción (1-3): ").strip()

            if opcion == "1":
                self.iniciar_exploracion()
            elif opcion == "2":
                self.mostrar_estadisticas()
            elif opcion == "3":
                print("\n¡Gracias por jugar a Pixel Quest! Hasta pronto.")
                break
            else:
                print("Opción inválida, intenta de nuevo.")

    def mostrar_estadisticas(self):
        print("\n--- ESTADÍSTICAS DEL HÉROE ---")
        print(f"Nombre: {self.heroe.nombre}")
        print(f"Nivel: {self.heroe.nivel}")
        print(f"Vida: {self.heroe.vida_actual}/{self.heroe.vida_maxima}")
        print(f"Ataque: {self.heroe.ataque}")
        print(f"Experiencia: {self.heroe.experiencia}")

    def iniciar_exploracion(self):
        monstruo = self.juego_service.explorar()
        print(f"\n¡Un salvaje {monstruo.nombre} ha aparecido!")

        while monstruo.esta_vivo() and self.heroe.esta_vivo():
            print(f"\n[{self.heroe.nombre}: {self.heroe.vida_actual} HP] vs [{monstruo.nombre}: {monstruo.vida_actual} HP]")
            print("1. Atacar")
            print("2. Huir")
            
            accion = input("¿Qué deseas hacer?: ").strip()

            if accion == "1":
                resultado = self.juego_service.ejecutar_turno_combate(monstruo, "atacar")
                print(resultado["mensaje"])
                if resultado["combate_finalizado"]:
                    break
            elif accion == "2":
                resultado = self.juego_service.ejecutar_turno_combate(monstruo, "huir")
                print(resultado["mensaje"])
                break
            else:
                print("Acción no válida.")

if __name__ == "__main__":
    app = MenuCLI()
    app.iniciar_juego()