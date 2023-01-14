import click
import internal.app_connector as app_connector
from resources.routes import *
from resources.params import *


# Main route
@click.group()
def process_command():
    pass


@process_command.group()
def create():
    pass


# Create subgroup
@click.argument('parent')
@click.argument('NODE_NAME')
@create.command()
def directory(node_name, parent):
    json_data = {"parent": parent}

    try:
        app_connector.post(json_data, DIR_ROUTE, node_name)
    except Exception as e:
        print(e)
        return

    print(SUCCESS_OPERATION)


@click.argument('PARENT')
@click.argument('CONTENT')
@click.argument('NODE_NAME')
@create.command()
def binary_file(node_name, content, parent):
    json_data = {
        "content": content,
        "parent": parent
    }

    try:
        app_connector.post(json_data, BIN_FILE_ROUTE, node_name)
    except Exception as e:
        print(e)
        return

    print(SUCCESS_OPERATION)


@click.argument('PARENT')
@click.argument('CONTENT')
@click.argument('NODE_NAME')
@create.command()
def log_file(node_name, content, parent):
    json_data = {
        "content": content,
        "parent": parent
    }

    try:
        app_connector.post(json_data, LOG_FILE_ROUTE, node_name)
    except Exception as e:
        print(e)
        return

    print(SUCCESS_OPERATION)


@click.argument('PARENT')
@click.argument('CONTENT')
@click.argument('NODE_NAME')
@create.command()
def buffer_file(node_name, content, parent):
    json_data = {
        "content": content,
        "parent": parent
    }

    try:
        app_connector.post(json_data, BUF_FILE_ROUTE, node_name)
    except Exception as e:
        print(e)
        return

    print(SUCCESS_OPERATION)


# Other methods
@click.argument('NAME_NODE')
@click.argument('FILE_TYPE')
@process_command.command()
def delete(name_node, file_type):
    try:
        app_connector.delete(file_type, name_node)
    except Exception as e:
        print(e)
        return

    print(SUCCESS_OPERATION)


@click.argument('FILE_TYPE')
@click.argument('NAME_NODE')
@process_command.command()
def read(name_node, file_type):
    try:
        app_connector.get(file_type, name_node)
    except Exception as e:
        print(e)
        return


@click.argument('CONTENT')
@click.argument('PARENT')
@click.argument('NAME_NODE')
@click.argument('FILE_TYPE')
@process_command.command()
def write(file_type, name_node, parent, content):
    if file_type == "directory":
        print("Content of a directory should be changed by modifying files.")
        return

    json_data = {
        "parent": parent,
        "content": content,
    }

    try:
        app_connector.put(json_data, file_type, name_node)
    except Exception as e:
        print(e)
        return

    print(SUCCESS_OPERATION)


def process():
    process_command()
