from pokedex import Database
from WriteAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
db.resetDatabase()