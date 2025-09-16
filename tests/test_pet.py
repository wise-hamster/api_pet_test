from src.request.url import MethodPet
from src.validation.schemas_respones import FullPetObject
from src.validation.validator import validator
from src.request.bodies import *
import requests

def test_post_pet(pet_ids_list, pet_ids_dict):
    response = requests.post(url=MethodPet().post_pet(),json=pet_dog)
    assert response.status_code == 200
    #
    is_valid = validator(response=response, body=pet_dog, schema_validation=FullPetObject)
    assert is_valid, "Response validation failed"

    pet_id = response.json().get('id')
    pet_ids_list.append(pet_id)
    pet_ids_dict[pet_id] = pet_dog