import global_modul


def niveauDeSecuriteStrategie(joueur, strategie):
    liste = []

    for profil_de_strategies in global_modul.fonctions_dutilite.keys():
        if profil_de_strategies[joueur] == strategie:
            liste.append(global_modul.fonctions_dutilite[profil_de_strategies][joueur])

    #print("gains possibles de la strategie ", strategie, " : ", liste)
    return min(liste)

def niveauDeSecuriteJoueur(joueur):
    liste = []
    for i in range(global_modul.nb_strategies_pour_chaque_joeurs[joueur]):
        liste.append(niveauDeSecuriteStrategie(joueur, i+1))
        #print("niveau de securite de la strategie ", i+1, " pour le joueur ", joueur+1, " : ", liste[-1])

    return max(liste)