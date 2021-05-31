def coupe_de_la_matrice(joueur, nombre_de_strategies, fonctions_dutilite):
    utilite_du_joueur = []

    # utilite_du_joueur est l'ensemble des coupes de la matrice du jeu
    # selon les strategies du joueur qui nous interesse
    for i in range(nombre_de_strategies):
        utilite_du_joueur.append({})
        for x in fonctions_dutilite:
            x1 = list(x)
            s = x1.pop(joueur-1)
            if s == i+1:
                utilite_du_joueur[i][tuple(x1)] = fonctions_dutilite[x][joueur-1]   #ou joueur - 1

    return utilite_du_joueur


def strategie_dominante(joueur, nombre_de_strategies, fonctions_dutilite):
    fonction_dutilite_du_joueur = coupe_de_la_matrice(joueur, nombre_de_strategies, fonctions_dutilite)

    for s0_condidate in range(len(fonction_dutilite_du_joueur)):
        b = True
        for s0 in range(len(fonction_dutilite_du_joueur)):
            for issue in fonction_dutilite_du_joueur[s0_condidate]:
                if fonction_dutilite_du_joueur[s0_condidate][issue] < fonction_dutilite_du_joueur[s0][issue]:
                    b = False
                    break
            if not b:
                break
        if b:
            return s0_condidate + 1

    return None