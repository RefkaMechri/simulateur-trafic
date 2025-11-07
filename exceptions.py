"""
exceptions.py
--------------
Ce module définit l'ensemble des exceptions personnalisées utilisées dans le simulateur de trafic.
Elles héritent toutes de la classe de base SimulationError, permettant une gestion cohérente
des erreurs à travers le projet.

Chaque exception contient :
- un message explicite destiné au développeur et/ou à l'utilisateur
- une méthode __str__ pour une sortie propre et lisible
- une initialisation personnalisée permettant de capturer des détails contextuels
"""

class SimulationError(Exception):
    """Exception de base pour toutes les erreurs du simulateur."""
    
    def __init__(self, message: str, contexte: str = None):
        self.message = message
        self.contexte = contexte
        super().__init__(self.message)
    
    def __str__(self):
        base_msg = f"[SimulationError] {self.message}"
        if self.contexte:
            base_msg += f" | Contexte : {self.contexte}"
        return base_msg


class InvalidPositionError(SimulationError):
    """Erreur déclenchée lorsqu’un véhicule dépasse les limites d’une route."""
    
    def __init__(self, identifiant_vehicule: str, position: float, longueur_route: float):
        message = (f"Position invalide pour le véhicule '{identifiant_vehicule}'. "
                   f"Position actuelle : {position}, longueur maximale : {longueur_route}.")
        super().__init__(message, contexte="Véhicule.avancer()")


class NegativeSpeedError(SimulationError):
    """Erreur déclenchée lorsqu’une vitesse négative est détectée."""
    
    def __init__(self, identifiant_vehicule: str, vitesse: float):
        message = (f"Vitesse négative détectée pour le véhicule '{identifiant_vehicule}' "
                   f"({vitesse} km/h).")
        super().__init__(message, contexte="Véhicule.avancer()")


class VehicleAlreadyOnRouteError(SimulationError):
    """Erreur lorsqu’un véhicule est déjà présent sur la même route."""
    
    def __init__(self, identifiant_vehicule: str, nom_route: str):
        message = (f"Le véhicule '{identifiant_vehicule}' est déjà présent sur la route '{nom_route}'.")
        super().__init__(message, contexte="Route.ajouter_vehicule()")


class RouteInexistanteError(SimulationError):
    """Erreur lorsqu’un véhicule tente de rejoindre une route inexistante."""
    
    def __init__(self, nom_route: str):
        message = f"Tentative d'accès à une route inexistante : '{nom_route}'."
        super().__init__(message, contexte="ReseauRoutier.get_route()")


class ConfigFileError(SimulationError):
    """Erreur lors de la lecture ou du parsing du fichier de configuration."""
    
    def __init__(self, fichier: str, erreur_detail: str):
        message = f"Erreur de configuration dans le fichier '{fichier}': {erreur_detail}"
        super().__init__(message, contexte="Simulateur.charger_config()")


class StatisticalComputationError(SimulationError):
    """Erreur lors du calcul d’indicateurs statistiques."""
    
    def __init__(self, nom_route: str, cause: str):
        message = f"Erreur statistique sur la route '{nom_route}': {cause}."
        super().__init__(message, contexte="Analyseur.calculer_statistiques()")
