from typing import List

from lab1.nodes.Node import Node
from lab1.nodes.directory import Directory


class BufferFile(Node):
    content = List[str]

    def __init__(self, name: str, parent: Directory, max_buf_file_size: int):
        pass

    def delete(self):
        pass

    def move(self, new_parent: Directory):
        pass

    def push(self, item: str):
        pass

    def consume(self, item: str) -> str:
        pass
