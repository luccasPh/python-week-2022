from typer.testing import CliRunner

from beerlog.cli import main

runner = CliRunner()


def test_add_beer():
    result = runner.invoke(
        main, ["add", "Test Beer", "TBR", "--flavor=3", "--image=5", "--cost=7"]
    )
    assert result.exit_code == 0
    assert "🍺 beer added successfully" in result.output
