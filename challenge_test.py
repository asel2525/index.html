import unittest
from challenge import nitro_salt

class TestNitroSalt(unittest.TestCase):
    def test_nitro_salt_return_mass(self):
        self.assertEqual(nitro_salt(1000), 10)
        self.assertEqual(nitro_salt(1500), 15)
        self.assertEqual(nitro_salt(800), 8)

    def test_nitro_salt_returns_int(self):
        self.assertInstance(nitro_salt(a), int)

    # def nitro_salt_recives_str_return_int(self):
    #     self.assertEqual(nitro_salt('1000'), 10)

    # def nitro_salt_recives_alpha_returns_zero(self):
    #     self.assertEqual(nitro_salt('abc'), 0)