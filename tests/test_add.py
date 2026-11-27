from app import store
from app.commands import execute_command


def test_add_new_title():
    execute_command('add Python "First note"')
    assert store.get_title_and_its_contents(0) == ("Python", ["First note"])


def test_add_existing_title():
    execute_command('add Python "First note"')
    execute_command('add Python "Second note"')
    assert store.get_title_and_its_contents(0) == ("Python", ["First note", "Second note"])
    assert len(store.get_all_ids_and_titles()) == 1


def test_add_empty_title(capsys):
    execute_command('add "" content')
    assert "Title is empty" in capsys.readouterr().out
