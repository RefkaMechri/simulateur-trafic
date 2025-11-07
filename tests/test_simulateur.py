import pytest
from core.simulateur import Simulateur

def test_initialisation_depuis_fixture(reseau_simple):
    simu = Simulateur.__new__(Simulateur)
    simu.reseau = reseau_simple

    # Vérifie que la route "A1" existe dans le réseau
    assert len(simu.reseau.routes) == 1
    assert simu.reseau.routes[0].nom == "A1"

def test_simulation_sans_erreur_fixture(reseau_simple):
    simu = Simulateur.__new__(Simulateur)
    simu.reseau = reseau_simple

    # Lance une simulation sur 5 tours, delta_t = 1
    simu.reseau.simuler(delta_t=1)

    # Vérifie qu'au moins un véhicule a avancé
    vehicule = simu.reseau.routes[0].vehicules[0]
    assert vehicule.position > 0
