def test_ajout_de_routes(reseau_simple, route_simple):
    assert route_simple in reseau_simple.routes

def test_mise_a_jour_de_toutes_les_routes(reseau_simple):
    # Simule 1 unité de temps (par exemple 1 seconde)
    delta_t = 1.0
    reseau_simple.simuler(delta_t)
    # Vérifie que le véhicule a avancé sur la première route
    vehicule = reseau_simple.routes[0].vehicules[0]
    assert vehicule.position > 0

