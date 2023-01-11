class Directory:
    def __init__(self, name: str, path: str, elementCapacity: int):
        self.name = name
        self.path = path
        self.elementCapacity = elementCapacity
    def __delete__(self, instance):
        del self
    def getContent(self):
        pass
    def moveContent(self):
        pass