import requests

from global_var import BASE


def test_binary_api():
    response = requests.post(BASE + "binaryfile/Binary file", {"content": "binary content", "parent": "parentDir"})
    print(response.json())

    response = requests.get(BASE + "binaryfile/Binary file")
    print(response.json())

    response = requests.put(BASE + "binaryfile/Binary file",
                            {"name": "New binary file", "content": "New binary content", "parent": "parentDir"})
    print(response.json())

    response = requests.delete(BASE + "binaryfile/New binary file")
    print(response.json())


def test_buffer_api():
    response = requests.post(BASE + "bufferfile/Buffer file", {"content": "buffer content", "parent": "parentDir"})
    print(response.json())

    response = requests.get(BASE + "bufferfile/Buffer file")
    print(response.json())

    response = requests.put(BASE + "bufferfile/Buffer file",
                            {"name": "New buffer file", "content": "New buffer content", "parent": "parentDir"})
    print(response.json())

    response = requests.delete(BASE + "bufferfile/New buffer file")
    print(response.json())


def test_log_api():
    response = requests.post(BASE + "logtextfile/Log file", {"content": "log content", "parent": "parentDir"})
    print(response.json())

    response = requests.get(BASE + "logtextfile/Log file")
    print(response.json())

    response = requests.put(BASE + "logtextfile/Log file",
                            {"name": "New log file", "content": "New log content", "parent": "parentDir"})
    print(response.json())

    response = requests.delete(BASE + "logtextfile/New log file")
    print(response.json())


def test_directory_api():
    response = requests.post(BASE + "directory/Dir", {"parent": "parentDir"})
    print(response.json())

    response = requests.get(BASE + "directory/Dir")
    print(response.json())

    response = requests.put(BASE + "directory/Dir", {"name": "New dir", "parent": "parentDir"})
    print(response.json())

    response = requests.delete(BASE + "directory/New dir")
    print(response.json())
