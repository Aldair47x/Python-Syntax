myDictionary = {
    "name": "Mowin"
    "city": "Pereira"
}

print(myDictionary.items())
print(myDictionary.clear())

print(myDictionary["name"])

myNewDictionary = dict(zip("abcd", [1,2,3,4]))

keys = myDictionary.keys()

values = myDictionary.values()

get = myDictionary.get("city")

