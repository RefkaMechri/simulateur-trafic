class ReseauRoutier:
    """
        Classe professionnelle représentant un réseau routier composé de plusieurs routes.

        Cette classe gère un ensemble de routes et permet la simulation du trafic sur celles-ci.
        Elle fournit des méthodes robustes pour l'ajout de routes et la simulation de l'évolution
        des véhicules sur chaque route durant un intervalle de temps spécifié.

        Attributes
        ----------
        routes : list
            Liste des instances de la classe Route constituant le réseau routier.

        Methods
        -------
        ajouter_route(route: Route) -> None
            Ajoute une instance de Route au réseau routier.

        simuler(delta_t: float) -> None
            Simule l'évolution du trafic sur chaque route du réseau pendant l'intervalle de temps delta_t.
    """
 
    def __init__(self):
        """
            Initialise une nouvelle instance de la classe ReseauRoutier.

            Cette méthode constructeur crée une liste vide destinée à contenir les routes
            qui composeront le réseau routier simulé.
        """
        self.routes = []

    def ajouter_route(self, route):
        """
            Ajoute une route au réseau routier.

            Args:
                route (Route): Instance de la classe Route à ajouter au réseau.
        """
        self.routes.append(route)
    def simuler(self, delta_t: float) -> None:
            """
                Simule l'évolution du trafic sur chaque route du réseau pendant l'intervalle de temps spécifié.

                Cette méthode parcourt toutes les routes du réseau et met à jour l'état des véhicules
                sur chacune d'elles en fonction du paramètre delta_t.

                Args:
                    delta_t (float): Intervalle de temps (en secondes) pour la simulation de l'évolution du trafic.
            """
            for route in self.routes:
                route.mettre_a_jour_vehicules(delta_t)
