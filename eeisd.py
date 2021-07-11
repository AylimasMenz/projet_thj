import global_modul
from strategie_dominante import coupe_de_la_matrice


def est_dominee_par(strategie1, strategie2, joueur, fu):
    if strategie1 == strategie2:
        return False
    fonction_dutilite_du_joueur = coupe_de_la_matrice(joueur+1, global_modul.nb_strategies_pour_chaque_joeurs[joueur], fu)

    for issue in fonction_dutilite_du_joueur[strategie1]:
        if fonction_dutilite_du_joueur[strategie2][issue] < fonction_dutilite_du_joueur[strategie1][issue]:
            # ALORS IL EXISTE UN S-i TQ S1 EST MEILLEURE QUE S2
            # ALORS S1 N'EST PAS DOMINEE PAR S2
            return False

    return True

def supprimer_strategie(strategie, joueur, fu):
    for x in list(fu.keys()):
        if x[joueur] == strategie+1:
            fu.pop(x)  # ICI x EST UNE ISSUE OU LE JOUEUR JOUE LA STRATEGIE QU'ON VEUT SUPPRIMER
    return fu

def strategie_n_a_pas_ete_supprimee(strategie, joueur, fu):
    for s in fu.keys():
        if s[joueur] == strategie:
            return True
    return False


def eeisd():
    print(global_modul.nb_strategies_pour_chaque_joeurs)
    print(global_modul.fonctions_dutilite)
    fu = global_modul.fonctions_dutilite.copy()

    b = True
    while b and len(fu) > 0:
        b = False
        for joueur in range(len(global_modul.nb_strategies_pour_chaque_joeurs)):
            print("pour le joueur ", joueur+1)
            for s1 in range(global_modul.nb_strategies_pour_chaque_joeurs[joueur]):
                if not strategie_n_a_pas_ete_supprimee(s1+1, joueur, fu):
                    continue
                for s2 in range(global_modul.nb_strategies_pour_chaque_joeurs[joueur]):
                    if not strategie_n_a_pas_ete_supprimee(s2 + 1, joueur, fu):
                        continue
                    if est_dominee_par(s1, s2, joueur, fu):
                        print(s1+1, " est dominee par ", s2+1)
                        for x in list(fu.keys()):
                            if x[joueur] == s1 + 1:
                                fu.pop(x)  # ICI x EST UNE ISSUE OU LE JOUEUR JOUE LA STRATEGIE QU'ON VEUT SUPPRIMER
                        print("fu devient : ", fu)
                        b = True    # ALORS D'AUTRES ELIMINATIONS POURRAIENT ETRE ENTRAINNÉES PAR CELLE CI

    return [*fu]