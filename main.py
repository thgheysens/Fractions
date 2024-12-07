from classeFraction import Fraction

f1 = Fraction(-8, 24)
f2 = Fraction(4, 3)
f3 = Fraction(3, 3)
f4 = f1+ Fraction(2, 3)
f5= f1-f2
f6= f1*f2
f7=f1/f2
f8= f1**2
print(f'11 La version reduite de Fraction(-8, 24) est {f1}.')
print(f'12 L\'addition de Fraction(-8, 24) et Fraction(2, 3) est {f4}.')
print(f'13 La soustraction à Fraction(-8, 24) de Fraction(4, 3) est {f5}.')
print(f'14 La multiplication de Fraction(-8, 24) et Fraction(4, 3) est {f6}.')
print(f'15 La division de Fraction(-8, 24) par Fraction(4, 3) est {f7}.')
print(f'16 Si f1 = Fraction(-8, 24) et f2 = Fraction(3, 3) sont égaux, {f1==f2}.')
print(f'18 Teste la fonction as mixed_number, {f2.as_mixed_number()}.')
print(f'19 Teste la fonction float, {float(f1)}.')
print(f'20 Teste si Fraction(-8, 24) est une fraction unitaire, {f1.is_unit()}.')
print(f'21 Vérifie si Fraction(4, 3) et f3 = Fraction(3, 3) fonctions sont adjacente, {f2.is_adjacent_to(f3)}.')
