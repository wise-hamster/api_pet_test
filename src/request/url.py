from enum import Enum

class API(Enum):
    URL = 'https://petstore.swagger.io/v2'

class MethodPet:
    BASE_URL = f'{API.URL.value}/pet'
    
    @classmethod
    def post_pet(cls):
        """Add a new pet to the store"""
        return cls.BASE_URL
    
    @classmethod
    def put_pet(cls):
        """Update an existing pet"""
        return cls.BASE_URL
    
    @classmethod
    def get_find_by_status(cls):
        """Finds Pets by status"""
        return f'{cls.BASE_URL}/findByStatus'
    
    @classmethod
    def get_pet_by_id(cls, pet_id):
        """Find pet by ID"""
        return f'{cls.BASE_URL}/{pet_id}'
    
    @classmethod
    def post_upload_image(cls, pet_id):
        """Uploads an image"""
        return f'{cls.BASE_URL}/{pet_id}/uploadImage'
    
    @classmethod
    def post_pet_by_id(cls, pet_id):
        """Updates a pet with form data"""
        return f'{cls.BASE_URL}/{pet_id}'
    
    @classmethod
    def delete_pet(cls, pet_id):
        """Deletes a pet"""
        return f'{cls.BASE_URL}/{pet_id}'