class Noeud:
    
    def __init__(self, valeur=None, gauche=None, droit=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit
    
    def est_vide(self):
        return self.valeur is None
    
    def __str__(self):
        if self.valeur is None:
            return ""
        else:
            return "Noeud("+str(self.valeur) + ","+ str(self.gauche) +","+ str(self.droit)+")"
    
class Arbre:
    
    def _