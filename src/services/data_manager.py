import json
import os
from src.domain.models import Heroe

class DataManager:
    @staticmethod
    def guardar_heroe(heroe: Heroe, filepath: str = "data/partida.json") -> bool:
        """Guarda las estadísticas del héroe en un archivo JSON."""
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        data = {
            "nombre": heroe.nombre,
            "vida_maxima": heroe.vida_maxima,
            "vida_actual": heroe.vida_actual,
            "ataque": heroe.ataque,
            "nivel": heroe.nivel,
            "experiencia": heroe.experiencia,
            "inventario": [item.nombre for item in heroe.inventario]
        }

        try:
            with open(filepath, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error al guardar la partida: {e}")
            return False

    @staticmethod
    def cargar_heroe(filepath: str = "data/partida.json") -> Heroe | None:
        """Carga las estadísticas del héroe desde un archivo JSON."""
        if not os.path.exists(filepath):
            return None

        try:
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)

            heroe = Heroe(
                nombre=data["nombre"],
                vida_maxima=data["vida_maxima"],
                ataque=data["ataque"]
            )
            heroe.vida_actual = data["vida_actual"]
            heroe.nivel = data.get("nivel", 1)
            heroe.experiencia = data.get("experiencia", 0)
            
            return heroe
        except Exception as e:
            print(f"Error al cargar la partida: {e}")
            return None