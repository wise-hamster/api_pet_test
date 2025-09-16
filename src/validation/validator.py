from pydantic import ValidationError
import pytest


def validator(response,body, schema_validation):
    try:
        #Checking that the response is a dictionary and matches the schema
        response_json = response.json()
        if isinstance(response_json,dict) and schema_validation(**response_json) and isinstance(body, dict):
            
            for key,value in response_json.items():
                if key == 'id':
                    continue
                else:
                    assert value == body.get(key)
        return True

    except ValidationError:
            return False