from db import MongoDB
from analyse import detecter_anomalie
from capteur import Capteur


# Initialisation de MongoDB
db = MongoDB()


# Création de plusieurs capteurs
capteurs = [
    Capteur(1, "électricité"),
    Capteur(2, "gaz"),
    Capteur(3, "eau")
]


# Génération et insertion de mesures
for i in range(5):  # 5 mesures par capteur
    for c in capteurs:
        mesure = c.mesurer()
        print(mesure)

        # Détection d’anomalie
        if detecter_anomalie(mesure):
            print(f"⚠️ Anomalie détectée pour {mesure['capteur']} !")

        # Insertion dans MongoDB
        db.insert_mesure(mesure)


print("Toutes les mesures ont été envoyées sur MongoDB Atlas !")
