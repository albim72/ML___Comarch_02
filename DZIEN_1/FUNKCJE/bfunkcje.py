def konkurs(imie,punkty,miejsce):
    return f'uczestnik konkursu: {imie}, liczba punktów: {punkty}, miejsce: {miejsce}.'


def punkty_plus_bonus(punkty,bonus):
    if punkty >65:
        return punkty*(1-bonus)
    else:
        return punkty
