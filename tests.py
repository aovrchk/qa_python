from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    #add_new_book Проверяем, что книге присваивается рейтинг 1
    def test_add_new_book_will_set_rating_one_for_book(self):
        #Создать экземпляр класса BooksCollector
        collector = BooksCollector()

        #Добавить новую книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        #Проверить, что ей присвоен рейтинг именно 1
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1

    #set_book_rating Проверить, что если переданного имени нет в словаре books_rating, содержание словаря не изменится
    def test_set_book_rating_unknown_book_will_not_set_rating_for(self):
        #Создать экземпляр класса BooksCollector
        collector = BooksCollector()
        #Добавить в словарь books_rating новую книгу
        collector.add_new_book('Гордость и предубеждение и зомби')

        #Передать имя книги не из словаря
        collector.set_book_rating('Война и мир', 6)

        #Проверить, что содержание словаря не изменилось
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1 and len(collector.get_books_rating()) == 1

    #get_book_rating Проверить, что полученный рейтинг соответствует рейтингу книги с переданным названием
    def test_get_book_rating_book_from_dictionary_books_rating_will_return_its_rating(self):
        #Создать экземпляр класса BooksCollector
        collector = BooksCollector()
        #Добавить в словарь books_rating новую книгу
        collector.add_new_book('Гордость и предубеждение и зомби')

        #Присвоить рейтинг книге
        collector.set_book_rating('Гордость и предубеждение и зомби', 3)

        #Убедиться, что рейтинги совпадают
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 3

    #get_books_with_specific_rating Проверить, что если передать рейтинг, которому не соответсвует ни одна книга, вернется пустой список
    def test_get_books_with_specific_rating_ubsent_rating_will_return_empty_list(self):
        #Создать экземпляр класса BooksCollector
        collector = BooksCollector()

        #Добавить в словарь books_rating 2 новые книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        #Задать добавленным книгам разные рейтинги
        collector.set_book_rating('Гордость и предубеждение и зомби', 6)
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 5)

        #Запросить книги с другим рейтингом, проверить, что вернется пустой массив
        assert not collector.get_books_with_specific_rating(2)

    #get_books_rating Проверить, что возвращается корректный словарь books_rating
    def test_get_books_rating_will_return_books_rating_dictionary(self):
        #Создать словарь с ожидаемым результатом
        expected_dictionary = {'Гордость и предубеждение и зомби': 1, 'Что делать, если ваш кот хочет вас убить': 1}

        #Создать экземпляр класса BooksCollector
        collector = BooksCollector()

        #Добавить в словарь books_rating 2 новые книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        #Проверить, что словари совпадают
        assert collector.get_books_rating() == expected_dictionary

    #add_book_in_favorites Проверить, что если книга уже есть в избранном, она не добавится второй раз
    def test_add_book_in_favorites_book_added_to_favorites_previously_will_not_be_added_second_time(self):
        #Создать список с ожидаемым результатом
        expected_list = ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']

        #Создать экземпляр класса BooksCollector
        collector = BooksCollector()

        #Добавить в избранное 2 книги
        for book in expected_list:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)

        #Добавить в избранное книгу, которая уже добавлена в избранном
        collector.add_book_in_favorites(expected_list[1])

        #Сверить список до и после, не должен измениться
        assert collector.get_list_of_favorites_books() == expected_list

    #delete_book_from_favorites Проверить, что если передать имя книги, которой нет в списке, список не изменится
    def test_delete_book_from_favorites_book_not_added_to_favorites_favorites_list_will_not_change(self):
        #Создать список с ожидаемым результатом
        expected_list = ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']

        #Создать экземпляр класса BooksCollector
        collector = BooksCollector()

        #Добавить в избранное 2 книги
        for book in expected_list:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)

        #Удалить из списка книгу, которой нет в избранном
        collector.delete_book_from_favorites('Война и мир')

        #Проверить, что список не изменился
        assert collector.get_list_of_favorites_books() == expected_list

    #get_list_of_favorites_books Проверить, что возвращается корректный список избранных книг
    def test_get_list_of_favorites_books_will_return_favorites_books_list(self):
        #Создать список с ожидаемым результатом
        expected_list = ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']

        #Создать экземпляр класса BooksCollector
        collector = BooksCollector()

        #Добавить в избранное 2 книги
        for book in expected_list:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)

        #Проверить, что списки совпадают
        assert collector.get_list_of_favorites_books() == expected_list

    #__init__ Проверить, что books_rating будет пустым словарем
    def test_books_rating_will_be_an_empty_dictionary_after_creating_an_instance_of_the_class(self):
        #Проверить, что books_rating - пустой словарь
        assert not BooksCollector().get_books_rating()

