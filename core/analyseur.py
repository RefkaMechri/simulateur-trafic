import statistics

from exceptions import StatisticalComputationError

class Analyseur:
    """
    La classe Analyseur permet d'effectuer une analyse statistique du trafic sur un réseau routier.

    Elle propose des méthodes pour calculer des indicateurs tels que la vitesse moyenne, l'écart-type des vitesses,
    la densité de trafic, le temps moyen de parcours et l'identification des zones de congestion sur chaque route.
    """
    def __init__(self, reseau):
        """
        Initialise une instance de la classe Analyseur.

        Args:
            reseau (ReseauRoutier): Instance représentant le réseau routier à analyser.
        """
        self.reseau = reseau

    def calculer_statistiques(self):
        """
        Calcule les statistiques de trafic pour chaque route du réseau.

        Returns:
            dict: Un dictionnaire contenant, pour chaque route, les indicateurs statistiques suivants :
            - vitesse_moyenne (float) : Vitesse moyenne des véhicules sur la route.
            - vitesse_minimale (float) : Vitesse minimale observée sur la route.
            - vitesse_maximale (float) : Vitesse maximale observée sur la route.
            - ecart_type_vitesse (float) : Écart-type des vitesses sur la route.
            - nb_vehicules (int) : Nombre de véhicules présents sur la route.
            - densite (float) : Densité de trafic (nombre de véhicules par unité de longueur).
            - temps_parcours_moyen (float) : Temps moyen de parcours sur la route (en minutes).
            - zone_congestion (bool) : Indique si la route est en situation de congestion.
        """
        stats_par_route = {}

        for route in self.reseau.routes:
            try:
                vehicules_route = route.vehicules
                vitesses = [v.vitesse for v in vehicules_route]
                nb_vehicules = len(vitesses)

                if nb_vehicules == 0:
                    raise StatisticalComputationError(
                        f"Aucun véhicule sur la route {route.nom} (division par zéro impossible)."
                    )

                # Calculs statistiques
                vitesse_moy = sum(vitesses) / nb_vehicules
                vitesse_min = min(vitesses)
                vitesse_max = max(vitesses)
                ecart_type = statistics.pstdev(vitesses) if nb_vehicules > 1 else 0
                densite = nb_vehicules / route.longueur
                temps_moyen = (route.longueur / (vitesse_moy / 60)) if vitesse_moy > 0 else float('inf')
                congestion = vitesse_moy < (0.3 * route.limite_vitesse)

                # Stockage des statistiques
                stats_par_route[route.nom] = {
                    "vitesse_moyenne": round(vitesse_moy, 2),
                    "vitesse_minimale": round(vitesse_min, 2),
                    "vitesse_maximale": round(vitesse_max, 2),
                    "ecart_type_vitesse": round(ecart_type, 2),
                    "densite": round(densite, 2),
                    "temps_parcours_moyen": round(temps_moyen, 2),
                    "zone_congestion": congestion
                }

            except StatisticalComputationError as e:
                print(f"[Erreur Analyse] {e}")
            except Exception as e:
                print(f"[Erreur Inattendue] lors du calcul pour {route.nom} : {e}")

        return stats_par_route