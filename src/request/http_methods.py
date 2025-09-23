import requests

class HttpMethods:

    @staticmethod 
    def get(url):
        result = requests.get(
            url=url)
        return result

    @staticmethod
    def post(url, body):
        result = requests.post(
            url=url,
            json=body)
        return result


    @staticmethod
    def put(url, body):
        result = requests.put(
            url=url,
            json=body)
        return result
    

    @staticmethod
    def delete(url, body):
        result = requests.delete(
            url=url,
            json=body)
        return result