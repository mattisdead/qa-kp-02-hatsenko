from typing import List

from lab1.nodes.Node import Node


class Directory(Node):
    content: List[Node]

    def __init__(self, name: str, parent: "Directory", max_element_capacity: int):
        self.name = name
        self.parent = parent
        self.max_element_capacity = max_element_capacity
        self.content = []
        if parent is not None:
            parent.add_node(self)

    def add_node(self, node: Node):
        if len(self.content) >= self.max_element_capacity:
            raise OverflowError

        if self.content.__contains__(node):
            raise Exception('Object with such name already exists')

        node.parent = self

        self.content.append(node)

    def delete(self):
        for item in self.content:
            del item
        del self

    def get_content(self, level: int) -> str:
        result = self.__str__() + "\n"

        if len(self.content) != 0:
            for item in self.content:
                if type(item) is Directory:
                    result += level * "-" + item.get_content(level + 1)
                else:
                    result += level * "-" + item.__str__() + "\n"
        return result

    def delete_node(self, node: Node):
        if node is None:
            raise Exception("No item provided")

        if not self.content.__contains__(node):
            raise Exception("No such item in current directory")

        node.parent = None
        self.content.remove(node)

    def move_node(self, node: Node, path: "Directory"):
        self.delete_node(node)
        node.parent = path
        path.content.append(node)
