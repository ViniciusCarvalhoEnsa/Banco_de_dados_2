from typing import Collection
import pymongo
from dataset import pokemon_dataset
from main import db
from WriteAJson import writeAJson


class Database:
    def __init__(self, database, collection):
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connectionString = "localhost:27017"
            self.clusterConnection = pymongo.MongoClient(connectionString, tlsAllowInvalidCertificates = True)
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
            print("Conectado ao banco de dados com sucesso!")
        except Exception as e:
            print(e)

    def resetDatabase(self):
        try: 
            self.db.drop_collection(self.collection)
            self.collection.insert_many(pokemon_dataset)
            print("Banco de dados resetado com sucesso!")
        except Exception as e:
            print(e)

#------------------------------------------------------------------------------------------primeiro comando
def getPokemonByName(name: str):
    return db.collection.find({"name": name})

pikachu = getPokemonByName("Charmander")
writeAJson(pikachu, "charmander")

#------------------------------------------------------------------------------------------segundo comando
tipos = ["Psychic"]
pokemons = db.collection.find({ "type": {"$in": tipos}, "next_evolution": {"$exists": True} })

#------------------------------------------------------------------------------------------terceiro comando
pokemons = db.collection.find({"weaknesses": {"$size": 3}})

#------------------------------------------------------------------------------------------quarto comando
pokemons = db.collection.find({"num:" "150"})

#------------------------------------------------------------------------------------------quinto comando
pokemons = db.collection.find()
