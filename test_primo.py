import unittest
from primo import es_primo

class TestPrimo(unittest.TestCase):
    def test_primos(self):
        self.assertTrue(es_primo(2))
        self.assertTrue(es_primo(3))
        self.assertTrue(es_primo(11))
        self.assertTrue(es_primo(1))
        self.assertFalse(es_primo(4))
        self.assertFalse(es_primo(9))

if __name__ == '_main_':
    unittest.main()