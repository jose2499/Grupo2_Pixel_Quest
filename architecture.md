# Arquitectura del Proyecto: Pixel-Quest (Motor RPG)

## Diagrama de Clases UML (Mermaid)

```mermaid
classDiagram
    %% Capa de Dominio
    class Personaje {
        -String nombre
        -int vida_maxima
        -int vida_actual
        -int ataque
        +esta_vivo() bool
        +recibir_dano(dano) void
    }

    class Heroe {
        -int nivel
        -int experiencia
        -List inventario
        +atacar(objetivo) void
        +ganar_experiencia(exp) void
        +agregar_item(item) void
    }

    class Monstruo {
        -int recompensa_exp
        +atacar(objetivo) void
    }

    class Item {
        -String nombre
        -String tipo
        -int efecto_valor
    }

    Personaje <|-- Heroe
    Personaje <|-- Monstruo
    Heroe "1" o-- "*" Item : posee

    %% Capa de Servicios
    class JuegoService {
        +crear_heroe(nombre) Heroe
        +generar_monstruo_aleatorio() Monstruo
        +ejecutar_turno_combate(heroe, monstruo, accion) Tuple
    }

    class DataManager {
        +guardar_partida(heroe, ruta) void
        +cargar_partida(ruta) Heroe
    }

    %% Capa de Interfaz
    class MenuCLI {
        +mostrar_menu_principal() void
        +iniciar_exploracion(heroe) void
        +mostrar_combate(heroe, monstruo) void
    }

    JuegoService ..> Heroe : gestiona
    JuegoService ..> Monstruo : gestiona
    DataManager ..> Heroe : serializa
    MenuCLI ..> JuegoService : utiliza
    MenuCLI ..> DataManager : utiliza
    ´´´