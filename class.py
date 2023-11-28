import requests
import json
class Cats:

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    
    def getCat(self, n):
        breeds = requests.get("https://catfact.ninja/breeds")
        jsonBreeds = json.loads(breeds.text)
        return jsonBreeds["data"][n]["breed"]
    


cat = Cats("Jayden", "Russell", 18)
print("Your breed is " + cat.getCat(10))


        
    