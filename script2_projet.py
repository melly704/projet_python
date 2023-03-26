import script1_projet
from pymongo import MongoClient


client = MongoClient()
db = client['Rakuten']
promos = db['Promos']
results = promos.find().limit(100)


for i in range(0, len(script1_projet.titles)):
    article = script1_projet.create_article(i)
    promos.insert_one(article)

