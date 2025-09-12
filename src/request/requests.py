import requests


def post_request(url,body):
    return requests.post(url=url,json=body)


def get_request(url):
    return requests.get(url=url)


def put_request(url,body):
    return requests.post(url=url,json=body)


def delete_request(url):
    return requests.post(url=url)