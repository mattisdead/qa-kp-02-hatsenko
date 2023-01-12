from typing import List

from lab1.nodes.Node import Node


class Directory(Node):
    content: List[Node]

    def __init__(self, name: str, parent: "Directory", max_element_capacity: int):
        pass

    def add_node(self, node: Node):
        pass

    def delete(self):
        pass

    def get_content(self, level: int) -> str:
        pass

    def delete_node(self, node: Node):
        pass

    def move_node(self, node: Node, path: "Directory"):
        pass