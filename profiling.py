import cProfile
import pstats
from core.simulateur import Simulateur
from models.reseau import ReseauRoutier

if __name__ == "__main__":
    reseau = ReseauRoutier.charger_depuis_fichier("data/reseau_config.json")
    simu = Simulateur(reseau)
    with cProfile.Profile() as profile:
        simu.lancer_simulation(n_tours=60, delta_t=1)

    stats = pstats.Stats(profile)
    stats.sort_stats(pstats.SortKey.TIME)  # Trie par temps d’exécution
    stats.print_stats(20)  # Affiche les 20 fonctions les plus lentes
