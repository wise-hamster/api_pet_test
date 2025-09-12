from src.request.API_URL import API


class MethodPet():
    def __init__(self,url,pet_id):
        self.url_pet = f'{API.URL.value}/pet'
        self.pet = f'{API.URL.value}/pet/{pet_id}'
    

    #uploads an image
    def url_post_upload_image(self):
        return f'{self.pet}/uploadImage'


    #Add a new pet to the store
    def url_post_pet (self):
        return self.url_pet
    

    #Update an existing pet
    def url_put_pet (self):
        return self.url_pet
    

    #Finds Pets by status
    def url_get_findByStatus(self):
        return f'{self.url_pet}/findByStatus'
    

    #Find pet by ID
    def url_get_pet_id(self):
        return self.pet
    

    #Updates a pet in the store with form data
    def url_post_pet_id(self):
        return self.pet


    #Deletes a pet
    def url_delete_pet_id(self):
        return self.pet
