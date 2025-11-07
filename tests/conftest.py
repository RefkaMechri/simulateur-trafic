import pytest
from models.route import Route
from models.vehicule import Vehicule
from models.reseau import ReseauRoutier

@pytest.fixture
def route_simple():
    return Route("A1", longueur=1000, limite_vitesse=30)

@pytest.fixture
def vehicule_exemple(route_simple):
    return Vehicule("V1", route_simple, position=0, vitesse=10)

@pytest.fixture
def reseau_simple(route_simple, vehicule_exemple):
    reseau = ReseauRoutier()
    reseau.ajouter_route(route_simple)
    route_simple.ajouter_vehicule(vehicule_exemple)
    return reseau
