import string
from typing import List

from nltk.corpus import stopwords
from wordcloud import WordCloud

from file import (
    check_extension,
    convert_folders_path_to_str,
    find_file,
    unzip_file,
    read_file
)

from user_settings import (
    add_words_to_russian_stopwords,
    remove_words_from_russian_stopwords,
    clear_russian_stopwords,
    set_word_len,
)

from word_cloud import (
    tokenize_text,
    lemmatize_tokens,
    lemma_list_to_text,
    make_wordcloud,
    show_figure
)

spec_chars: tuple = (string.punctuation, string.digits, '–”«»\t—…’')

russian_stopwords: List[str] = stopwords.words("russian")
russian_stopwords.extend([
    'который', 'следовательно', 'кроме', 'один', 'вследствие', 'например', 'относиться', 'такой', 'являться', 'мочь',
    'именно', 'самый', 'каждый', 'снова', 'всякий', 'оставаться', 'первый', 'постоянно', 'предмет', 'случай',
    'необходимый', 'постоянный', 'различие', 'сторона', 'поскольку', 'также', 'говорить', 'поэтому', 'свой',
    'совершенно', 'однако', 'вообще', 'следующий', 'известный', 'определённый', 'друг', 'посредством', 'находиться',
    'различный', 'отдельный', 'второй', 'образовать', 'новый', 'последний', 'образ', 'данный', 'выражение',
    'обстоятельство', 'report', 'больший', 'часть', 'простой', 'весь', 'далее', 'лишь', 'хотя', 'почему', 'дядя',
    'несколько', 'отвечать', 'глаз', 'рука', 'город', 'двадцать', 'каракатица', 'город', 'начать', 'пора', 'брат',
    'казаться', 'взгляд', 'несколько', 'отвечать', 'нравиться', 'слово', 'решить', 'лицо', 'старший', 'юный', 'ребёнок',
    'пять', 'место', 'человек', 'очень', 'хороший', 'пятнадцать', 'третий', 'однажды', 'сделать', 'спросить', 'десять',
    'улица', 'дверь', 'маленький', 'день', 'начало', 'любой', 'отец', 'мать', 'семь', 'мужчина', 'женщина', 'стоять',
    'сказать', 'немой', 'волос', 'идти', 'малый', 'книга', 'национальный', 'мыло', 'мальчик', 'дорога', 'бывать',
    'вечер', 'весьма', 'вскоре', 'часто', 'должный', 'правда',
]),

print('\nПривет! Я - консольное приложение. Умею создавать PNG-файлы на основе '
      'наиболее часто встречающихся слов в тексте. Просто следуйте инструкциям.\n')

while True:

    file_name: str = input('Я работаю с файлами, имеющими расширение .zip или .txt.'
                           ' Укажите имя файла, на основе которого будет создано изображение, с расширением.'
                           ' Например: capital.zip or capital.txt.\nИмя файла с расширением: ')

    try:
        extension: str = check_extension(file_name)

    except ValueError:
        print('Неверно указано расширение файла. Используйте в качестве расширения только .zip или .txt')
        user_choice: str = input('Попробуем ещё раз? да/нет: ').lower()
        if user_choice == 'да':
            continue
        elif user_choice == 'нет':
            print('Хорошего дня!')
            break

    else:
        folders_path_lst: List[str] = input(f'\nУкажите через пробелы путь к файлу {file_name!r}. '
                                            f'Диск и имя файла указывать не надо. '
                                            f'Например: Users Public Python\nПуть к файлу {file_name!r}: ').split()
        try:
            folders_path_str: str = convert_folders_path_to_str(folders_path_lst)
            file_path: str = find_file(folders_path_str, file_name)
        except FileNotFoundError:
            print('Файл не найден. Возможно, путь к нему указан неверно или такого файла не существует.')
            raise

        txt_file = file_path
        if extension == 'zip':
            txt_file: str = unzip_file(file_path=file_path)

        text: str = read_file(txt_file=txt_file)

        text_tokens: List[str] = tokenize_text(text_=text, special_chars=spec_chars)

        try:
            u_choice = int(input(
                f'\nДалее программа сгенерирует PNG файл из наиболее часто встречающихся в тексте слов за исключением: '
                f'{russian_stopwords}.\nВы можете добавить слова в список исключений или удалить их'
                f' из него.\n1 - продолжить\n2 - добавить одно или несколько слов\n3 - удалить одно или несколько слов'
                f'\n4 - очистить список и продолжить\n5 - очистить список и добавить стоп-слова'
                f'\nВыберите номер действия: '))
        except ValueError:
            print('Введено не число.')
            raise

        user_stop_words = []
        if u_choice == 1:
            user_stop_words = russian_stopwords.copy()
        if u_choice == 2:
            user_stop_words = add_words_to_russian_stopwords(stop_words=russian_stopwords.copy())
        if u_choice == 3:
            user_stop_words = remove_words_from_russian_stopwords(stop_words=russian_stopwords.copy())
        if u_choice == 4:
            user_stop_words = clear_russian_stopwords(stop_words=russian_stopwords.copy())
        if u_choice == 5:
            user_clear_stop_words = clear_russian_stopwords(stop_words=russian_stopwords.copy())
            user_stop_words = add_words_to_russian_stopwords(stop_words=user_clear_stop_words)

        lemma_list: List[str] = lemmatize_tokens(tokens_=text_tokens, u_stopwords=user_stop_words)

        new_text: str = lemma_list_to_text(lemma=lemma_list)

        usr_choice = input('\nПо умолчанию максимальное количество генерируемых слов равно 100. '
                           'Хотите изменить эту настройку? да/нет\nВаш выбор: ')
        if usr_choice == 'да':
            words_qty = set_word_len()
            wordcloud: WordCloud = make_wordcloud(txt=new_text, u_stopwords=set(user_stop_words), words_qty=words_qty)
        else:
            wordcloud: WordCloud = make_wordcloud(txt=new_text, u_stopwords=set(user_stop_words))

        show_figure(w_cloud=wordcloud)

    break
