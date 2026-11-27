from app.commands import execute_command


def test_list_entries(capsys):
    execute_command('add Python note')
    execute_command('add Java note')
    execute_command('list')
    assert capsys.readouterr().out == "0 | Python\n1 | Java\n"


def test_list_empty(capsys):
    execute_command('list')
    assert capsys.readouterr().out == ""
