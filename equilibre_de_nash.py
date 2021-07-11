import global_modul

def est_un_equilibre_de_nash(profil_de_strategies):
    for joueur in range(len(global_modul.nb_strategies_pour_chaque_joeurs)):
        for strategie in range(global_modul.nb_strategies_pour_chaque_joeurs[joueur]):
            autre_profil = list(profil_de_strategies)
            autre_profil[joueur] = strategie + 1
            if global_modul.fonctions_dutilite[tuple(autre_profil)][joueur] > global_modul.fonctions_dutilite[profil_de_strategies][joueur]:
                return False
    return True

def determinationDesEquilibresDeNash():
    equilibresDeNash = set()
    for profil_de_strategies in global_modul.fonctions_dutilite.keys():
        if est_un_equilibre_de_nash(profil_de_strategies):
            equilibresDeNash.add(profil_de_strategies)

    return equilibresDeNash