import matplotlib.pyplot as plt

class Affichage:
    """
        Classe Affichage pour la visualisation des statistiques de trafic routier.
        Fournit des méthodes pour afficher les statistiques textuellement et graphiquement.
    """
    def afficher(self, stats_par_route):
        """
            Affiche les statistiques de trafic pour chaque route.

            Args:
                stats_par_route (dict): Dictionnaire contenant les statistiques par route.
        """
        print("📊 Statistiques par route :")
        for route, stats in stats_par_route.items():
            print(f"{route}:")
            for k, v in stats.items():
                if isinstance(v, float):
                    print(f"  - {k}: {v:.2f}")
                else:
                    print(f"  - {k}: {v}")

        self.afficher_graphiques(stats_par_route)

    def afficher_graphiques(self, stats_par_route):
        """
            Affiche graphiquement les statistiques de trafic pour chaque route.

            Args:
                stats_par_route (dict): Dictionnaire contenant les statistiques par route.
        """
        routes = list(stats_par_route.keys())

        # --- Graphique 1 : vitesse moyenne par route ---
        vitesses_moy = [stats["vitesse_moyenne"] for stats in stats_par_route.values()]
        vitesses_min = [stats["vitesse_minimale"] for stats in stats_par_route.values()]
        vitesses_max = [stats["vitesse_maximale"] for stats in stats_par_route.values()]

        x = range(len(routes))
        plt.figure(figsize=(10, 5))
        plt.bar(x, vitesses_moy, width=0.3, label="Moyenne", color='green')
        plt.bar([i + 0.3 for i in x], vitesses_min, width=0.3, label="Min", color='red')
        plt.bar([i + 0.6 for i in x], vitesses_max, width=0.3, label="Max", color='blue')
        plt.xticks([i + 0.3 for i in x], routes)
        plt.ylabel("Vitesse (km/h)")
        plt.title("Vitesses des véhicules par route")
        plt.legend()
        plt.grid(axis="y", linestyle="--", alpha=0.6)
        plt.show()

        # --- Graphique 2 : densité par route ---
        densites = [stats["densite"] for stats in stats_par_route.values()]
        couleurs = ['red' if stats["zone_congestion"] else 'orange' for stats in stats_par_route.values()]

        plt.figure(figsize=(10, 5))
        plt.barh(routes, densites, color=couleurs)
        plt.xlabel("Véhicules / unité de longueur")
        plt.title("Densité de véhicules par route (rouge = congestion)")
        plt.grid(axis="x", linestyle="--", alpha=0.6)
        plt.show()
