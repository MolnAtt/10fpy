def szoroz(a:int, b:int) -> int:  # type hinteket lehetőleg használjunk!
    return a*b

def van_e_negativ(t:list[int]):
    for elem in t:
        if elem < 0:
            return True
    return False

def van_e_negativ_2(t:list[int]):
    i = 0
    while i<len(t) and not t[i] < 0:
        i+=1
    return i<len(t)


a = input('Adj meg két számot!\n')
b = input('Jöhet a másik\n')
print(f'a két szám összege: {int(a)+int(b)}') # ez egy f-string, amit c#-ban interpolált stringnek hívnak.
print(f'a két szám szorzata: {szoroz(int(a), int(b))}')


""" Ez a docstring
StreamReader f = new StreamReader("input.txt", Encoding.Default);

...

f.Close()
"""

t = []
f = open('input.txt', 'r', encoding='utf8')
for sor in f:
    print(sor.strip()) # strip: leszedi a whitespace-t a string két végéről!
    t.append(int(sor))
f.close()

print(f'1. feladat: Hány eleme van a sorozatnak? {len(t)}')
print(f'2. feladat: Van-e a sorozatban negatív szám? {van_e_negativ(t)} avagy {van_e_negativ_2(t)}')

def negnulla(t:list[int]):
    for i in range(1, len(t)):
        if t[i-1] < 0 and t[i] == 0:
            return True
        return False


print(f'9. feladat: Van-e a sorozatban olyan negatív szám, amelyet nulla követ?: {negnulla(t)}')

