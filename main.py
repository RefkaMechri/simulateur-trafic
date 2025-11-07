from core.simulateur import Simulateur

if __name__ == "__main__":
    simu = Simulateur(fichier_config="data/config_reseau.json")
    simu.lancer_simulation(n_tours=60, delta_t=1)  # 60 minutes, pas de 1 min
