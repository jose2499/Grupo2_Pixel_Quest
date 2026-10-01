from src.domain.models import Heroe
from src.services.juego_service import JuegoService
from src.services.data_manager import DataManager

def menu_principal():
    print("========================================")
    print("       ¡BIENVENIDO A PIXEL QUEST!       ")
    print("========================================")
    print("1. Nueva Partida")
    print("2. Cargar Partida")
    
    opcion_inicio = input("Selecciona una opción (1-2): ")
    heroe = None

    if opcion_inicio == "2":
        heroe = DataManager.cargar_heroe()
        if heroe:
            print(f"\n¡Partida cargada con éxito! Bienvenido de nuevo, {heroe.nombre}.")
        else:
            print("\nNo se encontró ninguna partida guardada. Se creará un nuevo héroe.")

    if not heroe:
        nombre = input("\nIngresa el nombre de tu héroe: ")
        heroe = Heroe(nombre=nombre, vida_maxima=100, vida_actual=100, ataque=15)
        print(f"\n¡Hola, {heroe.nombre}! Tu aventura comienza ahora.")

    juego_service = JuegoService(heroe)

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Explorar la Mazmorra")
        print("2. Ver Estadísticas del Héroe")
        print("3. Guardar Partida")
        print("4. Salir")
        
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            enemigo = juego_service.explorar()
            print(f"\n¡Te has encontrado con un {enemigo.nombre}!")
            
            # Bucle de combate
            while enemigo.esta_vivo() and heroe.esta_vivo():
                print(f"\nTu Vida: {heroe.vida_actual}/{heroe.vida_maxima} | Vida del {enemigo.nombre}: {enemigo.vida_actual}/{enemigo.vida_maxima}")
                print("1. Atacar")
                print("2. Huir")
                accion = input("¿Qué deseas hacer?: ")
                
                resultado = juego_service.ejecutar_turno_combate(enemigo, accion)
                print(resultado["mensaje"])
                
                if resultado["combate_finalizado"]:
                    break

            if heroe.vida_actual <= 0:
                print("\nHas sido derrotado. Fin del juego.")
                break
        elif opcion == "2":
            print(f"\n--- ESTADÍSTICAS DE {heroe.nombre.upper()} ---")
            print(f"Nivel: {heroe.nivel}")
            print(f"Vida: {heroe.vida_actual}/{heroe.vida_maxima}")
            print(f"Ataque: {heroe.ataque}")
            print(f"Experiencia: {heroe.experiencia}")
        elif opcion == "3":
            if DataManager.guardar_heroe(heroe):
                print(f"\n¡Partida de {heroe.nombre} guardada con éxito!")
            else:
                print("\nHubo un problema al guardar la partida.")
        elif opcion == "4":
            print("\n¡Gracias por jugar a Pixel Quest! Hasta pronto.")
            break
        else:
            print("\nOpción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    menu_principal()