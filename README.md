# Simulateur de Trafic Routier 🚗

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Simulateur de trafic routier avec analyse statistique, visualisation graphique et gestion d'exceptions avancée.

## 📦 Installation

### Depuis TestPyPI

```bash
pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ simulateur-trafic-refka
```

### Depuis les sources

```bash
git clone https://github.com/RefkaMechri/simulateur-trafic.git
cd simulateur-trafic
pip install -e .
```

## 🚀 Utilisation

### Exemple Simple

```python
from models.vehicule import Vehicule
from models.route import Route
from models.reseau import ReseauRoutier

# Créer une route
route = Route("Autoroute A1", longueur=10.0, limite_vitesse=130)

# Créer un véhicule
vehicule = Vehicule("V001", route, position=0.0, vitesse=120)

# Ajouter le véhicule sur la route
route.ajouter_vehicule(vehicule)

# Créer un réseau
reseau = ReseauRoutier()
reseau.ajouter_route(route)

# Simuler 1 minute
reseau.simuler(delta_t=1.0)
print(f"Position: {vehicule.position} km")
```

### Simulation Complète avec Fichier JSON

```python
from core.simulateur import Simulateur

# Créer le simulateur avec configuration JSON
simu = Simulateur(fichier_config="data/config_reseau.json")

# Lancer la simulation (60 minutes, pas de 1 min)
simu.lancer_simulation(n_tours=60, delta_t=1)
```

### Format du Fichier de Configuration

```json
{
  "routes": [
    {"nom": "Route 1", "longueur": 10.0, "limite_vitesse": 90},
    {"nom": "Route 2", "longueur": 15.0, "limite_vitesse": 110}
  ],
  "vehicules": [
    {"id": "V1", "route": 0, "position": 0.0, "vitesse": 80},
    {"id": "V2", "route": 1, "position": 5.0, "vitesse": 100}
  ]
}
```

## 📚 Modules Disponibles

### `models.vehicule.Vehicule`
Représente un véhicule circulant sur une route.

```python
vehicule = Vehicule(identifiant="V1", route=ma_route, position=0.0, vitesse=120)
vehicule.avancer(delta_t=1.0)  # Avance pendant 1 minute
vehicule.changer_de_route(nouvelle_route)
```

### `models.route.Route`
Représente une route avec ses caractéristiques.

```python
route = Route(nom="A1", longueur=50.0, limite_vitesse=130)
route.ajouter_vehicule(vehicule)
route.mettre_a_jour_vehicules(delta_t=1.0)
```

### `models.reseau.ReseauRoutier`
Gère un réseau de routes.

```python
reseau = ReseauRoutier()
reseau.ajouter_route(route1)
reseau.ajouter_route(route2)
reseau.simuler(delta_t=1.0)
```

### `core.simulateur.Simulateur`
Orchestre la simulation complète.

```python
simu = Simulateur(fichier_config="config.json")
simu.lancer_simulation(n_tours=60, delta_t=1)
```

### `core.analyseur.Analyseur`
Calcule les statistiques de trafic.

```python
from core.analyseur import Analyseur

analyseur = Analyseur(reseau)
stats = analyseur.calculer_statistiques()
# Retourne: vitesse_moyenne, densite, temps_parcours_moyen, zone_congestion, etc.
```

## 🎨 Visualisation

Le package génère automatiquement des graphiques :
- **Vitesses** : moyennes, minimales et maximales par route
- **Densité** : nombre de véhicules par km avec détection de congestion

## 💾 Export des Résultats

Les statistiques sont sauvegardées dans `resultats.json` :

```json
{
  "date": "2025-11-07 14:30:00",
  "statistiques": {
    "Route 1": {
      "vitesse_moyenne": 85.5,
      "densite": 0.8,
      "zone_congestion": false
    }
  }
}
```

## ⚠️ Gestion des Exceptions

Exceptions personnalisées disponibles :

```python
from exceptions import (
    InvalidPositionError,
    NegativeSpeedError,
    VehicleAlreadyOnRouteError,
    ConfigFileError
)

try:
    vehicule.avancer(delta_t=1.0)
except InvalidPositionError as e:
    print(f"Erreur: {e}")
```

## 🧪 Tests

```bash
# Installer les dépendances de développement
pip install -e ".[dev]"

# Lancer les tests
pytest

# Avec couverture
pytest --cov=. --cov-report=html
```

## 📖 Documentation

Documentation générée avec Sphinx disponible dans le dossier `docs/`.

```bash
cd docs
make html
```

## 👤 Auteur

**Refka Mechri**

- Email: ref.kaa2002@gmail.com

## 📝 Licence

MIT License - voir [LICENSE](LICENSE)

## 🎓 Contexte

Projet développé dans le cadre d'un travail pratique académique sur la simulation de systèmes de trafic routier.
