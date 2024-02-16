import graphviz
from datetime import datetime

c=[chr(i) for i in range(199,399)]

def caractere_invisible():
    v=c.pop(0)
    c.append(v)
    return v
    
def graph_arbre(a):
    if not(a.valeur==None):
        if not(a.gauche==None):
            d.edge(str(a.valeur),str(a.gauche.valeur))
            graph_arbre(a.gauche)
        else:
            v=c.pop(0)
            d.node(v,style='invis')
            d.edge(str(a.valeur),v,color='red',style='dashed')
        if not(a.dro