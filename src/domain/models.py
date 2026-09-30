from typing import List


class Item:
    """Representa un objeto que puede pertenecer al inventario de un héroe."""

    def __init__(self, nombre: str, tipo: str, efecto_valor: int) -> None:
        self.nombre = nombre
        self.tipo = tipo
        self.efecto_valor = efecto_valor


class Personaje:
    """Clase base para los personajes del juego."""

    def __init__(
        self,
        nombre: str,
        vida_maxima: int,
        vida_actual: int,
        ataque: int
    ) -> None:
        self.nombre = nombre
        self.vida_maxima = vida_maxima
        self.vida_actual = vida_actual
        self.ataque = ataque

    def esta_vivo(self) -> bool:
        """Indica si el personaje todavía tiene vida."""
        return self.vida_actual > 0

    def recibir_dano(self, dano: int) -> None:
        """Reduce la vida del personaje según el daño recibido."""
        if dano < 0:
            raise ValueError("El daño no puede ser negativo.")

        self.vida_actual = max(0, self.vida_actual - dano)


class Heroe(Personaje):
    """Representa al héroe controlado por el jugador."""

    def __init__(
        self,
        nombre: str,
        vida_maxima: int,
        vida_actual: int,
        ataque: int
    ) -> None:
        super().__init__(nombre, vida_maxima, vida_actual, ataque)

        self.nivel: int = 1
        self.experiencia: int = 0
        self.inventario: List[Item] = []

    def atacar(self, objetivo: Personaje) -> None:
        """Ataca a otro personaje."""
        objetivo.recibir_dano(self.ataque)

    def ganar_experiencia(self, exp: int) -> bool:
        """
        Añade experiencia al héroe.

        El héroe sube de nivel cada 50 puntos de experiencia
        correspondientes al siguiente nivel.

        Retorna True si subió de nivel.
        """
        if exp < 0:
            raise ValueError("La experiencia no puede ser negativa.")

        self.experiencia += exp
        subio_de_nivel = False

        while self.experiencia >= self.nivel * 50:
            self.nivel += 1
            self.vida_maxima += 10
            self.vida_actual = self.vida_maxima
            self.ataque += 2
            subio_de_nivel = True

        return subio_de_nivel

    def agregar_item(self, item: Item) -> None:
        """Agrega un objeto al inventario del héroe."""
        self.inventario.append(item)


class Monstruo(Personaje):
    """Representa a un monstruo enemigo."""

    def __init__(
        self,
        nombre: str,
        vida_maxima: int,
        vida_actual: int,
        ataque: int,
        recompensa_exp: int
    ) -> None:
        super().__init__(nombre, vida_maxima, vida_actual, ataque)
        self.recompensa_exp = recompensa_exp

    def atacar(self, objetivo: Personaje) -> None:
        """Ataca a otro personaje."""
        objetivo.recibir_dano(self.ataque)