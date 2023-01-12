from lab1.nodes.directory import Directory


class LogTextFile:
    def __init__(self, name: str, parent: Directory, content: str):
        pass

    def __delete__(self, instance):
        pass

    def move(self, new_parent):
        pass

    def getContent(self) -> str:
        pass

    def append(self, line: str):
        pass
