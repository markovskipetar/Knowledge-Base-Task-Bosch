from app.commands import execute_command


def test_show_existing_entry(capsys):
    execute_command('add Python note')
    execute_command('show 0')
    assert capsys.readouterr().out == "Python:\n - note\n"


def test_show_missing_entry(capsys):
    execute_command('show 9')
    assert "No entry found with ID 9" in capsys.readouterr().out


def test_show_invalid_id(capsys):
    execute_command('show abc')
    assert "ID must be an integer" in capsys.readouterr().out
