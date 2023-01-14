class Node:
    name: str
    def __eq__(self, other):
        if type(other) == Node:
            return False
        return self.name == other.name

    def __str__(self) -> str:
        return self.name
