import pytest


@pytest.fixture(scope='session')
def pet_ids_list():
    return []


@pytest.fixture(scope='session')
def pet_ids_dict():
    return {}


@pytest.fixture(scope='session')
def pet_id(pet_ids_list):
    return pet_ids_list[0]
