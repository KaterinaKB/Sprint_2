from main import BooksCollector
import pytest as pytest

@pytest.fixture
def new_books():
    collector = BooksCollector()
    collector.add_new_book('Harry Potter and Goblet of fire')
    collector.add_new_book('Идиот')
    collector.add_new_book('Неаполитанский квартет')
    return collector


@pytest.fixture
def collection_with_rating(new_books):
    new_books.set_book_rating('Harry Potter and Goblet of fire', 8)
    new_books.set_book_rating('Идиот', 10)
    new_books.set_book_rating('Неаполитанский квартет', 8)
    return new_books

@pytest.fixture
def list_of_favorities(new_books):
    new_books.add_book_in_favorites('Идиот')
    new_books.add_book_in_favorites('Неаполитанский квартет')
    return list_of_favorities
