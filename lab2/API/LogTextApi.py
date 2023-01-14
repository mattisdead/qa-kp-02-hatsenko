from flask import request
from flask_restful import Resource

from nodes.log_text_file import LogTextFile
from global_var import parent_directory


class LogTextApi(Resource):

    def get(self, name: str):
        log_text_file = parent_directory.find_node_in_content(name)
        return {log_text_file.name: log_text_file.get_content()}

    def post(self, name: str):
        if request.form["parent"] == parent_directory.name:
            curr_parent_dir = parent_directory
        else:
            curr_parent_dir = parent_directory.find_directory_in_content(request.form["parent"])
        log_text_file = LogTextFile(name, curr_parent_dir, request.form["content"])
        return {"Log file has been added to ": request.form["parent"]}

    def put(self, name: str):
        log_text_file = parent_directory.find_node_in_content(name)
        if log_text_file is None:
            self.post(name)
            return
        if log_text_file.name != request.form["name"]:
            log_text_file.name = request.form["name"]
        if log_text_file.content != request.form["content"]:
            log_text_file.content = request.form["content"]
        if log_text_file.parent.name != request.form["parent"]:
            directory_to_move_to = parent_directory.find_directory_in_content(request.form["parent"])
            if directory_to_move_to is not None:
                log_text_file.move(directory_to_move_to)
            else:
                return {"Error": "No directory found with the name: " + request.form["parent"]}

        return {"Updated": log_text_file.name}

    def delete(self, name: str):
        log_text_file = parent_directory.find_node_in_content(name)
        if log_text_file is not None:
            log_text_file.delete()
        else:
            return {"Error": "No log file with such name found"}
        return {"Deleted": name}
