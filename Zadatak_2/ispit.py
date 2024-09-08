from predmet import *

class Ispit (Predmet):

    def __init__(self, naziv_predmeta, datum_odrzavanja_ispita):
        super().__init__(naziv_predmeta)
        self.datum_odrzavanja_ispita = datum_odrzavanja_ispita

    def str (self):
        return "Ispit: " + " " + self.naziv_predmeta + " " " - zakazani datum polaganja ispita je " + self.datum_odrzavanja_ispita
ispit1 = Ispit ("Programiranje", "8.6.2024.")
print(ispit1.str())
