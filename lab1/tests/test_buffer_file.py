from lab1.nodes.buffer_file import BufferFile
from lab1.nodes.directory import Directory


def test_binary_file_init():
    directory = Directory("dir", None, 5)
    buffer_file = BufferFile("BufferFile", directory, 3)

    assert buffer_file.name == "BufferFile"
    assert directory.content.__contains__(buffer_file)


def test_delete():
    directory = Directory("dir", None, 5)
    buffer_file = BufferFile("BufferFile", directory, 3)
    buffer_file.delete()

    assert directory.content.__contains__(buffer_file) is False


def test_move():
    directory = Directory("dir", None, 5)
    directory2 = Directory("dir2", directory, 5)
    buffer_file = BufferFile("BufferFile", directory, 3)

    buffer_file.move(directory2)

    assert directory2.content.__contains__(buffer_file)
    assert directory.content.__contains__(buffer_file) is False


def test_push():
    directory = Directory("dir", None, 5)
    buffer_file = BufferFile("BufferFile", directory, 3)

    buffer_file.push("1234")

    assert buffer_file.content.__contains__("1234")


def test_consume():
    directory = Directory("dir", None, 5)
    buffer_file = BufferFile("BufferFile", directory, 3)

    buffer_file.push("1234")
    buffer_file.consume("1234")

    assert buffer_file.content.__contains__("1234") is False
    assert len(buffer_file.content) == 0
