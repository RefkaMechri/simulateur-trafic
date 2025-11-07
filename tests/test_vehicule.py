def test_avancement_modifie_position(vehicule_exemple):
    vehicule_exemple.avancer(5)  # delta_t = 5
    expected_position = 10 * 5 / 60  # selon la formule dans avancer()
    assert abs(vehicule_exemple.position - expected_position) < 1e-6


def test_vehicule_ne_depasse_pas_longueur_route(vehicule_exemple, route_simple):
    vehicule_exemple.position = 990
    vehicule_exemple.avancer(2)
    assert vehicule_exemple.position <= route_simple.longueur

def test_changement_de_route_remet_position_a_zero(vehicule_exemple, route_simple):
    nouvelle_route = route_simple.__class__("B2", longueur=500, limite_vitesse=40)
    vehicule_exemple.changer_de_route(nouvelle_route)
    assert vehicule_exemple.position == 0
    assert vehicule_exemple.route.nom == "B2"