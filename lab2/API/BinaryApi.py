from flask import request
from flask_restful import Resource

from global_var import parent_directory
from nodes.binary_file import BinaryFile


class BinaryApi(Resource):

    def get(self, name: str):
        binary_file = parent_directory.find_node_in_content(name)
        return {binary_file.name: binary_file.get_content()}

    def post(self, name: str):
        if request.form["parent"] == parent_directory.name:
            curr_parent_dir = parent_directory
        else:
            curr_parent_dir = parent_directory.find_directory_in_content(request.form["parent"])
        curr_binary_file = BinaryFile(name, request.form["content"], curr_parent_dir)
        return {"Binary file has been added to ": request.form["parent"]}

    def put(self, name: str):
        binary_file = parent_directory.find_node_in_content(name)
        if binary_file is None:
            self.post(name)
            return
        if binary_file.name != request.form["name"]:
            binary_file.name = request.form["name"]
        if binary_file.content != request.form["content"]:
            binary_file.content = request.form["content"]
        if binary_file.parent.name != request.form["parent"]:
            directory_to_move_to = parent_directory.find_directory_in_content(request.form["parent"])
            if directory_to_move_to is not None:
                binary_file.move(directory_to_move_to)
            else:
                return {"Error": "No directory found with the name: " + request.form["parent"]}

        return {"Updated": binary_file.name}

    def delete(self, name: str):
        binary_file = parent_directory.find_node_in_content(name)
        if binary_file is not None:
            binary_file.delete()
        else:
            return {"Error": "No binary file with such name found"}
        return {"Deleted": name}
