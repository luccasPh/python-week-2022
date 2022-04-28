from beerlog.core import get_beers_database, add_beer_database


def test_add_beer_database():
    assert add_beer_database("Test Beer", "TBR", 3, 5, 7)


def test_get_beers_database():
    add_beer_database("Test Beer", "TBR", 3, 5, 7)

    result = get_beers_database()

    assert len(result) > 0
