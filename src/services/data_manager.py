import json
import os
from typing import Dict, Any, Optional


class DataManager:
    """Clase encargada de gestionar la carga y guardado de datos en formato JSON."""

    def __init__(self, filepath: str = "data/savegame.json"):
        self.filepath = filepath

    def save_game(self, data: Dict[str, Any]) -> bool:
        """Guarda un diccionario de datos en el archivo JSON especificado."""
        try:
            folder = os.path.dirname(self.filepath)
            if folder and not os.path.exists(folder):
                os.makedirs(folder, exist_ok=True)

            with open(self.filepath, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            print(f"[DataManager] Partida guardada exitosamente en {self.filepath}")
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
            print(f"[DataManager] Error al guardar la partida: {e}")
            return False

    def load_game(self) -> Optional[Dict[str, Any]]:
        """Carga y retorna los datos guardados en el archivo JSON."""
        if not os.path.exists(self.filepath):
            print(f"[DataManager] El archivo {self.filepath} no existe.")
            return None


        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
            print(f"[DataManager] Partida cargada exitosamente desde {self.filepath}")
            return data

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
            print(f"[DataManager] Error al cargar la partida: {e}")
            return None


if __name__ == "__main__":
    # Prueba rápida de funcionamiento local
    manager = DataManager("data/test_save.json")
    mock_data = {"player": "Hero", "level": 5, "score": 1200}

    print("--- Probando guardado ---")
    manager.save_game(mock_data)

    print("\n--- Probando carga ---")
    loaded = manager.load_game()
    print("Datos cargados:", loaded)

    # Limpieza del archivo de prueba
    if os.path.exists("data/test_save.json"):
        os.remove("data/test_save.json")