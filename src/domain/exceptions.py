class DomainError(Exception):
    """Error base para las reglas del dominio del juego."""

    pass


class ValidationError(DomainError):
    """Se usa cuando un dato no cumple una regla del juego."""

    pass


class InvalidActionError(DomainError):
    """Se usa cuando una acción no está permitida en ese momento."""

    pass


class NotEnoughHealthError(DomainError):
    """Se lanza cuando una acción requiere más vida de la disponible."""

    pass


class ItemNotAvailableError(DomainError):
    """Se lanza cuando se intenta usar un objeto que no está disponible."""

    pass


class CharacterNotFoundError(DomainError):
    """Se usa cuando no se encuentra un personaje requerido."""

    pass


class GameOverError(DomainError):
    """Se usa cuando se intenta continuar una partida que ya terminó."""

    pass
