from database import Database
from product_analyzer import ProductAnalyzer
from helper.writeAJson import writeAJson

db = Database(database = "mercado", collection = "compras")
db.resetDatabase()

product = ProductAnalyzer(db)

product.totalVendas 
product.produtoMais 
product.clienteRico 
product.produtoMais1 