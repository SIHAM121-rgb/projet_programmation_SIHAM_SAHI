import random
from datetime import datetime


class Capteur:
    """Classe pour simuler un capteur IoT."""


    def __init__(self, id_capteur, nom):
        self.id = id_capteur
        self.nom = nom


    def mesurer(self):
        """Simule une mesure aléatoire du capteur."""
        valeur = random.randint(50, 200)
        return {
            "id": self.id,
            "capteur": self.nom,
            "consommation": valeur,
            "timestamp": datetime.now().isoformat()
        }
