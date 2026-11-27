from app.commands import execute_command


def test_search_highlights_matches(capsys):
    execute_command('add Python "Hello this is Python"')
    execute_command('search THIS')
    assert "Hello [this] is Python" in capsys.readouterr().out


def test_search_without_matches(capsys):
    execute_command('search missing')
    assert "No matches found" in capsys.readouterr().out
