from pymongo import MongoClient


class MongoDB:
    """Classe pour gérer la connexion et insertion sur MongoDB Atlas."""


    def __init__(self):
        self.uri = (
            "mongodb+srv://sihamsahi_db_user:9nvozxVsVDhlJrUa@cluster0.qxr22jk.mongodb.net/"
            "?appName=Cluster0"
        )
        self.client = MongoClient(self.uri)
        self.db = self.client["consommation_energetique"]


    def insert_mesure(self, mesure):
        """Insère une mesure dans la collection 'mesures'."""
        collection = self.db["mesures"]
        result = collection.insert_one(mesure)
        print(f"Mesure insérée avec l'ID : {result.inserted_id}")
