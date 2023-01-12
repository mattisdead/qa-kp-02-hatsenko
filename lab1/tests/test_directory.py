from lab1.nodes.directory import Directory


def test_dir_init():
    dir_parent = Directory("ParentDir", None, 5)
    dir_child = Directory("ChildDir", dir_parent, 5)

    assert dir_child.parent == dir_parent


def test_add_node():
    dir_parent = Directory("ParentDir", None, 5)
    dir_child = Directory("ChildDir", None, 5)
    dir_parent.add_node(dir_child)
    assert dir_child.parent == dir_parent
    assert dir_parent.content.__contains__(dir_child)


def test_add_node_when_maximum_reached():
    dir_parent = Directory("ParentDir", None, 1)
    dir_child1 = Directory("ChildDir", None, 1)
    dir_child2 = Directory("ChildDir2", None, 1)
    dir_parent.add_node(dir_child1)
    try:
        dir_parent.add_node(dir_child2)
    except OverflowError:
        pass
    assert dir_parent.content.__contains__(dir_child2) is False


def test_remove_node():
    dir_parent = Directory("ParentDir", None, 5)
    dir_child = Directory("ChildDir", None, 5)

    dir_parent.add_node(dir_child)
    dir_parent.delete_node(dir_child)

    assert dir_parent.content.__contains__(dir_child) is False


def test_move_node():
    dir_parent_initial = Directory("ParentDirInitial", None, 5)
    dir_parent_new = Directory("ParentDirNew", None, 5)
    dir_child = Directory("ChildDir", None, 5)

    dir_parent_initial.add_node(dir_child)
    dir_parent_initial.move_node(dir_child, dir_parent_new)

    assert dir_parent_initial.content.__contains__(dir_child) is False
    assert dir_parent_new.content.__contains__(dir_child)
