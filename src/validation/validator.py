from pydantic import ValidationError
import pytest


def validator_pet(response,body, schema_validation):
    try:
        #Checking that the response is a dictionary and matches the schema
        response_json = response.json()
        if isinstance(response_json,dict) and schema_validation(**response_json) and isinstance(body, dict):
            
            for key_response,value_response in response_json.items():
                value_body = body.get(key_response)
                if key_response == 'id':
                    continue
                elif isinstance(value_response,dict):
                    validator_dict(value_body,value_response)
                elif isinstance (value_response,list):
                    validator_list(value_body,value_response)                   
                else:
                    assert value_response == value_body, f'ERROR: {value_response} != {value_body}'
        return True

    except ValidationError:
            return False
    
def validator_dict(value_body, value_response):
    for key, value in value_response.items():
        if key not in value_body:
            assert value == 0
        else:
            assert value == value_body[key]


def validator_list(value_body, value_response):
    for index, item in enumerate(value_response):
        if isinstance(item,dict):
            validator_dict(value_body[index],item)
        else:
            assert value_body[index] == item
