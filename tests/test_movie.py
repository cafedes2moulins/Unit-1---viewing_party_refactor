import pytest
from viewing_party.movie import Movie

def test_1():
    # Arrange
    #(title, genre, rating, host)
    # Act
    spider_man = Movie("Spider Man", "Action", 2, "Netflix")
    # Assert
    assert(spider_man.title == "Spider Man")
    assert(spider_man.genre == "Action")
    assert(spider_man.rating == 2)
    assert(spider_man.host == "Netflix")

def test_update_rating():
    # Arrange
    spider_man = Movie("Spider Man", "Action", 2, "Netflix")

    # Act
    spider_man.update_rating(5)

    # Assert
    assert(spider_man.rating == 5)