class Etudiant:
 
    def __init__(self, nom, prenom, age, cne, moyenne):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.cne = cne
        self.moyenne = moyenne
 
    def __repr__(self):
        return '{' + self.nom + ', ' + self.prenom + ', ' + str(self.age) + ', ' + str(self.cne) +', ' + str(self.moyenne) +'}'
 
if __name__ == '__main__':
    # list of Etudiant objects 
    Etudiants = [
        Etudiant('el-ayoubi', 'tarik', 25, 12222223, 14),
        Etudiant('nasser', 'mohamed', 30, 489238923, 16),
        Etudiant('el-harti', 'zouhir', 18, 12222233, 11),
        Etudiant('massiri', 'tawfik', 40, 1334342223, 18)
    ]
 
    # sort list by `age` in the natural order
    Etudiants.sort(key=lambda x: x.age)
 
    # output: [{el-harti, zouhir, 18, 12222233, 11}, {el-ayoubi, tarik, 25, 12222223, 14}, {nasser, mohamed, 30, 489238923, 16}, {massiri, tawfik, 40, 1334342223, 18}]
    print(Etudiants)
 
    # sort list by `moyenne` in the natural order
    Etudiants.sort(key=lambda x: x.moyenne)
 
    # output: [{el-harti, zouhir, 18, 12222233, 11}, {el-ayoubi, tarik, 25, 12222223, 14}, {nasser, mohamed, 30, 489238923, 16}, {massiri, tawfik, 40, 1334342223, 18}]
    print(Etudiants)
 