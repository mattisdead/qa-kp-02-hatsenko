from lab1.nodes.directory import Directory


def test_dir_init():
    dirParent = Directory("ParentDir", None, 5)
    dirChild = Directory("ChildDir", dirParent, 5)

    assert dirChild.parent == dirParent


def test_add_node():
    dirParent = Directory("ParentDir", None, 5)
    dirChild = Directory("ChildDir", None, 5)
    dirParent.add_node(dirChild)
    assert dirChild.parent == dirParent
    assert dirParent.content.__contains__(dirChild)


def test_add_node_when_maximum_reached():
    dirParent = Directory("ParentDir", None, 1)
    dirChild1 = Directory("ChildDir", None, 1)
    dirChild2 = Directory("ChildDir2", None, 1)
    dirParent.add_node(dirChild1)
    try:
        dirParent.add_node(dirChild2)
    except OverflowError:
        pass
    assert dirParent.content.__contains__(dirChild2) == False


def test_remove_node():
    dirParent = Directory("ParentDir", None, 5)
    dirChild = Directory("ChildDir", None, 5)

    dirParent.add_node(dirChild)
    dirParent.delete_node(dirChild)

    assert dirParent.content.__contains__(dirChild) == False


def test_move_node():
    dirParentInitial = Directory("ParentDirInitial", None, 5)
    dirParentNew = Directory("ParentDirNew", None, 5)
    dirChild = Directory("ChildDir", None, 5)

    dirParentInitial.add_node(dirChild)
    dirParentInitial.move_node(dirChild, dirParentNew)

    assert dirParentInitial.content.__contains__(dirChild) == False
    assert dirParentNew.content.__contains__(dirChild)
