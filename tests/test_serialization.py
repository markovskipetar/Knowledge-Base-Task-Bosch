from app import serialization, store


def test_save_and_load_preserves_last_used_id(tmp_path):
    path = tmp_path / "knowledge.json"
    store.add("First", "Content")
    store.add("Deleted", "Content")
    store.delete(1)
    serialization.save(path)

    store.title_to_contents.clear()
    store.id_to_title.clear()
    store.set_last_used_title_id(-1)
    serialization.load(path)
    store.add("New", "Content")

    assert store.get_all_ids_and_titles() == [(0, "First"), (2, "New")]
    assert store.get_title_and_its_contents(0) == ("First", ["Content"])
