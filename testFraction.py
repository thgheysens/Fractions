import unittest

from classeFraction import Fraction
from unittest import TestCase


class TestFraction(TestCase):

    def test_init(self):
        # Test de création normale
        frac1 = Fraction(3, 4)
        self.assertEqual(frac1.numerator, 3)
        self.assertEqual(frac1.denominator, 4)

        # Test avec un dénominateur négatif
        frac2 = Fraction(3, -4)
        self.assertEqual(frac2.numerator, -3)
        self.assertEqual(frac2.denominator, 4)

        # Test avec un zéro au numérateur
        frac3 = Fraction(0, 5)
        self.assertEqual(frac3.numerator, 0)
        self.assertEqual(frac3.denominator, 5)

        # Test avec un dénominateur nul
        self.assertRaises(ZeroDivisionError, Fraction, 3, 0)

    def test_str(self):
        # Représentation textuelle normale
        self.assertEqual(str(Fraction(3, 4)), "3/4")
        self.assertEqual(str(Fraction(4, 4)), "1/1")
        self.assertEqual(str(Fraction(0, 4)), "0/4")
        self.assertEqual(str(Fraction(5, 1)), "5/1")

    def test_as_mixed_number(self):
        # Test conversion en nombre mixte
        self.assertEqual(Fraction(-7, 3).as_mixed_number(), "-2 1/3")
        self.assertEqual(Fraction(-3, 3).as_mixed_number(), "-1")
        self.assertEqual(Fraction(1, 3).as_mixed_number(), "1/3")

    def test_operations(self):
        # Addition
        self.assertEqual(Fraction(1, 2) + Fraction(1, 3), Fraction(5, 6))
        self.assertEqual(Fraction(1, 2) + Fraction(0, 3), Fraction(1, 2))
        self.assertEqual(Fraction(1, 2) + Fraction(-1, 3), Fraction(1, 6))

        # Soustraction
        self.assertEqual(Fraction(3, 4) - Fraction(1, 2), Fraction(1, 4))

        # Multiplication
        self.assertEqual(Fraction(2, 3) * Fraction(3, 4), Fraction(1, 2))

        # Division
        self.assertEqual(Fraction(3, 4) / Fraction(3, 2), Fraction(1, 2))
        self.assertEqual(Fraction(3, 4) / Fraction(-3, 2), Fraction(-1, 2))
        self.assertRaises(ZeroDivisionError, lambda: Fraction(1, 2) / Fraction(0, 1))

        # Puissance
        self.assertEqual(Fraction(1, 2)**2, Fraction(1,4))
        self.assertEqual(Fraction(1, 2) ** -2, Fraction(4, 1))

        # Test des erreurs
        self.assertRaises(TypeError, lambda: Fraction(1, 2) + 5)
         # Division par zéro

    def test_comparison(self):
        # Égalité
        self.assertTrue(Fraction(6, 8) == Fraction(3, 4))
        self.assertFalse(Fraction(3, 4) == Fraction(2, 4))
        self.assertRaises(TypeError, lambda: Fraction(3, 4) == 4)

    def test_is_zero(self):
        self.assertTrue(Fraction(0, 5).is_zero())
        self.assertFalse(Fraction(1, 5).is_zero())

    def test_is_integer(self):
        self.assertTrue(Fraction(4, 2).is_integer())
        self.assertFalse(Fraction(3, 2).is_integer())
        self.assertTrue(Fraction(-6, 3).is_integer())


    def test_is_proper(self):
        self.assertTrue(Fraction(-1, 2).is_proper())
        self.assertTrue(Fraction(1, 2).is_proper())
        self.assertFalse(Fraction(3, 2).is_proper())

    def test_is_unit(self):
        self.assertTrue(Fraction(1, 5).is_unit())
        self.assertFalse(Fraction(2, 5).is_unit())

    def test_is_adjacent_to(self):
        self.assertTrue(Fraction(1, 3).is_adjacent_to(Fraction(2, 3)))
        self.assertTrue(Fraction(-1, 3).is_adjacent_to(Fraction(-2, 3)))
        self.assertFalse(Fraction(1, 4).is_adjacent_to(Fraction(2, 3)))
        self.assertRaises(TypeError, lambda: Fraction(1, 4).is_adjacent_to(4))


if __name__ == '__main__':
    unittest.main()

