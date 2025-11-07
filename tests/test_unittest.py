# tests/test_simulateur_unittest.py

import unittest
from models.vehicule import Vehicule
from models.route import Route
from models.reseau import ReseauRoutier
from core.simulateur import Simulateur

# ----------------------------
# Classe de test pour les véhicules
# ----------------------------
class TestVehicule(unittest.TestCase):

    def setUp(self):
        self.route = Route("A1", longueur=1000, limite_vitesse=30)
        self.vehicule = Vehicule("V1", self.route, position=0, vitesse=10)

    def test_avancer(self):
        self.vehicule.avancer(5)  # delta_t = 5
        # Adapter selon l'unité dans Vehicule
        self.assertTrue(self.vehicule.position > 0)

    def test_changement_de_route(self):
        nouvelle_route = Route("B2", longueur=500, limite_vitesse=20)
        self.vehicule.changer_de_route(nouvelle_route)
        self.assertEqual(self.vehicule.route, nouvelle_route)
        self.assertEqual(self.vehicule.position, 0)

# ----------------------------
# Classe de test pour les routes
# ----------------------------
class TestRoute(unittest.TestCase):

    def setUp(self):
        self.route = Route("A1", longueur=1000, limite_vitesse=30)
        self.vehicule = Vehicule("V1", self.route, position=0, vitesse=10)
        self.route.ajouter_vehicule(self.vehicule)

    def test_ajout_vehicule(self):
        self.assertIn(self.vehicule, self.route.vehicules)

    def test_mise_a_jour_vehicules(self):
        self.route.mettre_a_jour_vehicules(delta_t=5)
        self.assertTrue(self.vehicule.position > 0)

# ----------------------------
# Classe de test pour le réseau
# ----------------------------
class TestReseau(unittest.TestCase):

    def setUp(self):
        self.route = Route("A1", longueur=1000, limite_vitesse=30)
        self.vehicule = Vehicule("V1", self.route, position=0, vitesse=10)
        self.route.ajouter_vehicule(self.vehicule)

        self.reseau = ReseauRoutier()
        self.reseau.ajouter_route(self.route)

    def test_ajout_de_routes(self):
        self.assertIn(self.route, self.reseau.routes)

    def test_simulation_reseau(self):
        self.reseau.simuler(delta_t=5)
        self.assertTrue(self.vehicule.position > 0)

# ----------------------------
# Classe de test pour le simulateur
# ----------------------------
class TestSimulateur(unittest.TestCase):

    def setUp(self):
        # Création manuelle du réseau pour éviter les fichiers JSON
        self.route = Route("A1", longueur=1000, limite_vitesse=30)
        self.vehicule = Vehicule("V1", self.route, position=0, vitesse=10)
        self.route.ajouter_vehicule(self.vehicule)

        self.reseau = ReseauRoutier()
        self.reseau.ajouter_route(self.route)

        self.simu = Simulateur.__new__(Simulateur)
        self.simu.reseau = self.reseau

    def test_initialisation_reseau(self):
        self.assertEqual(len(self.simu.reseau.routes), 1)
        self.assertEqual(self.simu.reseau.routes[0].nom, "A1")

    def test_simulation_sans_erreur(self):
        self.simu.reseau.simuler(delta_t=5)
        self.assertTrue(self.vehicule.position > 0)

# ----------------------------
# Point d'entrée
# ----------------------------
if __name__ == "__main__":
    unittest.main()
