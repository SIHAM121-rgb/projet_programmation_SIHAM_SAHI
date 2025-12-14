def detecter_anomalie(mesure):
    """
    Vérifie si une mesure dépasse les seuils normaux.
    Retourne True si anomalie détectée, False sinon.
    """
    capteur = mesure["capteur"]
    valeur = mesure["consommation"]

    seuils = {
        "électricité": (50, 180),
        "gaz": (50, 150),
        "eau": (30, 120)
    }

    if capteur in seuils:
        min_val, max_val = seuils[capteur]
        if valeur < min_val or valeur > max_val:
            return True

    return False
