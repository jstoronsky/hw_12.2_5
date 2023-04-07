from utilss import dicts


def test_one():
    collection = {"subaru": "impreza"}
    assert dicts.get_val(collection, "subaru") == "impreza"
    assert dicts.get_val(collection, "subaru", "lancer") == "impreza"


def test_two():
    collection = {"subaru": "impreza"}
    assert dicts.get_val(collection, "subarissimo", "lancer") == "lancer"


def test_three():
    collection = {}
    assert dicts.get_val(collection, "subaru", "lancer") == "lancer"


def test_four():
    assert dicts.get_val({}, "subaru", "lancer") == "lancer"
