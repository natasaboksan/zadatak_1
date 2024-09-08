class Predmet:

    def __init__(self, naziv_predmeta):
        self.naziv_predmeta = naziv_predmeta
    
    def info (self):
        return "Predmet: " + " " + self.naziv_predmeta
    
predmet1 = Predmet (" Programiranje")
print (predmet1.info())


    
        





    