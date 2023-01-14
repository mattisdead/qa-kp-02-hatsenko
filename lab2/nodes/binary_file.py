from nodes.Node import Node
from nodes.directory import Directory


class BinaryFile(Node):
    def __init__(self, name: str, content: str, parent: Directory):
        if parent is None:
            raise Exception("No parent directory provided")
        self.name = name
        self.content = content
        self.parent = parent
        parent.add_node(self)

    def delete(self):
        self.parent.delete_node(self)
        del self

    def move(self, new_parent: Directory):
        self.parent.delete_node(self)
        new_parent.add_node(self)
        self.parent = new_parent

    def get_content(self) -> str:
        return self.content
