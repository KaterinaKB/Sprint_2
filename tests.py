import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books_length_is_right(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_add_book_book_is_in_collection(self):
        collector = BooksCollector()
        collector.add_new_book('Севастопольские рассказы')
        assert 'Севастопольские рассказы' in collector.books_rating

    def test_add_new_book_add_book_book_rating_is_one(self, new_books):
        assert new_books.books_rating['Harry Potter and Goblet of fire'] == 1

    @pytest.mark.parametrize('valid_boundary_values', [1, 10])
    def test_set_book_rating_valid_boundary_values_rating_updated(self, new_books, valid_boundary_values):
        new_books.set_book_rating('Harry Potter and Goblet of fire', valid_boundary_values)
        assert new_books.books_rating['Harry Potter and Goblet of fire'] == valid_boundary_values

    @pytest.mark.parametrize('invalid_values', [-1, 0, 11, ' ', '', 'a', '1', 9.99])
    def test_set_book_rating_invalid_values_rating_not_updated(self, new_books, invalid_values):
        new_books.set_book_rating('Harry Potter and Goblet of fire', invalid_values)
        assert new_books.books_rating['Harry Potter and Goblet of fire'] == 1

    def test_get_book_rating_book_from_collection_rating_returned(self, new_books, collection_with_rating):
        assert collection_with_rating.get_book_rating('Идиот') == 10

    def test_get_books_with_specific_rating_valid_rating_correct_list_returned(self, new_books, collection_with_rating):
        assert 'Harry Potter and Goblet of fire' in collection_with_rating.get_books_with_specific_rating(8) and 'Неаполитанский квартет' in collection_with_rating.get_books_with_specific_rating(8) and len(collection_with_rating.get_books_with_specific_rating(8)) == 2

    @pytest.mark.parametrize('invalid_values', [-1, 0, 11, ' ', '', 'a', '1', 9.99])
    def test_get_books_with_specific_rating_invalid_rating_empty_list_returned(self, new_books, collection_with_rating, invalid_values):
        assert collection_with_rating.get_books_with_specific_rating(invalid_values) == []

    def test_get_books_rating_collection_returned(self, new_books, collection_with_rating):
        assert collection_with_rating.get_books_rating() == {'Harry Potter and Goblet of fire': 8, 'Идиот': 10, 'Неаполитанский квартет': 8}

    def test_add_book_in_favorites_book_in_collection_book_added_to_favorities(self, new_books):
        new_books.add_book_in_favorites('Идиот')
        assert 'Идиот' in new_books.favorites

    def test_add_book_in_favorites_book_not_in_collection_book_not_added_to_favorities(self, new_books):
        new_books.add_book_in_favorites('Рукоделие из собачьей шерсти')
        assert new_books.favorites == []

    def test_add_book_in_favorites_book_already_in_favorities_book_not_added_to_favorities(self, new_books, list_of_favorities):
        new_books.add_book_in_favorites('Идиот')
        assert new_books.favorites.count('Идиот') == 1

    def test_delete_book_from_favorites_book_in_favorities_book_deleted_from_favorities(self, new_books, list_of_favorities):
        new_books.delete_book_from_favorites('Идиот')
        assert 'Идиот' not in new_books.favorites

    def test_get_list_of_favorites_books_list_returned(self, new_books, list_of_favorities):
        assert new_books.favorites == ['Идиот', 'Неаполитанский квартет']

