import requests
from resources.status_codes import *
from resources.params import *
from resources.routes import BASE_ROUTE

BASE = "http://127.0.0.1:5000/"


def post(json_data, file_type: str, file_name: str):
    if file_type == "directory":
        response = requests.post(BASE + file_type + "/" + file_name, {"parent": json_data["parent"]})
    else:
        response = requests.post(BASE + file_type + "/" + file_name, {"content": json_data["content"], "parent": json_data["parent"]})

    if response.status_code == STATUS_NOT_FOUND:
        raise Exception(ERROR_NOT_FOUND)

    if response.status_code < STATUS_SUCCESSFULL or response.status_code > 300:
        response_body = response.json()
        err = response_body[DATA_PARAM][ERROR_PARAM]
        raise Exception(f'error: {err}')

    print(response.json())


def delete(file_type: str, file_name: str):
    response = requests.delete(BASE + file_type + "/" + file_name)

    if response.status_code == STATUS_NOT_FOUND:
        raise Exception(ERROR_NOT_FOUND)

    if response.status_code < STATUS_SUCCESSFULL or response.status_code > 300:
        response_body = response.json()
        err = response_body[DATA_PARAM][ERROR_PARAM]
        raise Exception(f'error: {err}')
    print(response.json())


def put(json_data, file_type: str, file_name: str):
    response = requests.put(BASE + file_type + "/" + file_name, {"name": file_name, "content": json_data["content"], "parent": json_data["parent"]})

    if response.status_code == STATUS_NOT_FOUND:
        raise Exception(ERROR_NOT_FOUND)

    if response.status_code < STATUS_SUCCESSFULL or response.status_code > 300:
        response_body = response.json()
        err = response_body[DATA_PARAM][ERROR_PARAM]
        raise Exception(f'error: {err}')
    print(response.json())


def get(file_type, file_name):
    print(BASE + file_type + "/" + file_name)
    response = requests.get(BASE + file_type + "/" + file_name)

    if response.status_code == STATUS_NOT_FOUND:
        raise Exception(ERROR_NOT_FOUND)

    if response.status_code < STATUS_SUCCESSFULL or response.status_code > 300:
        response_body = response.json()
        err = response_body[DATA_PARAM][ERROR_PARAM]
        raise Exception(f'error: {err}')

    print(response.json())

