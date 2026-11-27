from app.commands import execute_command


def test_exit():
    assert execute_command('exit') is True
