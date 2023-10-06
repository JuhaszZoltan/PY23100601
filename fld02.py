szamlalo:int = 1
while szamlalo <= 10:
    allat:str = input(f'írd be az {szamlalo}. állatfajtát: ')
    szamlalo += 1
    if allat == 'fotel': break
else: print('ügyes vagy, sikerült 10 állatot beírod anélkül, hogy "fotel"!')

# ciklushoz tartozó "else" akkor fut le, ha a ciklusban sosem volt "break"


