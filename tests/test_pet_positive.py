from src.request.url import PetGroup
from src.validation.schemas_respones import FullPetObject
from src.validation.validator import validator_pet
from src.request.bodies import *
import pytest
from requests import Response 
from src.request.http_methods import HttpMethods


class Test_Pet():
    @pytest.mark.parametrize("pet_data", [pet_dog,pet_dog_without_status,pet_dog_without_name_in_tags,
                                      pet_dog_without_id_in_tags,pet_dog_without_tags,pet_dog_without_photoUrls,
                                      pet_dog_without_name_in_category,pet_dog_without_id_in_category,pet_dog_without_category])
    def test_post_pet_full_1(self,pet_data,pet_ids_dict):
        result_response: Response = HttpMethods.post(url=PetGroup().post_pet(),body= pet_data)
        print('Send POST-request')

        #Check status code from request
        assert result_response.status_code == 200, f'ERROR: Status code != 200; Status code == {result_response.status_code}'
        print(f'Status code - {result_response.status_code}')

        #Validation response and body for request
        is_valid = validator_pet(response=result_response, body=pet_data, schema_validation=FullPetObject)
        assert is_valid, "Response validation failed"
        print(f'Validation correct')

        #Add pet_id in list
        pet_id = result_response.json().get('id')
        pet_ids_dict[pet_id] = result_response.json()