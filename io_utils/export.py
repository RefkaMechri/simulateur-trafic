import json
import os
from datetime import datetime

class Export:
    def __init__(self, nom_fichier="resultats.json"):
        self.nom_fichier = nom_fichier
        self.data = self._charger_donnees_existantes()

    def _charger_donnees_existantes(self):
        """Charge les anciennes données si le fichier existe déjà"""
        if os.path.exists(self.nom_fichier):
            with open(self.nom_fichier, "r") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        return []

    def sauvegarder(self, stats):
        """Sauvegarde les nouvelles statistiques dans le fichier JSON"""
        entree = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "statistiques": stats
        }
        self.data.append(entree)
        with open(self.nom_fichier, "w") as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)
        print(f"💾 Statistiques sauvegardées dans '{self.nom_fichier}'")
