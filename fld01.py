# oldalh:int = int(input('egyenlő oldalú 3szög oldalának hossza (cm): '))
# print(f'kerület hetede: {round(oldalh*3/7, 2)} cm')
# print('------------------------')
# kors:int = int(input('kör sugarának hossza (cm): '))
# print(f'kör kerülete: {round(2*kors*3.14, 2)} cm')
# szam:float = 2.35735324
# tj:int = 2
# kerekitett = round(szam, tj)
# print(f"kerekitett:= {kerekitett}")
# print('------------------------')
# csillagsz:int = int(input('hány csillag legyen Béla jutalma a szorgalmas tanulásért?: '))
# print(f'Béla jutalma: {csillagsz * "*"}')
# print('------------------------')

szam01:int = int(input('egyik szám: '))
szam02:int = int(input('másik szám: '))

osszeg:int = 0
for n in range(szam01+1, szam02):
    osszeg += n
    print(n, end=' ')
print(f"\nösszeg: {osszeg}")
print('\n------------------------')

osszeg:int = 0
while True:
    szam:int = int(input('írj be egy számot: '))
    osszeg += szam
    if szam % 10 == 0: break
print(f'számok összege: {osszeg}')