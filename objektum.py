class Tanulo:
    def __init__(self, nev, magassag):
        self.nev = nev
        self.magassag = magassag
        self.jofej = False

    def __str__(self) -> str:
        return self.nev + f"({self.magassag})"
    
    def koszon(self):
        print(f"Szia! {self.nev} vagyok")

    def letszam():
        return 10

t = Tanulo("Laci", 180)

print(t)

t.koszon()
Tanulo.koszon(t)





a = "Béla"

a = 5

