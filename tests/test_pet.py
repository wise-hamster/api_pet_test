from src.request.url import MethodPet
from src.validation.schemas_respones import FullPetObject
from src.validation.validator import validator_pet
from src.request.bodies import *
import pytest
import requests


@pytest.mark.parametrize("pet_data", [pet_dog,pet_dog_without_status,pet_dog_without_name_in_tags,
                                      pet_dog_without_id_in_tags,pet_dog_without_tags,pet_dog_without_photoUrls,
                                      pet_dog_without_name_in_category,pet_dog_without_id_in_category,pet_dog_without_category])
def test_post_pet_full(pet_data,pet_ids_dict):
    response = requests.post(url=MethodPet().post_pet(),json=pet_data)
    assert response.status_code == 200, f'ERROR: Status code != 200; Status code == {response.status_code}'
    #Validation response and body for request
    is_valid = validator_pet(response=response, body=pet_data, schema_validation=FullPetObject)
    assert is_valid, "Response validation failed"

    pet_id = response.json().get('id')
    pet_ids_dict[pet_id] = response.json()