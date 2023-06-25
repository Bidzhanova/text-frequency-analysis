from typing import List


def add_words_to_russian_stopwords(stop_words: List[str]) -> List[str]:
    user_words = input('\nПеречислите через пробел слова, '
                       'которе хотите добавить в список исключений: ').lower().strip().split()
    stop_words.extend(set(user_words))
    print('Слова добавлены в список исключений.')

    return stop_words


def remove_words_from_russian_stopwords(stop_words: List[str]) -> List[str]:
    user_words = input('\nПеречислите через пробел слова, '
                       'которе хотите удалить из списка исключений: ').lower().strip().split()
    for word in user_words:
        if word in stop_words:
            stop_words.remove(word)
            print(f'Слово {word!r} было удалено из списка исключений.')
        else:
            print(f'Слова {word!r} нет в списке исключений.')

    return stop_words


def clear_russian_stopwords(stop_words: List[str]) -> List[str]:
    stop_words.clear()
    print('Все слова были удалены из списка исключений.')

    return stop_words


def set_word_len():
    user_choice = int(input('Укажите максимальное количество слов в диапазоне от 10 до 300: '))
    if user_choice < 10 or user_choice > 300:
        raise ValueError('Максимальное количество слов должно быть в диапазоне от 10 до 300 включительно.')

    return user_choice
