from lab1.nodes.binary_file import BinaryFile
from lab1.nodes.directory import Directory
from lab1.nodes.buffer_file import BufferFile
from lab1.nodes.log_text_file import LogTextFile

dir_parent = Directory("Parent Dir", None, 5)
dir_child = Directory("Child Dir", dir_parent, 5)
dir_child_child = Directory("Child Child Dir", dir_child, 5)

binary_file = BinaryFile("Binary File", "1234", dir_child_child)
binary_file2 = BinaryFile("2nd binary file", "2nd", dir_parent)
buffer_file = BufferFile("Buffer File", dir_child_child, 10)
log_text_file = LogTextFile("Log test file", dir_child, "Hello World")

print(dir_parent.get_content(1))