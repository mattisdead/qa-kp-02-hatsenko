from lab1.nodes.binary_file import BinaryFile
from lab1.nodes.directory import Directory

dirParent = Directory("ParentDir", None, 5)
dirChild = Directory("ChildDir", dirParent, 5)
dirChildChild = Directory("ChildChildDir", dirChild, 5)
binaryFile = BinaryFile("BinaryFile", "1234", dirChildChild)
binaryFile2 = BinaryFile("BinaryFile2", "123456", dirChildChild)

print(dirParent.get_content(1))