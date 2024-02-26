print("program testowy Python 3")

liczba = [4,6,2,6,2,78,90,-11,103,57,12,34,-56,12,45,101,-3,0]

parzyste = list(filter(lambda x:x%2==0,liczba))

print(parzyste)

cube = list(map(lambda x:x**3,liczba))
print(cube)
