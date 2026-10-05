import unittest
from src.domain.exceptions import (
    DomainError,
    ValidationError,
    InvalidActionError,
    NotEnoughHealthError
)

class TestDomainExceptions(unittest.TestCase):
    def test_domain_error_inheritance(self):
        err = ValidationError("Dato invalido")
        self.assertIsInstance(err, DomainError)

    def test_not_enough_health_error(self):
        err = NotEnoughHealthError("Vida insuficiente")
        self.assertIsInstance(err, DomainError)

if __name__ == "__main__":
    unittest.main()