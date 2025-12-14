import pytest
from analyse import detecter_anomalie

def test_detecter_anomalie():
    mesure_normale = {"capteur": "électricité", "consommation": 100}
    mesure_haute = {"capteur": "électricité", "consommation": 190}
    mesure_basse = {"capteur": "eau", "consommation": 20}

    assert detecter_anomalie(mesure_normale) == False
    assert detecter_anomalie(mesure_haute) == True
    assert detecter_anomalie(mesure_basse) == True
