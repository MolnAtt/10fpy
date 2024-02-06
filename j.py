class Tanulo:
    def __init__(self, id, nev, matcsop, ancsop, nyelv2, nem, egyuttlakok, testverek) -> None:
        self.id = id
        self.nev = nev
        self.matcsop = matcsop
        self.ancsop = ancsop
        self.nyelv2 = nyelv2
        self.nem = nem
        self.egyuttlakok = egyuttlakok
        self.testverek = testverek

    def __str__(self) -> str:
        return self.nev
    
lista = []

with open('j.txt', 'r', encoding='utf8') as f:
    for sor in f:
        # sor:  1;Avon Mór;alfa;4. Kis;német;F;4;1\n
        szepsor = sor.strip() # 1;Avon Mór;alfa;4. Kis;német;F;4;1
        sortomb = szepsor.split(';') # ['1', 'Avon Mór', 'alfa', '4. Kis', 'német', 'F', '4', '1']
        lista.append(Tanulo(sortomb[0], sortomb[1], sortomb[2], sortomb[3], sortomb[4], sortomb[5], int(sortomb[6]), int(sortomb[7])))

print(len(lista))

