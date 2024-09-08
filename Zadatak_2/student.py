class Student:
   
    def __init__(self, ime, prezime, brIndeksa ):
        self.ime = ime
        self.prezime = prezime
        self.brIndeksa = brIndeksa

    def info (self):  
        return "Student: " + " " + self.ime + " " +self.prezime + " " +self.brIndeksa
   
student1 = Student ("Ana", "Jovanovic", "123/2024")
student2 = Student ("Luka", "Lekic", "122/2024")

print (student1.info())
print (student2.info())







      
