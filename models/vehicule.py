from exceptions import InvalidPositionError, NegativeSpeedError, RouteInexistanteError


class Vehicule:
    """
        Classe représentant un véhicule circulant sur une route.

        Attributes:
            identifiant (str): Identifiant unique du véhicule.
            route (Route): Instance de la route sur laquelle le véhicule circule.
            position (float): Position actuelle du véhicule sur la route (en mètres).
            vitesse (float): Vitesse actuelle du véhicule (en km/h).
    """
    
    def __init__(self, identifiant, route, position=0.0, vitesse=0.0):
        """
            Initialise une nouvelle instance de la classe Vehicule.

            Args:
                identifiant (str): Identifiant unique du véhicule.
                route (Route): Instance de la route sur laquelle le véhicule circule.
                position (float, optional): Position initiale du véhicule sur la route (en mètres). Par défaut à 0.0.
                vitesse (float, optional): Vitesse initiale du véhicule (en km/h). Par défaut à 0.0.
        """
        self.identifiant = identifiant
        self.route = route
        self.position = position
        self.vitesse = vitesse

    def avancer(self, delta_t):
        """
            Fait avancer le véhicule sur sa route en fonction du temps écoulé.

            Args:
                delta_t (float): Durée pendant laquelle le véhicule avance (en minutes).
        """
        
        try:
            if self.vitesse < 0:
                raise NegativeSpeedError(self.identifiant, self.vitesse)
            if self.position < 0 or self.position > self.route.longueur:
                raise InvalidPositionError(self.identifiant, self.position, self.route.longueur)
            
            self.position += (self.vitesse / 60) * delta_t
            if self.position > self.route.longueur:
                self.position = self.route.longueur
        except (NegativeSpeedError, InvalidPositionError) as e:
            print(f"[Erreur Véhicule] {e}")

    def changer_de_route(self, nouvelle_route):
        """
            Permet au véhicule de changer de route.

            Args:
                nouvelle_route (Route): Nouvelle instance de la route sur laquelle le véhicule va circuler.
        """
        try:
            if nouvelle_route is None:
                raise RouteInexistanteError(self.identifiant)
            self.route = nouvelle_route
            self.position = 0.0
            print(f"🚗 Le véhicule {self.identifiant} a changé pour la route {nouvelle_route.nom}.")
        except RouteInexistanteError as e:
            print(f"[Erreur Véhicule] {e}")