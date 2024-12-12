from traitlets import Integer


class Fraction:
    """Class representing a fraction and operations on it

    Author : Gheysens Theo
    Date : 27 novembre 2024
    This class allows fraction manipulations through several operations.
    """
    def __init__(self, num=0, den=1):
        """
        PRE: num est un entier
        POST:initialise la fraction
        RAISE: ZeroDivisionError si den==0
        """
        if den==0:
            raise ZeroDivisionError
        else:
            if den < 0:
                num = num * -1
                den = den * -1
            divNum = []
            divDen = []
            for i in range(1, abs(num) + 1):
                if num % i == 0:
                    divNum.append(i)
            for j in range(1, den + 1):
                if den % j == 0:
                    divDen.append(j)
            pgcd = 1
            for divisor in divNum:
                if divisor in divDen:
                    pgcd = divisor
            self._num = num // pgcd
            self._den = den // pgcd



    @property
    def numerator(self)->int :
        return self._num

    @property
    def denominator(self)->int :
        return self._den

    # ------------------ Textual representations ------------------

    def __str__(self)->str:
        """Retourne une représentation textuelle de la forme réduite de la fraction

        PRE :
        POST : retourne la fraction sous forme de string
        """
        return f"{self._num}/{self._den}"

    def as_mixed_number(self)->str:
        """Retournez une représentation textuelle de la forme réduite de la fraction sous forme de nombre mixte.

        PRE :
        POST : retourne une forme simplifier de la fraction, constituer de la division et de son reste sous forme de srting
        """
        if self._num>0:
            entier=self._num//self._den
            reste=self._num%self._den
            if reste==0:
                return f'{self._num//self._den}'
            elif entier==0:
                return f"{self._num}/{self._den}"
            else:
                return f"{entier} {reste}/{self._den}"
        else:
            entier=abs(self._num)//self._den
            reste=abs(self._num)%self._den
            if reste==0:
                return f'{self._num//self._den}'
            elif entier==0:
                return f"{self._num}/{self._den}"
            else:
                return f"-{entier} {reste}/{self._den}"


    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Surcharge de l'opérateur + pour les fractions.

         PRE :
         POST : retourne la somme des 2 fractions sous forme de fraction.
         RAISE: TypeError si other n'est pas une instance de fraction
         """
        if not isinstance(other, Fraction):
            raise TypeError("L'autre opérande doit être une instance de Fraction.")
        new_den = self._den * other._den
        new_num = self._num * other._den + other._num * self._den
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        """Surcharge de l'opérateur - pour les fractions.

        PRE :
        POST : retourne la différence des 2 fractions sous forme de fraction
        RAISE: TypeError si other n'est pas une instance de fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("L'autre opérande doit être une instance de Fraction.")
        new_den = self._den * other._den
        new_num = self._num * other._den - other._num * self._den
        if new_num == 0:
            return Fraction(new_num, 1)
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        """Surcharge de l'opérateur * pour les fractions.

        PRE :
        POST : retourne la multiplication des 2 fractions sous forme de fraction
        RAISE: TypeError si other n'est pas une instance de fraction

        """
        if not isinstance(other, Fraction):
            raise TypeError("L'autre opérande doit être une instance de Fraction.")
        new_den = self._den * other._den
        new_num = self._num * other._num
        if new_num == 0:
            return Fraction(new_num, 1)
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        """Surcharge de l'opérateur / pour les fractions.

        PRE :
        POST : retounre la division des 2 fractions sous forme de fraction
        RAISE: TypeError si other n'est pas une instance de fraction
                ZeroDivisionError si other à un numérateur qui vaut 0.
        """
        if not isinstance(other, Fraction):
            raise TypeError("L'autre opérande doit être une instance de Fraction.")
        if other._num==0:
            raise ZeroDivisionError
        new_den = self._den * other._num
        new_num = self._num * other._den
        return Fraction(new_num, new_den)

    def __pow__(self, other):
        """Surcharge de l'opérateur ** pour les fractions.

        PRE :
        POST : retounre la fraction élévé à une certaine puissance
        RAISE: TypeError si other n'est pas une instance de fraction
        """
        if not isinstance(other, int):
            raise TypeError("L'autre opérande doit être un entier.")
        if other<0:
            new_num = self._den ** abs(other)
            new_den = self._num ** abs(other)
            return Fraction(new_num, new_den)
        else:
            new_den = self._den ** other
            new_num = self._num ** other
            return Fraction(new_num, new_den)

    def __eq__(self, other):
        """Surcharge de l'opérateur == pour les fractions.

        PRE :
        POST : retourne true ou false si les 2 fractions sont identique ou non.
        RAISE: TypeError si other n'est pas une instance de fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("L'autre opérande doit être une instance de Fraction.")
        return self._num == other._num and self._den == other._den

    def __float__(self):
        """Renvoie la valeur décimale de la fraction.

        PRE :
        POST : retourne la valeur décimal de la fraction
        """
        return self._num/self._den


    # ------------------ Properties checking  ------------------

    def is_zero(self):
        """Vérifie si la valeur d'une fraction est 0.

        PRE :
        POST : retourne true si une fraction vaut 0
        """
        return self._num == 0

    def is_integer(self):
        """Vérifie si une fraction est un entier (ex : 8/4, 3, 2/2, ...).

        PRE :
        POST : retourne vrai si la fraction est égale à un entier
        """
        return self._num%self._den == 0

    def is_proper(self):
        """Vérifiez si la valeur absolue de la fraction est < 1.

        PRE :
        POST : retourne true si la valeur de la fraction est plus petite que 1
        """
        return abs(self._num) < self._den

    def is_unit(self):
        """Vérifie si le numérateur d'une fraction est 1 dans sa forme réduite.

        PRE :
        POST : retounre true si le numérateur de la fonction simplifier vaut 1
        """
        return abs(self._num)==1


    def is_adjacent_to(self, other):
        """Vérifie si deux fractions diffèrent par une fraction unitaire.

        PRE : 
        POST : retourne true si 2 fractions sont adjacents, soit si la différence des ces 2 fractions est une fraction unitaire
        """
        if not isinstance(other, Fraction):
            raise TypeError("L'autre opérande doit être une instance de Fraction.")

        frac = Fraction(self._num, self._den)
        secfrac= Fraction(other._num, other._den)
        result=(frac-secfrac)

        return result.is_unit()

