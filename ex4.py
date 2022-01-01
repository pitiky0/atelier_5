class Point:
# classe de point du plan
    def __init__(self, x=0.0, y=0.0):
        # Initialisation avec valeurs par defaut
        self.x = float(x)
        self.y = float(y)
class Segment:
    def __init__(self, x1, y1, x2, y2):
        # L'initialisation utilise deux objets Point
        self.orig = Point(x1, y1)
        self.extrem = Point(x2, y2)
    def __str__(self):
        #  Representation d'un objet segment.
        return ("Segment : [({0}, {1}), ({2}, {3})]".format(self.orig.x, self.orig.y, self.extrem.x, self.extrem.y))
if __name__ == '__main__':
    s = Segment(1, 2, 3, 4)
    print(s)