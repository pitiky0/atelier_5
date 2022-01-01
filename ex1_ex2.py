class Vecteur2D:
# classe de vecteur du plan
    def __init__(self, x=0, y=0):
        # Initialisation avec valeurs par defaut
        self.x = x
        self.y = y

    def __str__(self):
        # Affichage d'un Vecteur2D :
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        # Addition de deux vecteur2D : 
        return Vecteur2D(self.x + other.x, self.y + other.y)

if __name__ == '__main__':
    v1 = Vecteur2D()
    v2 = Vecteur2D(10, 20)
    # affichage classique :
    print("Les coordonnée de ce vecteur sont: ({0},{1})".format(v1.x, v1.y))
    print("Les coordonnée de ce vecteur sont: ({0},{1})".format(v2.x, v2.y))
    print("\n")
    # affichage par la methode __str__ :
    print("Les coordonnée de ce vecteur sont:{0}" .format(v1))
    print("Les coordonnée de ce vecteur sont:{0}" .format(v2))
    print("\n")
    # Addition vectorielle :
    print("la somme de deux victeurs est {0}" .format(v1+v2))