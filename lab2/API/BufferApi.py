from flask import request
from flask_restful import Resource

from global_var import parent_directory
from nodes.buffer_file import BufferFile


class BufferApi(Resource):

    def get(self, name: str):
        buffer_file = parent_directory.find_node_in_content(name)
        return {buffer_file.name: buffer_file.get_content()}

    def post(self, name: str):
        if request.form["parent"] == parent_directory.name:
            curr_parent_dir = parent_directory
        else:
            curr_parent_dir = parent_directory.find_directory_in_content(request.form["parent"])
        curr_buffer_file = BufferFile(name, request.form["content"], curr_parent_dir)
        return {"Buffer file has been added to ": request.form["parent"]}

    def put(self, name: str):
        buffer_file = parent_directory.find_node_in_content(name)
        if buffer_file is None:
            self.post(name)
            return
        if buffer_file.name != request.form["name"]:
            buffer_file.name = request.form["name"]
        if buffer_file.content != request.form["content"]:
            buffer_file.content = request.form["content"]
        if buffer_file.parent.name != request.form["parent"]:
            directory_to_move_to = parent_directory.find_directory_in_content(request.form["parent"])
            if directory_to_move_to is not None:
                buffer_file.move(directory_to_move_to)
            else:
                return {"Error": "No directory found with the name: " + request.form["parent"]}

        return {"Updated": buffer_file.name}

    def delete(self, name: str):
        buffer_file = parent_directory.find_node_in_content(name)
        if buffer_file is not None:
            buffer_file.delete()
        else:
            return {"Error": "No buffer file with such name found"}
        return {"Deleted": name}
