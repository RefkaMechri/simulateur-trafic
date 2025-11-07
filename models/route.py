from exceptions import VehicleAlreadyOnRouteError


class Route :
    """ 
        ------------
        Représente une route dans le simulateur de trafic.
        Attributs :
            nom (str) : Nom de la route.
            longueur (float) : Longueur de la route en kilomètres.
            limite_vitesse (float) : Limite de vitesse sur la route en km/h.
            vehicules (list) : Liste des véhicules présents sur la route.
        Méthodes disponibles :
            - ajouter_vehicule(vehicule) : Ajoute un véhicule à la route.
            - mettre_a_jour_vehicules(delta_t) : Met à jour la position de chaque véhicule sur la route en fonction du temps écoulé (delta_t en minutes).
    """
    def __init__(self, nom, longueur, limite_vitesse):
        """
            Initialise une instance de la classe Route.

            Args:
                nom (str): Nom de la route.
                longueur (float): Longueur de la route en kilomètres.
                limite_vitesse (float): Limite de vitesse sur la route en km/h.
        """
        self.nom = nom
        self.longueur = longueur
        self.limite_vitesse = limite_vitesse
        self.vehicules = []
        
    def ajouter_vehicule(self,vehicule):
        """
            Ajoute un véhicule à la route.

            Args:
                vehicule (Vehicule): Instance du véhicule à ajouter à la route.
        """
        
        try:
            if vehicule in self.vehicules:
                raise VehicleAlreadyOnRouteError(vehicule.identifiant,self.nom)
            self.vehicules.append(vehicule)
        except (VehicleAlreadyOnRouteError) as e:
            print(f"[Erreur Route] {e}")
        
    def mettre_a_jour_vehicules(self,delta_t):
        """
            Met à jour la position de chaque véhicule sur la route en fonction du temps écoulé.

            Args:
                delta_t (float): Temps écoulé en minutes depuis la dernière mise à jour.
        """
        for v in self.vehicules :
            v.avancer(delta_t)
    
            
