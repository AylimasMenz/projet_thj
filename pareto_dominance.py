import global_modul


def n_est_pas_pareto_domine_par(profil1, profil2):
    # RETOURNE VRAI SI profil1 N'EST PAS PARETO DOMINE PAR profil2
    # FAUX SI NON
    b = False
    for i in range(len(global_modul.nb_strategies_pour_chaque_joeurs)):
        if global_modul.fonctions_dutilite[profil2][i] >= global_modul.fonctions_dutilite[profil1][i]:
            if global_modul.fonctions_dutilite[profil2][i] > global_modul.fonctions_dutilite[profil1][i]:
                b = True
        else:
            return True
    return not b


def determinationDesOptimumsDePareto():
    optimumsDePareto = set()
    for profil_de_strategies in global_modul.fonctions_dutilite.keys():
        b = True
        for ps in global_modul.fonctions_dutilite.keys():
            if not n_est_pas_pareto_domine_par(profil_de_strategies, ps):
                b = False
                break
        if b:
            optimumsDePareto.add(profil_de_strategies)

    return optimumsDePareto
