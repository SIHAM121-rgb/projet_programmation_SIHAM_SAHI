import pytest
from capteur import Capteur

def test_mesurer_valeurs():
    capteur = Capteur(1, "électricité")
    mesure = capteur.mesurer()

    assert "id" in mesure
    assert "capteur" in mesure
    assert "consommation" in mesure
    assert "timestamp" in mesure

    # Consommation dans la plage simulée
    assert 50 <= mesure["consommation"] <= 200
