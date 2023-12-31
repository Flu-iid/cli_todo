from typer.testing import CliRunner
from cli_todo import cli, __version__, __app_name__

runner = CliRunner()

def test_version():
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}" in result.stdout
    