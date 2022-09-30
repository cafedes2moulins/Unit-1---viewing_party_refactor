import pytest
from viewing_party.person import Person


def test_1():
    # Arrange and Act
    ariel_movie_list = Person("Ariel", [], ["Julia", "Tara"], ["Netflix", "Hulu"])
   

    # Assert
    assert(ariel_movie_list.name == "Ariel")
    assert(ariel_movie_list.watched == [])
    assert(ariel_movie_list.friends == ["Julia", "Tara"])
    assert(ariel_movie_list.subscriptions == ["Netflix", "Hulu"])