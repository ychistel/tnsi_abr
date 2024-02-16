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
        if not(a.droit==None):
            d.edge(str(a.valeur),str(a.droit.valeur))
            graph_arbre(a.droit)
        else:
            v=c.pop(0)
            d.node(v,style='invis')
            d.edge(str(a.valeur),v,color='blue',style='dashed')
            
def afficher(a,format='png'):
    global d
    f="arbre"+datetime.now().strftime("%d%H%M%S")+".gv"
    d=graphviz.Digraph(filename=f, format=format, edge_attr={'dir': 'none'},\
                       node_attr={'width':'0.4','height':'0.4','nodesep':'10','fontsize':'16'})

    graph_arbre(a.racine)
    #s = graphviz.Source(d, filename="arbre.gv", format="png")
    #d.view()
    # pour les notebook jupyter
    return d
