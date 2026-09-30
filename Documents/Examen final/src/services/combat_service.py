import random
from src.domain.models import Heroe, Monstruo


class CombatService:
    def generar_monstruo_aleatorio(self, nivel_heroe: int) -> Monstruo:
        """
        Genera un monstruo con nombre y estadísticas escaladas al nivel del héroe.
        """
        tipos_monstruos = [
            {"nombre": "Trasgo", "mult_hp": 8, "mult_atk": 2},
            {"nombre": "Orco", "mult_hp": 12, "mult_atk": 3},
            {"nombre": "Dragón", "mult_hp": 20, "mult_atk": 5},
        ]
        
        plantilla = random.choice(tipos_monstruos)
        salud = plantilla["mult_hp"] * nivel_heroe
        ataque = plantilla["mult_atk"] * nivel_heroe
        exp_recompensa = nivel_heroe * 50

        return Monstruo(
            nombre=plantilla["nombre"],
            salud=salud,
            salud_maxima=salud,
            ataque=ataque,
            experiencia_otorgada=exp_recompensa
        )

    def ejecutar_turno(self, heroe: Heroe, monstruo: Monstruo, accion: str) -> dict:
        """
        Maneja las acciones 'atacar', 'huir' o 'usar_item' y retorna un diccionario
        con el resumen de los eventos del turno.
        """
        dano_infligido = 0
        dano_recibido = 0
        exp_ganada = 0
        estado_combate = "en_progreso"
        mensaje = ""

        accion = accion.lower().strip()

        if accion == "atacar":
            dano_infligido = getattr(heroe, "ataque", 10)
            monstruo.salud -= dano_infligido
            
            if monstruo.salud <= 0:
                monstruo.salud = 0
                estado_combate = "victoria"
                exp_ganada = getattr(monstruo, "experiencia_otorgada", 50)
                mensaje = f"Has derrotado a {monstruo.nombre}."
            else:
                mensaje = f"Atacaste a {monstruo.nombre} e infligiste {dano_infligido} de daño."

        elif accion == "huir":
            exito_huida = random.choice([True, False])
            if exito_huida:
                estado_combate = "escapado"
                mensaje = "Lograste escapar con éxito del combate."
                return {
                    "dano_infligido": 0,
                    "dano_recibido": 0,
                    "estado_combate": estado_combate,
                    "experiencia_ganada": 0,
                    "mensaje": mensaje
                }
            else:
                mensaje = "Intentaste huir pero fallaste."

        elif accion == "usar_item":
            curacion = 20
            salud_max = getattr(heroe, "salud_maxima", 100)
            heroe.salud = min(salud_max, heroe.salud + curacion)
            mensaje = f"Usaste un ítem y recuperaste {curacion} puntos de salud."

        else:
            mensaje = f"Acción '{accion}' no válida. Perdiste el turno."

        # Contraataque del monstruo si sigue vivo y no se ha escapado
        if estado_combate == "en_progreso":
            dano_recibido = getattr(monstruo, "ataque", 5)
            heroe.salud -= dano_recibido
            
            if heroe.salud <= 0:
                heroe.salud = 0
                estado_combate = "derrota"
                mensaje += f" {monstruo.nombre} te atacó e infligió {dano_recibido} de daño. Has sido derrotado."
            else:
                mensaje += f" {monstruo.nombre} te atacó e infligió {dano_recibido} de daño."

        return {
            "dano_infligido": dano_infligido,
            "dano_recibido": dano_recibido,
            "estado_combate": estado_combate,
            "experiencia_ganada": exp_ganada,
            "mensaje": mensaje
        }