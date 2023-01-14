from nodes.Node import Node
from nodes.directory import Directory


class LogTextFile(Node):
    def __init__(self, name: str, parent: Directory, content: str):
        if parent is None:
            raise Exception("No parent direction provided")
        self.name = name
        self.parent = parent
        self.parent.add_node(self)
        self.content = content

    def delete(self):
        self.parent.delete_node(self)
        del self

    def move(self, new_parent):
        self.parent.delete_node(self)
        new_parent.add_node(self)
        self.parent = new_parent

    def get_content(self) -> str:
        return self.content

    def append(self, line: str):
        self.content += "\n" + line
