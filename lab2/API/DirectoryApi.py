from flask import request
from flask_restful import Resource


from global_var import parent_directory
from nodes.directory import Directory


class DirectoryApi(Resource):
    def get(self, name: str):
        if parent_directory.name == name:
            return {parent_directory.name: parent_directory.get_content(1)}

        directory = parent_directory.find_directory_in_content(name)
        return {directory.name: directory.get_content(1)}

    def post(self, name: str):
        if request.form["parent"] == parent_directory.name:
            curr_parent_dir = parent_directory
        else:
            curr_parent_dir = parent_directory.find_directory_in_content(request.form["parent"])
        directory = Directory(name, curr_parent_dir, 10)
        return {"New directory has been added to ": request.form["parent"]}

    def put(self, name: str):
        directory = parent_directory.find_directory_in_content(name)
        if directory is None:
            self.post(name)
            return
        if directory.name != request.form["name"]:
            directory.name = request.form["name"]
        if directory.parent.name != request.form["parent"]:
            directory_to_move_to = parent_directory.find_directory_in_content(request.form["parent"])
            if directory_to_move_to is not None:
                directory.move(directory_to_move_to)
            else:
                return {"Error" : "No directory found with the name: " + request.form["parent"]}

        return {"Updated": directory.name}

    def delete(self, name: str):
        directory = parent_directory.find_node_in_content(name)
        if directory is not None:
            directory.delete()
        else:
            return {"Error": "No directory with such name found"}
        return {"Deleted": name}