from lab1.nodes.binary_file import BinaryFile
from lab1.nodes.directory import Directory


def test_binary_file_init():
    directory = Directory("dir", None, 5)
    binary_file = BinaryFile("BinaryFile", "", directory)

    assert binary_file.name == "BinaryFile"
    assert directory.content.__contains__(binary_file)


def test_delete():
    directory = Directory("dir", None, 5)
    binary_file = BinaryFile("BinaryFile", "", directory)
    binary_file.delete()

    assert directory.content.__contains__(binary_file) is False


def test_move():
    directory = Directory("dir", None, 5)
    directory2 = Directory("dir2", directory, 5)
    binary_file = BinaryFile("BinaryFile", "", directory)

    binary_file.move(directory2)

    assert directory2.content.__contains__(binary_file)
    assert directory.content.__contains__(binary_file) is False


def test_get_content():
    directory = Directory("dir", None, 5)
    binary_file = BinaryFile("BinaryFile", "1234", directory)

    assert binary_file.content == "1234"
