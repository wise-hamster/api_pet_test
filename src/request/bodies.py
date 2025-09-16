from .constructor_body import PetObject
import random

animal_names = ("Buddy","Luna", "Max","Bella","Charlie","Lucy",
    "Cooper","Daisy","Milo","Zoe")

pet_dog = PetObject(
    category = {"id": random.randint(1,10000),
                "name": "dog"},
    name= random.choice(animal_names),
    photoUrls=['https://i.pinimg.com/originals/42/d5/76/42d576804ac5a5a41b76c6b56c4a0fb3.jpg'],
    tags=[{'id': random.randint(1,10000),
           'name': 'Junior'} ],
    status= 'vaccination').to_dict()
