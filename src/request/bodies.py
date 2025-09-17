from .constructor_body import PetObject
import random

animal_names = ("Buddy","Luna", "Max","Bella","Charlie","Lucy",
    "Cooper","Daisy","Milo","Zoe")


def create_pet_dog(**kwargs):
    defaults = {
        'category': {'id': random.randint(1, 10000), 
                     'name': 'dog'},
        'name': random.choice(animal_names),
        'photoUrls': ['https://i.pinimg.com/originals/42/d5/76/42d576804ac5a5a41b76c6b56c4a0fb3.jpg'],
        'tags': [{'id': random.randint(1, 10000), 
                  'name': 'Junior'}],
        'status': 'vaccination'
    }
    defaults.update(kwargs)
    return PetObject(**defaults).to_dict()

pet_dog = create_pet_dog()
pet_dog_without_status = create_pet_dog(status = None)
pet_dog_without_name_in_tags = create_pet_dog(tags = [{'id': random.randint(1,10000)}])
pet_dog_without_id_in_tags = create_pet_dog(tags = [{'name': 'Junior'}])
pet_dog_without_tags = create_pet_dog(tags = [])
pet_dog_without_photoUrls = create_pet_dog(photoUrls= [])
pet_dog_without_name = create_pet_dog(name= None)
pet_dog_without_name_in_category = create_pet_dog(category = {'id': random.randint(1, 10000)})
pet_dog_without_id_in_category = create_pet_dog(category = {'name':'Junior'})
pet_dog_without_category = create_pet_dog(category = None)
