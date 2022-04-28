from typing import Optional
import typer
from beerlog.core import add_beer_database, get_beers_database
from rich.table import Table
from rich.console import Console

main = typer.Typer(help="Beerlog CLI")
console = Console()


@main.command("add")
def add_beer(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """
    Add a beer to the database.
    """
    if add_beer_database(name, style, flavor, image, cost):
        print("🍺 beer added successfully")


@main.command("list")
def list_beers(style: Optional[str] = typer.Option(None)):
    """
    List all beers in the database.
    """
    beers = get_beers_database()
    table = Table(title="Beerlog :beer_mug:")
    headers = ["id", "name", "style", "rate", "created_at"]
    for header in headers:
        table.add_column(header, style="magenta")

    for beer in beers:
        beer.created_at = beer.created_at.strftime("%d/%m/%Y")
        values = [str(getattr(beer, header)) for header in headers]
        table.add_row(*values)

    console.print(table)
