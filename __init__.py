"""
Simulateur de Trafic Routier

Un package Python pour simuler et analyser le trafic routier avec gestion
d'exceptions avancées et visualisation des statistiques.

Auteur: Refka Mechri
"""

__version__ = "1.0.0"
__author__ = "Refka Mechri"

# Imports pour faciliter l'utilisation
from exceptions import (
    SimulationError,
    InvalidPositionError,
    NegativeSpeedError,
    VehicleAlreadyOnRouteError,
    RouteInexistanteError,
    ConfigFileError,
    StatisticalComputationError
)

from models.vehicule import Vehicule
from models.route import Route
from models.reseau import ReseauRoutier

from core.simulateur import Simulateur
from core.analyseur import Analyseur

from io_utils.affichage import Affichage
from io_utils.export import Export

__all__ = [
    # Exceptions
    "SimulationError",
    "InvalidPositionError",
    "NegativeSpeedError",
    "VehicleAlreadyOnRouteError",
    "RouteInexistanteError",
    "ConfigFileError",
    "StatisticalComputationError",
    # Modèles
    "Vehicule",
    "Route",
    "ReseauRoutier",
    # Core
    "Simulateur",
    "Analyseur",
    # IO Utils
    "Affichage",
    "Export",
]