from app import store
from app.commands import execute_command


def test_delete_existing_entry():
    execute_command('add Python note')
    execute_command('delete 0')
    assert store.get_title_and_its_contents(0) == (None, None)


def test_delete_missing_entry(capsys):
    execute_command('delete 9')
    assert "No entry found with ID 9" in capsys.readouterr().out


def test_delete_negative_id(capsys):
    execute_command('delete -1')
    assert "ID cannot be negative" in capsys.readouterr().out
