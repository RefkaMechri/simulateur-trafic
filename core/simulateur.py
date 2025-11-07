
import json
from exceptions import ConfigFileError, SimulationError
from models.route import Route
from models.vehicule import Vehicule
from models.reseau import ReseauRoutier
from core.analyseur import Analyseur
from io_utils.affichage import Affichage
from io_utils.export import Export

class Simulateur:
    """
        Simulateur de trafic routier.

        Cette classe gère le cycle principal de la simulation, y compris le chargement de la configuration,
        l'exécution des tours de simulation, l'analyse des statistiques, l'affichage et l'export des résultats.
    """
    def __init__(self, fichier_config):
        """
            Initialise une instance de la classe Simulateur.

            Args:
                fichier_config (str): Chemin vers le fichier de configuration JSON.

            Attributs:
                reseau (ReseauRoutier): Instance du réseau routier simulé.
                analyseur (Analyseur): Outil d'analyse des statistiques de simulation.
                affichage (Affichage): Outil d'affichage des résultats.
                export (Export): Outil d'export des statistiques.
        """
        
        self.reseau = ReseauRoutier()
        self.analyseur = Analyseur(self.reseau)
        self.affichage = Affichage()
        self.export = Export()
        self.charger_config(fichier_config)

    def charger_config(self, fichier):
        """
            Charge la configuration du simulateur à partir d'un fichier JSON.

            Args:
                fichier (str): Chemin vers le fichier de configuration JSON.
        """
        
        try:
            with open(fichier, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            raise ConfigFileError(fichier, "Fichier non trouvé.")
        except json.JSONDecodeError:
            raise ConfigFileError(f"Le fichier {fichier} est mal formé.")

        for r in data.get("routes", []):
            self.reseau.ajouter_route(Route(r["nom"], r["longueur"], r["limite_vitesse"]))

        for v in data.get("vehicules", []):
            try:
                route = self.reseau.routes[v["route"]]
                vehicule = Vehicule(v["id"], route, v["position"], v["vitesse"])
                route.ajouter_vehicule(vehicule)
            except IndexError:
                print(f"[Erreur Config] La route {v['route']} n'existe pas pour le véhicule {v['id']}.")
            except KeyError as e:
                print(f"[Erreur Config] Champ manquant : {e}")
                
    def lancer_simulation(self, n_tours, delta_t):
        """
            Lance la simulation pour un nombre spécifié de tours avec un intervalle de temps donné.
    
            Args:
                n_tours (int): Nombre de tours de simulation à exécuter.
                delta_t (float): Intervalle de temps (en minutes) pour chaque tour de simulation.
        """
        try:
            if n_tours <= 0 or delta_t <= 0:
                raise ValueError("Nombre d’itérations ou delta_t invalide.")
            
            print(f"Début de la simulation ({n_tours} tours, delta_t={delta_t})")
            for t in range(n_tours):
                print(f"--- Tour {t+1}/{n_tours} ---")
                self.reseau.simuler(delta_t)
                stats = self.analyseur.calculer_statistiques()
                self.affichage.afficher(stats)
                self.export.sauvegarder(stats)
            print("Simulation terminée.")
        except (ValueError, SimulationError) as e:
            print(f"[Erreur Simulation] {e}")