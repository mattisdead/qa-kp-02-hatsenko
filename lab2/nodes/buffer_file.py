from typing import List

from nodes.Node import Node
from nodes.directory import Directory


class BufferFile(Node):
    content = List[str]

    def __init__(self, name: str, parent: Directory, max_buf_file_size: int):
        if parent is None:
            raise Exception("No parent directory provided")
        self.name = name
        self.parent = parent
        self.parent.add_node(self)
        self.max_buf_file_size = max_buf_file_size
        self.content = []

    def delete(self):
        self.parent.delete_node(self)
        del self

    def move(self, new_parent: Directory):
        self.parent.delete_node(self)
        new_parent.add_node(self)
        self.parent = new_parent

    def push(self, item: str):
        if len(self.content) >= self.max_buf_file_size:
            raise OverflowError

        self.content.append(item)

    def consume(self, item: str) -> str:
        if len(self.content) == 0:
            raise Exception("File does not contain any items")

        if not self.content.__contains__(item):
            raise Exception("No such item found")

        index = self.content.index(item)
        return self.content.pop(index)
