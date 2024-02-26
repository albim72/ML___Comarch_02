print("program testowy Python 3")

liczba = [4,6,2,6,2,78,90,-11,103,57,12,34,-56,12,45,101,-3,0]

parzyste = list(filter(lambda x:x%2==0,liczba))

print(parzyste)

cube = list(map(lambda x:x**3,liczba))
print(cube)

import funkcje.bfunkcje as bf

def witaj(imie):
    return f'Miło Cię widzieć {imie}'

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Leon"))
print(bf.konkurs("Anna",78,13))

print(bf.punkty_plus_bonus(78,0.23))
