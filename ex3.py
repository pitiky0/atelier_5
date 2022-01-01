class Rectangle:
    def __init__(self, longueur=0, largeur=0):
        self.longueur = longueur
        self.largeur = largeur
        self.nom = "rectangle"
    
    def __str__(self):
        # Affichage des caracteristiques d'un rectangle :
        return "Longueur = {0}, Largeur = {1}".format(self.longueur, self.largeur)
    
    def surface(self):
        return self.longueur*self.largeur
class Carre(Rectangle):
    def __init__(self, cote=0):
        Rectangle.__init__(self, cote, cote)
        self.nom = "carré"

if __name__ == '__main__':
    rec = Rectangle(12, 6)
    car = Carre(8)
    print("Je suis le " + rec.nom )
    print("Mes dimantion sont : {0}" .format(rec) )
    print("Ma surface égale à: " + str(rec.surface()) )
    print("\n")
    print("Je suis le " + car.nom )
    print("Mes dimantion sont : {0}" .format(car) )
    print("Ma surface égale à: " + str(car.surface()) )