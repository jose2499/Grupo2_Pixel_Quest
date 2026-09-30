import random
from domain.models import Heroe, Monstruo

class JuegoService:
    def __init__(self, heroe: Heroe):
        self.heroe = heroe

    def explorar(self) -> Monstruo:
        """Genera un evento de exploración y retorna un monstruo enemigo."""
        nombres = ["Slink de las Sombras", "Orco de las Cavernas", "Esqueleto Errante"]
        nombre_enemigo = random.choice(nombres)
        
        # Generamos un monstruo escalado al nivel del héroe
        nivel_enemigo = self.heroe.nivel
        vida_enemigo = nivel_enemigo * 20
        ataque_enemigo = nivel_enemigo * 5
        
        return Monstruo(
            nombre=nombre_enemigo,
            vida_maxima=vida_enemigo,
            vida_actual=vida_enemigo,
            ataque=ataque_enemigo,
            recompensa_exp=nivel_enemigo * 15
        )

    def ejecutar_turno_combate(self, enemigo: Monstruo, accion: str) -> dict:
        """
        Ejecuta un turno de combate.
        Acciones válidas: 'atacar', 'huir'
        """
        resultado = {"mensaje": "", "combate_finalizado": False, "victoria": False}

        if accion == "atacar":
            # Turno del Héroe
            daño_heroe = self.heroe.atacar(enemigo)
            resultado["mensaje"] += f"¡Atacaste a {enemigo.nombre} y le causaste {daño_heroe} de daño!\n"

            if not enemigo.esta_vivo():
                resultado["mensaje"] += f"¡Has derrotado a {enemigo.nombre}!\n"
                self.heroe.ganar_experiencia(enemigo.recompensa_exp)
                resultado["mensaje"] += f"Ganaste {enemigo.recompensa_exp} pts de experiencia."
                resultado["combate_finalizado"] = True
                resultado["victoria"] = True
                return resultado

            # Turno del Enemigo
            daño_enemigo = enemigo.atacar(self.heroe)
            resultado["mensaje"] += f"{enemigo.nombre} te ataca y te causa {daño_enemigo} de daño."

            if not self.heroe.esta_vivo():
                resultado["mensaje"] += "\n¡Has sido derrotado en combate!"
                resultado["combate_finalizado"] = True
                resultado["victoria"] = False

        elif accion == "huir":
            resultado["mensaje"] = "¡Escapaste con éxito del combate!"
            resultado["combate_finalizado"] = True
            resultado["victoria"] = False

        return resultado