def test_ajout_vehicule(route_simple, vehicule_exemple):
    route_simple.ajouter_vehicule(vehicule_exemple)
    assert vehicule_exemple in route_simple.vehicules

def test_mise_a_jour_fait_avancer_vehicules(route_simple, vehicule_exemple):
    route_simple.ajouter_vehicule(vehicule_exemple)
    position_initiale = vehicule_exemple.position
    route_simple.mettre_a_jour_vehicules(1)
    assert vehicule_exemple.position > position_initiale