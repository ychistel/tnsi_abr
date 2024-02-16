class Noeud:
    
    def __init__(self, valeur, gauche=None, droit=None):
        # instancie, crée un objet Noeud avec ces trois attributs
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit
    
    def __str__(self):
        # crée une chaine de caratères pour afficher un objet Noeud avec la commande print
        if self.valeur is None:
            return ""
        else:
            return "Noeud("+str(self.valeur) + ","+ str(self.gauche) +","+ str(self.droit)+")"
    
class Arbre:
    
    def __init__(self,racine=None):
        # instancie, crée un objet Arbre avec un seul attribut dont la valeur est un objet Noeud.
        if isinstance(racine,Noeud):
            self.racine = racine
        else:
            self.racine = Noeud(racine)
        
    def __str__(self):
        # appelle la méthode de l'objet Noeud pour être affiché
        return str(self.racine)
        
    def est_vide(self):
        # teste si l'arbre est vide
        return self.racine.valeur is None
    
    def fils_gauche(self):
        # renvoie le contenu d'un noeud fils gauche en arbre
        return Arbre(self.racine.gauche)
        
    def fils_droit(self):
        # renvoie le contenu d'un noeud fils droit en arbre
        return Arbre(self.racine.droit)
         
if __name__ == '__main__':
    from draw_arbre import afficher
    
    n=Noeud(7,Noeud(5,Noeud(8),Noeud(1)),Noeud(4,None,Noeud(6)))
    a=Arbre(n)
    afficher(a,'jpg')
    
    """
    Fonctions utilisant les méthodes d'arbres
    """
    def taille(a):
        if a.est_vide():
            return 0
        else:
            return 1 + taille(a.fils_gauche()) + taille(a.fils_droit())

    def hauteur(a):
        if a.est_vide():
            return -1
        else:
            return 1 + max(hauteur(a.fils_gauche()),hauteur(a.fils_droit()))
    
    def niveau(a,p,nds=[]):
        if p <= hauteur(a):
            if p == 0:
                if not a.est_vide():
                    # on empile dans une liste les valeurs
                    nds.append(a.racine.valeur)
            else:
                niveau(a.fils_gauche(),p-1,nds)
                niveau(a.fils_droit(),p-1,nds)
            return nds
        else:
            return []

    print("Taille de l'arbre:",taille(a))
    print("Hauteur de l'arbre:",hauteur(a))
    for i in range(hauteur(a)+1):
        print("Niveau %s : %s" % (i,niveau(a,i,[])))
    
    