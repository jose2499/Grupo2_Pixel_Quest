import sys

class MenuCLI:
    def __init__(self):
        self.heroe = None

    def mostrar_banner(self):
        print("=" * 45)
        print("    ⚔️  PIXEL-QUEST: EL MOTOR RPG  ⚔️    ")
        print("=" * 45)

    def iniciar(self):
        self.mostrar_banner()
        while True:
            print("\n--- MENÚ PRINCIPAL ---")
            print("1. Nueva Partida")
            print("2. Cargar Partida")
            print("3. Salir")
            
            opcion = input("\nSelecciona una opción (1-3): ").strip()

            if opcion == "1":
                self.nueva_partida()
            elif opcion == "2":
                print("\n[!] Cargando partida... (Módulo de persistencia pendiente)")
            elif opcion == "3":
                print("\n¡Gracias por jugar a Pixel-Quest! Hasta pronto 👋")
                sys.exit()
            else:
                print("\n❌ Opción inválida. Intenta de nuevo.")

    def nueva_partida(self):
        nombre = input("\nIngresa el nombre de tu héroe: ").strip()
        if not nombre:
            nombre = "Aventurero"
        print(f"\n✨ ¡Bienvenido a la aventura, {nombre}! ✨")
        print("[!] Conectando con los servicios de juego y combate...")

if __name__ == "__main__":
    menu = MenuCLI()
    menu.iniciar()
    