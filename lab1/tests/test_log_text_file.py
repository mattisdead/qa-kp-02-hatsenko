from lab1.nodes.directory import Directory
from lab1.nodes.log_text_file import LogTextFile


def test_log_text_file_init():
    directory = Directory("dir", None, 5)
    log_text_file = LogTextFile("LogTextFile", directory, "1234")

    assert log_text_file.name == "LogTextFile"
    assert directory.content.__contains__(log_text_file)

def test_delete():
    directory = Directory("dir", None, 5)
    log_text_file = LogTextFile("LogTextFile", directory, "1234")
    log_text_file.delete()

    assert directory.content.__contains__(log_text_file) is False

def test_move():
    directory = Directory("dir", None, 5)
    directory2 = Directory("dir2", directory, 5)
    log_text_file = LogTextFile("LogTextFile", directory, "1234")

    log_text_file.move(directory2)

    assert directory2.content.__contains__(log_text_file)
    assert directory.content.__contains__(log_text_file) is False

def test_get_content():
    directory = Directory("dir", None, 5)
    log_text_file = LogTextFile("LogTextFile", directory, "1234")

    assert log_text_file.get_content() == "1234"

def test_append():
    directory = Directory("dir", None, 5)
    log_text_file = LogTextFile("LogTextFile", directory, "1234")

    log_text_file.append("5678")

    assert log_text_file.content == "1234\n5678"