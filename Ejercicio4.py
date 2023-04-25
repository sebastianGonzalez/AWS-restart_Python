"""misFrutas = ["Manzana", "Banana", "Cereza"]
print(misFrutas)
print(type(misFrutas))
print(misFrutas[0])
print(misFrutas[1])
print(misFrutas[2])

misFrutas[2] = "Naranja"
print(misFrutas)"""

"""myFinalAnswerTuple = ("Manzana", "Banana", "Piña")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])"""

myFavoriteFruitDictionary = {
  "Akua" : ["Manzana", "Banana", "Cereza"],
  "Saanvi" : ["Mandarina", "Bocadillo", "Coco"],
  "Paulo" : ["Mango", "Borojo", "lulo"]
}

print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

print(myFavoriteFruitDictionary["Akua"][0])
print(myFavoriteFruitDictionary["Saanvi"][1])
print(myFavoriteFruitDictionary["Paulo"][2])

import pandas
mydb = pandas.DataFrame(myFavoriteFruitDictionary)
print(mydb)